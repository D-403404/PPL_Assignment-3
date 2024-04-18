# from AST import *
# from Visitor import *
# from Utils import Utils
# from StaticError import *
# from functools import reduce

from main.zcode.utils.AST import *
from main.zcode.utils.Visitor import *
from main.zcode.utils.Utils import Utils
from StaticError import *
from functools import reduce


class StaticChecker(BaseVisitor, Utils):
    def __init__(self, ast):
        self.ast = ast
        self.symlst = [{}]  # array of dicts
        # o: [{'a': ('var', NumberType()), 'b': ('func', VoidType()), ...}, {}, {'a': ('var', BoolType())}, ...]    wrong
        # o: [{'a.var': VariableSymbol('a', NumberType()), 'b.func': FunctionSymbol('b', VoidType()), ...}, {}, {'a.var': VariableSymbol('a', BoolType())}, ...]    wrong
        # o: [{'a': VariableSymbol('a', NumberType()), 'b': FunctionSymbol('b', VoidType()), ...}, {}, {'a': VariableSymbol('a', BoolType())}, ...]    wrong
        self.decl_lhs = None
        self.arraylst = []
        self.nobodylst = []
        self.visited_return = False
        self.curr_func_name = ''
        self.looplst = []

    # Utils
    # def lookup(self, name, lst, func):
    #     for x in lst:
    #         if name == func(x):
    #             return x
    #     return None

    # BaseVisitor
    # def visit(self, ast, param):
    #     return ast.accept(self, param)
        
    def lookupScope(self, name, lst):  # lookup the scope containing name
        for scope in lst:
            if name in scope:
                return scope

    def check(self):
        self.visit(self.ast, None)

    def visitProgram(self, ast, param):
        symbol_table = [{}]
        for decl in ast.decl:
            self.visit(decl, symbol_table)

        if 'main.func' not in symbol_table[-1]:
            raise NoEntryPoint()
        if type(symbol_table[-1]['main.func'].type) is not VoidType or len(symbol_table[-1]['main.func'].paramlst) != 0:
            raise NoEntryPoint()

        if self.nobodylst != []:
            raise NoDefinition(self.nobodylst[0])

    def visitVarDecl(self, ast, param):
        if ast.name + '.var' in param[0] or ast.name + '.func' in param[0]:
            raise Redeclared(Variable(), ast.name)
        
        if ast.varInit is not None:
            lhs_typ = ast.varType
            rhs_typ = self.visit(ast.varInit, param)
            if lhs_typ is None and rhs_typ is None:
                raise TypeCannotBeInferred(ast)
            elif lhs_typ is None:
                param[0][ast.name + '.var'] = VariableSymbol(ast.name, rhs_typ)
            elif rhs_typ is None:
                rhs_check = self.checkType(ast, ast.varInit, rhs_typ, lhs_typ, param, 1)
                if rhs_check is None:
                    raise TypeCannotBeInferred(ast)
                rhs_typ = lhs_typ
                param[0][ast.name + '.var'] = VariableSymbol(ast.name, rhs_typ)
            elif type(lhs_typ) is not type(rhs_typ):
                raise TypeMismatchInStatement(ast)
            elif type(lhs_typ) is ArrayType:
                if rhs_typ.size[:len(lhs_typ.type.size)] != lhs_typ.type.size:  # [[a,b],[3,4]] => dont know size of a,b => [a,b] size is [2,?]
                    raise TypeMismatchInStatement(ast)
                
                if rhs_typ.eleType is None:
                    if self.checkType(ast, ast.rhs, rhs_typ, lhs_typ, param, 1) is not None:
                        rhs_typ = lhs_typ
                    else:
                        raise TypeCannotBeInferred(ast)

                if rhs_typ.size != lhs_typ.size or rhs_typ.eleType is not lhs_typ.eleType:
                    raise TypeMismatchInStatement(ast)
            else:
                param[0][ast.name + '.var'] = VariableSymbol(ast.name, lhs_typ)
        
        self.arraylst = []

    def visitFuncDecl(self, ast, param):
        scope = param[-1]   # global scope
        if ast.name + '.var' in scope:
            raise Redeclared(Function(), ast.name)

        paramlst = [{}]
        for decl in ast.param:
            self.visit(decl, paramlst)
        function_scope = paramlst + param

        if ast.name + '.func' in scope:
            symbol = scope[ast.name + '.func']
            if symbol.body is not None:
                raise Redeclared(Function(), ast.name)
            if ast.body is None:    # redeclare function declaration
                raise Redeclared(Function(), ast.name)
            # symbol.body is None and ast.body is not None
            # process like ast.name not in scope, except check param and pop ast out of nobodylst
            if len(ast.param) != len(symbol.param): # different # of params
                raise Redeclared(Function(), ast.name)
            for idx in range(len(paramlst)):
                if paramlst[paramlst.keys()[idx]] != symbol.param[symbol.param.keys()[idx]]:    # different type of params
                    raise Redeclared(Function(), ast.name)

            for idx in range(len(self.nobodylst)):
                if self.nobodylst[idx].name == ast.name:
                    self.nobodylst.pop(idx)
                    break

        if ast.body is None:
            scope[ast.name + '.func'] = FunctionSymbol(ast.name, None, paramlst, ast.body)
            self.nobodylst += [ast]
        else:
            func_typ = self.visit(ast.body, function_scope)
            scope[ast.name + '.func'] = FunctionSymbol(ast.name, func_typ, paramlst, ast.body)
        
        self.visited_return = False

    def visitNumberType(self, ast, param):
        return NumberType()

    def visitBoolType(self, ast, param):
        return BoolType()

    def visitStringType(self, ast, param):
        return StringType()

    def visitArrayType(self, ast, param):
        return ArrayType(ast.size, ast.eleType)

    def inferType(self, ast: Id | ArrayLiteral | CallExpr | CallStmt, req_op_typ, param):
        if type(ast) is Id:
            for scopedict in param:
                # res = self.lookup(ast.name + '.var', scopedict.keys(), lambda id: id)
                # if res is not None and type(scopedict[res + '.var']) is VariableSymbol:
                if ast.name + '.var' in scopedict:
                    symbol = scopedict[ast.name + '.var']
                    scopedict[ast.name + '.var'] = VariableSymbol(symbol.name, req_op_typ)
                    return True
        
        if type(ast) is ArrayLiteral:
            inferred = False
            if type(req_op_typ) is ArrayType:  
                for expr in ast.value:
                    if len(req_op_typ.size) == 1:   # 1d array
                        inferred = self.inferType(expr, req_op_typ.eleType, param)
                    else:
                        inferred = self.inferType(expr, ArrayType(req_op_typ.size[1:], req_op_typ.eleType), param)
                return inferred

        if type(ast) in [CallExpr, CallStmt]:
            scope = param[-1]
            if ast.name + '.func' in scope:
                symbol = scopedict[ast.name + '.func']
                scope[ast.name + '.func'] = FunctionSymbol(symbol.name, req_op_typ, symbol.paramlst, symbol.body)

        return False

    def checkType(self, ast, op, op_typ, req_op_typ, param, type = 0):
        if op_typ is None:  # infer type
            if type(op) in [Id, CallExpr, ArrayLiteral]:
                inferred = self.inferType(op, req_op_typ, param)
                if inferred:
                    return req_op_typ
                return None
            return None

        if type(op_typ) is not type(req_op_typ):
            if type == 0:
                raise TypeMismatchInExpression(ast)
            else:
                raise TypeMismatchInStatement(ast)

        return req_op_typ

    def visitBinaryOp(self, ast, param):
        left_typ = self.visit(ast.left, param)
        right_typ = self.visit(ast.right, param)

        # if left_typ is None and type(ast.left) is Id:
        #     left_scope = self.lookupScope(ast.left)
        # if right_typ is None and type(ast.right) is Id:
        #     right_scope = self.lookupScope(ast.right)

        if ast.op in ['+', '-', '*', '/', '%']:
            # if type(ast.left) is Id:
            #     left_scope[ast.left.name] = NumberType
            # if type(ast.right) is Id:
            #     right_scope[ast.right.name] = NumberType
            # if type(left_typ) is not NumberType or type(right_typ) is not NumberType:
            #     raise TypeMismatchInExpression(ast)
            left_check = self.checkType(ast, ast.left, left_typ, NumberType(), param)
            right_check = self.checkType(ast, ast.right, right_typ, NumberType(), param)
            if left_check is None or right_check is None:
                return None
            return NumberType()
        
        if ast.op in ['and', 'or']:
            left_check = self.checkType(ast, ast.left, left_typ, BoolType(), param)
            right_check = self.checkType(ast, ast.right, right_typ, BoolType(), param)
            if left_check is None or right_check is None:
                return None
            return BoolType()
        
        if ast.op == '...':
            left_check = self.checkType(ast, ast.left, left_typ, StringType(), param)
            right_check = self.checkType(ast, ast.right, right_typ, StringType(), param)
            if left_check is None or right_check is None:
                return None
            return StringType()
        
        if ast.op in ['=', '!=', '<', '>', '<=', '>=', '==']:
            if ast.op == '==':
                left_check = self.checkType(ast, ast.left, left_typ, StringType(), param)
                right_check = self.checkType(ast, ast.right, right_typ, StringType(), param)
            else:
                left_check = self.checkType(ast, ast.left, left_typ, NumberType(), param)
                right_check = self.checkType(ast, ast.right, right_typ, NumberType(), param)
            if left_check is None or right_check is None:
                return None
            return BoolType()

    def visitUnaryOp(self, ast, param):
        op_typ = self.visit(ast.operand, param)
        if ast.op == '-':
            return self.checkType(ast, ast.operand, op_typ, NumberType(), param)
        # op == 'not'
        return self.checkType(ast, ast.operand, op_typ, BoolType(), param)

    def visitCallExpr(self, ast, param):
        for scope in param[:-1]:
            if ast.name + '.var' in scope:  # a var with the same name as func
                raise TypeMismatchInExpression(ast)

        if ast.name + '.func' not in param[-1]:
            raise Undeclared(Function(), ast.name)
        
        symbol = param[-1][ast.name + '.func']
        if type(symbol.type) is VoidType:
            raise TypeMismatchInExpression(ast)
        if len(ast.args) != len(symbol.paramlst):
            raise TypeMismatchInExpression(ast)
        
        for idx in range(len(ast.args)):
            arg_typ = self.visit(ast.args[idx], param)
            arg_check = self.checkType(ast, ast.args[idx], arg_typ, symbol.paramlst[symbol.paramlst.keys()[idx]], param)
            if arg_check is None:
                return None
            # arg_typ = symbol.paramlst[symbol.paramlst.keys()[idx]]

            req_op_typ = symbol.paramlst[symbol.paramlst.keys()[idx]]
            if type(arg_typ) is ArrayType:
                if arg_typ.size[:len(req_op_typ.size)] != req_op_typ.size:  # [[a,b],[3,4]] => dont know size of a,b => [a,b] size is [2,?]
                    raise TypeMismatchInExpression(ast)
                
                if arg_typ.eleType is None:
                    if type(ast.args[idx]) in [Id, CallExpr, ArrayLiteral]:
                        if self.inferType(ast.args[idx], req_op_typ, param):
                            arg_typ = symbol.paramlst[symbol.paramlst.keys()[idx]]
                        else:
                            raise TypeCannotBeInferred(ast)
                    else:
                        raise TypeCannotBeInferred(ast)

                if arg_typ.size != symbol.paramlst[symbol.paramlst.keys()[idx]].size or arg_typ.eleType is not symbol.paramlst[symbol.paramlst.keys()[idx]].eleType:
                    raise TypeMismatchInExpression(ast)

    def visitId(self, ast, param):
        # param: list of scopes
        # scope/scopedict: dictionary of ids and their type
        # if self.decl_lhs is not None and ast.name == self.decl_lhs:
        #     raise Undeclared(Identifier(), ast.name)

        # found = None
        # scope = None
        # for scopedict in param:
        #     found = self.lookup(ast.name + '.var', list(scopedict.keys()), lambda id: id)
        #     scope = scopedict
        #     if found is not None:
        #         break
                
        # if found is None:
        #     raise Undeclared(Identifier(), ast.name)
        
        # for id in scope:
        #     if found == id:
        #         return scope[id]

        scope = self.lookupScope(ast.name + '.var', param)
        if scope is None:
            raise Undeclared(Identifier(), ast.name)
        return scope[ast.name + '.var'].type

    def visitArrayCell(self, ast, param):
        # arrayId_typ: type of the id of array (as in VarDecl)
        # ast.arr.eleType: type of elements of array
        arrayId_typ = self.visit(ast.arr, param)
        if arrayId_typ is None:
            return None
        
        if type(arrayId_typ) is not ArrayType:
            raise TypeMismatchInExpression(ast)
        if len(ast.idx) > (ast.arr.size):
            raise TypeMismatchInExpression(ast)
        for idx in ast.idx:
            idx_typ = self.visit(idx, param)
            idx_check = self.checkType(ast, idx, idx_typ, NumberType, param)
            if idx_check is None:
                return None
            
        if len(ast.arr.size) == len(ast.idx):
            return ast.arr.eleType
        return ArrayType(ast.arr.size[len(ast.idx):], ast.arr.eleType)

    def visitBlock(self, ast, param):
        block_scope = [{}] + param
        for stmt in ast.stmt:
            self.visit(stmt, block_scope)
        
        self.arraylst = []
        self.visited_return = False

    def visitIf(self, ast, param):
        self.visited_return = False
        expr_typ = self.visit(ast.expr, param)
        expr_check = self.checkType(ast, ast.expr, expr_typ, BoolType(), param, 1)
        if expr_check is None:
            raise TypeCannotBeInferred(ast)
        self.visit(ast.thenStmt, param)

        for stmt in ast.elifStmt:
            expr_typ = self.visit(stmt[0], param)
            expr_check = self.checkType(ast, stmt[0], expr_typ, BoolType(), param, 1)
            if expr_check is None:
                raise TypeCannotBeInferred(ast)
            self.visit(stmt[1], param)

        self.visit(ast.elseStmt)

        self.arraylst = []

    def visitFor(self, ast, param):
        self.visited_return = False
        self.looplst += [ast]

        name_typ = self.visit(ast.name, param)
        name_check = self.checkType(ast, ast.name, name_typ, NumberType(), param, 1)
        if name_check is None:
            raise TypeCannotBeInferred(ast)
        
        condExpr_typ = self.visit(ast.condExpr, param)
        condExpr_check = self.checkType(ast, ast.condExpr, condExpr_typ, BoolType(), param, 1)
        if condExpr_check is None:
            raise TypeCannotBeInferred(ast)
        
        updExpr_typ = self.visit(ast.updExpr, param)
        updExpr_check = self.checkType(ast, ast.updExpr, updExpr_typ, NumberType(), param, 1)
        if updExpr_check is None:
            raise TypeCannotBeInferred(ast)
        
        self.visit(ast.body, param)

        self.looplst.pop()
        self.arraylst = []

    def visitContinue(self, ast, param):
        if self.looplst == []:
            raise MustInLoop(ast)
        self.arraylst = []

    def visitBreak(self, ast, param):
        if self.looplst == []:
            raise MustInLoop(ast)
        self.arraylst = []

    def visitReturn(self, ast, param):
        if self.visited_return is True:
            return
        
        if ast.expr is None:
            return VoidType()
        
        ret_typ = self.visit(ast.expr, param)
        global_scope = param[-1]
        symbol = global_scope[self.curr_func_name + '.func']
        if symbol.type is None:
            if ret_typ is None:
                raise TypeCannotBeInferred(ast)
            # infer type of function
            global_scope[self.curr_func_name + '.func'] = FunctionSymbol(symbol.name, ret_typ, symbol.paramlst, symbol.body)

        # function has a type
        if type(symbol.type) is VoidType:
            raise TypeMismatchInStatement(ast)
        
        ret_check = self.checkType(ast, ast.expr, ret_typ, symbol.type, param)
        if ret_check is None:
            raise TypeCannotBeInferred(ast)
        ret_typ = symbol.type

        # if ret_typ is None:  # infer type
        #     if type(ast.expr) in [Id, CallExpr, ArrayLiteral]:
        #         inferred = self.inferType(ast.expr, symbol.type, param)
        #         if inferred:
        #             ret_typ = symbol.type
        #         else:
        #             raise TypeCannotBeInferred(ast)
        #     else:
        #         raise TypeCannotBeInferred(ast)

        # if type(ret_typ) is not type(symbol.type):
        #     raise TypeMismatchInStatement(ast)

        if type(ret_typ) is ArrayType:
            if ret_typ.size[:len(symbol.type.size)] != symbol.type.size:  # [[a,b],[3,4]] => dont know size of a,b => [a,b] size is [2,?]
                raise TypeMismatchInStatement(ast)
            
            if ret_typ.eleType is None:
                if type(ast.expr) in [Id, CallExpr, ArrayLiteral]:
                    if self.inferType(ast.expr, symbol.type, param):
                        ret_typ = symbol.type
                    else:
                        raise TypeCannotBeInferred(ast)
                else:
                    raise TypeCannotBeInferred(ast)

            if ret_typ.size != symbol.type.size or ret_typ.eleType is not symbol.type.eleType:
                raise TypeMismatchInStatement(ast)
            
        self.arraylst = []

    def visitAssign(self, ast, param):
        rhs_typ = self.visit(ast.rhs)
        lhs_typ = self.visit(ast.lhs)

        if lhs_typ is None and rhs_typ is None:
            raise TypeCannotBeInferred(ast)
        elif lhs_typ is None:
            if self.checkType(lhs_typ, rhs_typ, param) is None:
                raise TypeCannotBeInferred(ast)
        elif rhs_typ is None:
            if self.checkType(rhs_typ, lhs_typ, param) is None:
                raise TypeCannotBeInferred(ast)
        elif type(lhs_typ) is VoidType or type(rhs_typ) is VoidType:
            raise TypeMismatchInStatement(ast)
        elif type(lhs_typ) is not type(rhs_typ):
            raise TypeMismatchInStatement(ast)
        elif type(lhs_typ) is ArrayType:
                if rhs_typ.size[:len(lhs_typ.type.size)] != lhs_typ.type.size:  # [[a,b],[3,4]] => dont know size of a,b => [a,b] size is [2,?]
                    raise TypeMismatchInStatement(ast)
                
                if rhs_typ.eleType is None:
                    if self.checkType(ast, ast.rhs, rhs_typ, lhs_typ, param, 1) is not None:
                        rhs_typ = lhs_typ
                    else:
                        raise TypeCannotBeInferred(ast)

                if rhs_typ.size != lhs_typ.size or rhs_typ.eleType is not lhs_typ.eleType:
                    raise TypeMismatchInStatement(ast)

    def visitCallStmt(self, ast, param):
        for scope in param[:-1]:
            if ast.name + '.var' in scope:  # a var with the same name as func
                raise TypeMismatchInStatement(ast)

        if ast.name + '.func' not in param[-1]:
            raise Undeclared(Function(), ast.name)
        
        symbol = param[-1][ast.name + '.func']
        if type(symbol.type) is not None and type(symbol.type) is VoidType:
            raise TypeMismatchInExpression(ast)
        if len(ast.args) != len(symbol.paramlst):
            raise TypeMismatchInStatement(ast)
        
        for idx in range(len(ast.args)):
            arg_typ = self.visit(ast.args[idx], param)
            arg_check = self.checkType(ast, ast.args[idx], arg_typ, symbol.paramlst[symbol.paramlst.keys()[idx]], param)
            if arg_check is None:
                return None
            # arg_typ = symbol.paramlst[symbol.paramlst.keys()[idx]]

            req_op_typ = symbol.paramlst[symbol.paramlst.keys()[idx]]
            if type(arg_typ) is ArrayType:
                if arg_typ.size[:len(req_op_typ.size)] != req_op_typ.size:  # [[a,b],[3,4]] => dont know size of a,b => [a,b] size is [2,?]
                    raise TypeMismatchInStatement(ast)
                
                if arg_typ.eleType is None:
                    if type(ast.args[idx]) in [Id, CallExpr, ArrayLiteral]:
                        if self.inferType(ast.args[idx], req_op_typ, param):
                            arg_typ = symbol.paramlst[symbol.paramlst.keys()[idx]]
                        else:
                            raise TypeCannotBeInferred(ast)
                    else:
                        raise TypeCannotBeInferred(ast)

                if arg_typ.size != symbol.paramlst[symbol.paramlst.keys()[idx]].size or arg_typ.eleType is not symbol.paramlst[symbol.paramlst.keys()[idx]].eleType:
                    raise TypeMismatchInStatement(ast)
                
            if type(symbol.type) is None:
                if not self.inferType(ast, VoidType(), param):
                    raise TypeCannotBeInferred(ast)
                
        self.arraylst = []

    def visitNumberLiteral(self, ast, param):
        return NumberType()

    def visitBooleanLiteral(self, ast, param):
        return BoolType()

    def visitStringLiteral(self, ast, param):
        return StringType()

    # def checkArrayLiteral(self, ast, root_ast, param):  # to call recursion



    def visitArrayLiteral(self, ast, param):
        # array literal is not empty
        # param[0]: scope list              wrong
        # param[1]: array element type in VarDecl statement     wrong

        self.arraylst += [ast]
        arrayele_typ = None
        for expr in ast.value:
            arrayele_typ = self.visit(expr, param)
            if arrayele_typ is not None:
                break

        if arrayele_typ is None:
            return None

        for expr in ast.value:
            expr_typ = self.visit(expr, param)
            expr_check = self.checkType(ast, expr, expr_typ, arrayele_typ, param)
            if expr_check is None:
                return None
            expr_typ = arrayele_typ

            # if expr_typ is None:  # infer type
            #     if type(expr) in [Id, CallExpr, ArrayLiteral]:
            #         if self.inferType(expr, arrayele_typ, param):
            #             expr_typ = arrayele_typ
            #         else:
            #             return None
            #     else:
            #         return None

            # if type(expr_typ) is not type(arrayele_typ):
            #     raise TypeMismatchInExpression(self.arraylst[0])

            # expr_typ is ArrayType, expr is ArrayLiteral
            if type(expr_typ) is ArrayType:
                if expr_typ.size[:len(arrayele_typ.size)] != arrayele_typ.size:  # [[a,b],[3,4]] => dont know size of a,b => [a,b] size is [2,?]
                    raise TypeMismatchInExpression(self.arraylst[0])
                
                if expr_typ.eleType is None:
                    if type(expr) in [Id, CallExpr, ArrayLiteral]:
                        if self.inferType(expr, arrayele_typ, param):
                            expr_typ = arrayele_typ
                        else:
                            return None
                    else:
                        return None

                if expr_typ.size != arrayele_typ.size or expr_typ.eleType is not arrayele_typ.eleType:
                    raise TypeMismatchInExpression(self.arraylst[0])

        self.arraylst.pop()
        if arrayele_typ is ArrayType:
            return ArrayType([len(ast.value)] + arrayele_typ.size, arrayele_typ.eleType)
        return ArrayType([len(ast.value)], arrayele_typ)



class Symbol(ABC):
    pass

class VariableSymbol(Symbol):
    def __init__(self, name, type):
        self.name = name
        self.type = type

class FunctionSymbol(Symbol):
    def __init__(self, name, type, paramlst, body):
        self.name = name
        self.type = type
        self.paramlst = paramlst
        self.has_body = body