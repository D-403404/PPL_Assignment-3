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
        self.decl_lhs = None
        self.arraylst = []
        self.nobodylst = []
        self.visited_return = False
        self.curr_var_name = ''
        self.curr_func_name = ''
        self.looplst = []
        self.inferring_func = False
        self.ret_typ = None
        self.iodict = {
            'readNumber.func': FunctionSymbol('readNumber', NumberType(), {}, None), 
            'writeNumber.func': FunctionSymbol('writeNumber', VoidType(), {'anArg.var': VariableSymbol('anArg', NumberType())}, None), 
            'readBool.func': FunctionSymbol('readBool', BoolType(), {}, None), 
            'writeBool.func': FunctionSymbol('writeBool', VoidType(), {'anArg.var': VariableSymbol('anArg', BoolType())}, None), 
            'readString.func': FunctionSymbol('readString', StringType(), {}, None), 
            'writeString.func': FunctionSymbol('writeString', VoidType(), {'anArg.var': VariableSymbol('anArg', StringType())}, None), 
            }
        self.symlst = [self.iodict]  # array of dicts
        # o: [{'a': ('var', NumberType()), 'b': ('func', VoidType()), ...}, {}, {'a': ('var', BoolType())}, ...]    wrong
        # o: [{'a.var': VariableSymbol('a', NumberType()), 'b.func': FunctionSymbol('b', VoidType()), ...}, {}, {'a.var': VariableSymbol('a', BoolType())}, ...]    wrong
        # o: [{'a': VariableSymbol('a', NumberType()), 'b': FunctionSymbol('b', VoidType()), ...}, {}, {'a': VariableSymbol('a', BoolType())}, ...]    wrong

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
        print('check')
        self.visit(self.ast, self.symlst)
        # return ''

    def visitProgram(self, ast, param):
        print(ast)

        # symbol_table = [self.iodict]
        for decl in ast.decl:
            self.visit(decl, param)

        [scope[sym].print() for scope in param for sym in scope]

        print(self.nobodylst)

        if self.nobodylst != []:
            raise NoDefinition(self.nobodylst[0].name.name)
        
        if 'main.func' not in param[-1]:
            print('no main found')
            raise NoEntryPoint()
        if type(param[-1]['main.func'].type) is not VoidType or len(param[-1]['main.func'].paramlst) != 0:
            print('main not void or empty param')
            raise NoEntryPoint()
        
    def visitVarDecl(self, ast, param):
        print(ast)
        if ast.name.name + '.var' in param[0] or ast.name.name + '.func' in param[0]:
            raise Redeclared(Variable(), ast.name.name)
        
        self.curr_var_name = ast.name.name
        
        if ast.varInit is not None:
            rhs_typ = self.visit(ast.varInit, param)
            lhs_typ = ast.varType
            print(rhs_typ)
            print(lhs_typ)
            if lhs_typ is None and rhs_typ is None:
                raise TypeCannotBeInferred(ast)
            elif lhs_typ is None:
                param[0][ast.name.name + '.var'] = VariableSymbol(ast.name.name, rhs_typ)
            elif rhs_typ is None:
                rhs_check = self.checkType(ast, ast.varInit, rhs_typ, lhs_typ, param, 1)
                if rhs_check is None:
                    raise TypeCannotBeInferred(ast)
                rhs_typ = lhs_typ
                param[0][ast.name.name + '.var'] = VariableSymbol(ast.name.name, rhs_typ)
            elif type(lhs_typ) is not type(rhs_typ):
                raise TypeMismatchInStatement(ast)
            elif type(lhs_typ) is ArrayType:
                if rhs_typ.size[:len(lhs_typ.size)] != lhs_typ.size:  # [[a,b],[3,4]] => dont know size of a,b => [a,b] size is [2,?]
                    raise TypeMismatchInStatement(ast)
                print(4)
                
                if rhs_typ.eleType is None:
                    if self.checkType(ast, ast.rhs, rhs_typ, lhs_typ, param, 1) is not None:
                        rhs_typ = lhs_typ
                    else:
                        raise TypeCannotBeInferred(ast)

                print(rhs_typ.eleType)
                print(lhs_typ.eleType)
                if rhs_typ.size != lhs_typ.size or type(rhs_typ.eleType) is not type(lhs_typ.eleType):
                    raise TypeMismatchInStatement(ast)
                print(5)

                param[0][ast.name.name + '.var'] = VariableSymbol(ast.name.name, lhs_typ)
            else:
                param[0][ast.name.name + '.var'] = VariableSymbol(ast.name.name, lhs_typ)
        else:
            print(3)
            param[0][ast.name.name + '.var'] = VariableSymbol(ast.name.name, ast.varType)
            param[0][ast.name.name + '.var'].print()
        
        self.curr_var_name = ''
        self.arraylst = []

    def visitFuncDecl(self, ast, param):
        print(ast)
        print(f'inferring in FuncDecl of {ast}: {self.inferring_func}')

        # self.curr_func_name = ast.name.name

        global_scope = param[-1]   # global scope
        if not self.inferring_func and ast.name.name + '.var' in global_scope:
            raise Redeclared(Function(), ast.name.name)

        paramlst = [{}]
        for decl in ast.param:
            if decl.name.name + '.var' in paramlst[0]:
                raise Redeclared(Parameter(), decl.name.name)
            paramlst[0][decl.name.name + '.var'] = VariableSymbol(decl.name.name, decl.varType)
        function_scope = paramlst + param

        print(paramlst)
        print(function_scope)
        [dict[sym].print() for dict in function_scope for sym in dict]
        # print(global_scope[ast.name.name + '.func'])

        if ast.name.name + '.func' in global_scope:
            symbol = global_scope[ast.name.name + '.func']
            symbol.print()

            if not self.inferring_func and symbol.body is not None:
                raise Redeclared(Function(), ast.name.name)
            if not self.inferring_func and ast.body is None:    # redeclare function declaration
                raise Redeclared(Function(), ast.name.name)
            # symbol.body is None and ast.body is not None
            # process like ast.name not in scope, except check param and pop ast out of nobodylst
            if len(ast.param) != len(symbol.paramlst): # different # of params
                raise Redeclared(Function(), ast.name.name)
            for idx in range(len(paramlst[0])):
                if type(list(paramlst[0].values())[idx]) != type(list(symbol.paramlst.values())[idx]):    # different type of params
                    print('redeclared func_4')
                    raise Redeclared(Function(), ast.name.name)

            if not self.inferring_func:
                for idx in range(len(self.nobodylst)):
                    if self.nobodylst[idx].name.name == ast.name.name:
                        self.nobodylst.pop(idx)
                        break

            if ast.body is not None:
                print(1.2)
                self.curr_func_name = ast.name.name
                self.visit(ast.body, function_scope)
                # global_scope[ast.name.name + '.func'] = FunctionSymbol(ast.name.name, func_typ, paramlst[0], ast.body)
                # print(f'func_typ of {ast.body} is {func_typ}')
                if global_scope[ast.name.name + '.func'].type is None:
                    global_scope[ast.name.name + '.func'] = FunctionSymbol(ast.name.name, VoidType(), paramlst[0], ast.body)

        else:
            print('not in scope: ' + ast.name.name)
            self.curr_func_name = ast.name.name
            global_scope[ast.name.name + '.func'] = FunctionSymbol(ast.name.name, None, paramlst[0], ast.body)
            if ast.body is None:
                if not self.inferring_func:
                    self.nobodylst += [ast]
            else:
                self.visit(ast.body, function_scope)
                # global_scope[ast.name.name + '.func'] = FunctionSymbol(ast.name.name, func_typ, paramlst[0], ast.body)
                # print(f'func_typ of {ast.body} is {func_typ}')
                if global_scope[ast.name.name + '.func'].type is None:
                    global_scope[ast.name.name + '.func'] = FunctionSymbol(ast.name.name, VoidType(), paramlst[0], ast.body)
        
        print(param)

        self.visited_return = False

    def visitNumberType(self, ast, param):
        return NumberType()

    def visitBoolType(self, ast, param):
        return BoolType()

    def visitStringType(self, ast, param):
        return StringType()

    def visitArrayType(self, ast, param):
        return ArrayType(ast.size, ast.eleType)

    def inferType(self, ast, req_op_typ, param):
        print(f'inferring {ast} to {req_op_typ}')
        if type(ast) is Id:
            for scopedict in param:
                # res = self.lookup(ast.name + '.var', scopedict.keys(), lambda id: id)
                # if res is not None and type(scopedict[res + '.var']) is VariableSymbol:
                if ast.name + '.var' in scopedict:
                    print(1.1)
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
            global_scope = param[-1]
            if ast.name.name + '.func' in global_scope:
                symbol = global_scope[ast.name.name + '.func']
                global_scope[ast.name.name + '.func'] = FunctionSymbol(symbol.name, req_op_typ, symbol.paramlst, symbol.body)

                # revisit funcdecl to check body statements
                self.inferring_func = True
                curr_func = FuncDecl(Id(symbol.name), list(map(lambda param: VarDecl(Id(symbol.paramlst[param].name), symbol.paramlst[param].type, None, None), symbol.paramlst)), symbol.body)
                self.visit(curr_func, param)
                self.inferring_func = False
                return True

        return False

    def checkType(self, ast, op, op_typ, req_op_typ, param, typ = 0):
        print(f'checking {op} in {ast}')
        print(f'{op_typ} vs {req_op_typ}')
        if op_typ is None:  # infer type
            print('op_typ is None')
            if type(op) in [Id, CallExpr, ArrayLiteral]:
                inferred = self.inferType(op, req_op_typ, param)
                if inferred:
                    return req_op_typ
                return None
            return None

        if type(op_typ) is not type(req_op_typ):
            if typ == 0:
                raise TypeMismatchInExpression(ast)
            else:
                raise TypeMismatchInStatement(ast)

        print('all good')
        return req_op_typ

    def visitBinaryOp(self, ast, param):
        print(ast)

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
            right_typ = self.visit(ast.right, param)
            right_check = self.checkType(ast, ast.right, right_typ, NumberType(), param)
            if left_check is None or right_check is None:
                return None
            return NumberType()
        
        if ast.op in ['and', 'or']:
            left_check = self.checkType(ast, ast.left, left_typ, BoolType(), param)
            right_typ = self.visit(ast.right, param)
            right_check = self.checkType(ast, ast.right, right_typ, BoolType(), param)
            if left_check is None or right_check is None:
                return None
            return BoolType()
        
        if ast.op == '...':
            left_check = self.checkType(ast, ast.left, left_typ, StringType(), param)
            right_typ = self.visit(ast.right, param)
            right_check = self.checkType(ast, ast.right, right_typ, StringType(), param)
            if left_check is None or right_check is None:
                return None
            return StringType()
        
        if ast.op in ['=', '!=', '<', '>', '<=', '>=', '==']:
            if ast.op == '==':
                left_check = self.checkType(ast, ast.left, left_typ, StringType(), param)
                right_typ = self.visit(ast.right, param)
                right_check = self.checkType(ast, ast.right, right_typ, StringType(), param)
            else:
                left_check = self.checkType(ast, ast.left, left_typ, NumberType(), param)
                right_typ = self.visit(ast.right, param)
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
        print(ast)

        if ast.name.name == self.curr_var_name:
            raise TypeMismatchInExpression(ast)

        for scope in param[:-1]:
            if ast.name.name + '.var' in scope:  # a var with the same name as func
                raise TypeMismatchInExpression(ast)

        if ast.name.name + '.func' not in param[-1]:
            raise Undeclared(Function(), ast.name.name)
        
        symbol = param[-1][ast.name.name + '.func']
        print(symbol)
        symbol.print()

        # if symbol.type is None:
        
        if type(symbol.type) is VoidType:
            raise TypeMismatchInExpression(ast)
        if len(ast.args) != len(symbol.paramlst):
            raise TypeMismatchInExpression(ast)
        
        print(1)
        
        for idx in range(len(ast.args)):
            arg_typ = self.visit(ast.args[idx], param)
            print(arg_typ)
            print(ast.args[idx])
            symbol.paramlst[list(symbol.paramlst.keys())[idx]].print()

            arg_check = self.checkType(ast, ast.args[idx], arg_typ, symbol.paramlst[list(symbol.paramlst.keys())[idx]].type, param)
            print(2)
            if arg_check is None:
                return None
            # arg_typ = symbol.paramlst[list(symbol.paramlst.keys())[idx]]

            req_op_typ = symbol.paramlst[list(symbol.paramlst.keys())[idx]].type
            if type(arg_typ) is ArrayType:
                if arg_typ.size[:len(req_op_typ.size)] != req_op_typ.size:  # [[a,b],[3,4]] => dont know size of a,b => [a,b] size is [2,?]
                    raise TypeMismatchInExpression(ast)
                
                if arg_typ.eleType is None:
                    if type(ast.args[idx]) in [Id, CallExpr, ArrayLiteral]:
                        if self.inferType(ast.args[idx], req_op_typ, param):
                            arg_typ = symbol.paramlst[list(symbol.paramlst.keys())[idx]].type
                        else:
                            raise TypeCannotBeInferred(ast)
                    else:
                        raise TypeCannotBeInferred(ast)

                if arg_typ.size != symbol.paramlst[list(symbol.paramlst.keys())[idx]].type.size or type(arg_typ.eleType) is not type(symbol.paramlst[list(symbol.paramlst.keys())[idx]].type.eleType):
                    raise TypeMismatchInExpression(ast)
                
        symbol.print()
        return symbol.type

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
        if ast.name == self.curr_var_name:
            raise Undeclared(Identifier(), ast.name)

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
        print('haha')
        if len(ast.idx) > len(arrayId_typ.size):
            raise TypeMismatchInExpression(ast)
        print('hihi')
        for idx in ast.idx:
            idx_typ = self.visit(idx, param)
            idx_check = self.checkType(ast, idx, idx_typ, NumberType(), param)
            if idx_check is None:
                return None
            
        if len(ast.idx) == len(arrayId_typ.size):
            return arrayId_typ.eleType
        return ArrayType(arrayId_typ.size[len(ast.idx):], arrayId_typ.eleType)

    def visitBlock(self, ast, param):
        block_scope = [{}] + param
        for stmt in ast.stmt:
            self.visit(stmt, block_scope)
        
        self.arraylst = []
        self.visited_return = False

    def visitIf(self, ast, param):
        # self.visited_return = False
        expr_typ = self.visit(ast.expr, param)
        expr_check = self.checkType(ast, ast.expr, expr_typ, BoolType(), param, 1)
        if expr_check is None:
            raise TypeCannotBeInferred(ast)
        self.visited_return = False
        self.visit(ast.thenStmt, param)

        for stmt in ast.elifStmt:
            self.visited_return = False
            expr_typ = self.visit(stmt[0], param)
            expr_check = self.checkType(ast, stmt[0], expr_typ, BoolType(), param, 1)
            if expr_check is None:
                raise TypeCannotBeInferred(ast)
            self.visit(stmt[1], param)

        self.visited_return = False
        if ast.elseStmt is not None:
            self.visit(ast.elseStmt, param)

        self.arraylst = []

    def visitFor(self, ast, param):
        # self.visited_return = False
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
        print(ast)

        if self.visited_return is True:
            return
        self.visited_return = True
        
        global_scope = param[-1]
        symbol = global_scope[self.curr_func_name + '.func']

        if ast.expr is None:
            if symbol.type is not None and type(symbol.type) is not VoidType:
                raise TypeMismatchInStatement(ast)
            
            global_scope[self.curr_func_name + '.func'] = FunctionSymbol(symbol.name, VoidType(), symbol.paramlst, symbol.body)
            return VoidType()
        
        ret_typ = self.visit(ast.expr, param)
        print(f'ret_typ of {self.curr_func_name}: {ret_typ}')
        print(f'current ret_typ of {self.curr_func_name}: {symbol.type}')

        if symbol.type is None:
            if ret_typ is None:
                raise TypeCannotBeInferred(ast)
            # infer type of function
            global_scope[self.curr_func_name + '.func'] = FunctionSymbol(symbol.name, ret_typ, symbol.paramlst, symbol.body)
            print((global_scope[self.curr_func_name + '.func'].type))

        # function has a type
        else:
            if type(symbol.type) is VoidType:
                raise TypeMismatchInStatement(ast)
            
            ret_check = self.checkType(ast, ast.expr, ret_typ, symbol.type, param, 1)
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

                if ret_typ.size != symbol.type.size or type(ret_typ.eleType) is not type(symbol.type.eleType):
                    raise TypeMismatchInStatement(ast)
            
        self.arraylst = []

    def visitAssign(self, ast, param):
        print(ast)
        rhs_typ = self.visit(ast.rhs, param)
        lhs_typ = self.visit(ast.lhs, param)

        print(rhs_typ)
        print(lhs_typ)

        if lhs_typ is None and rhs_typ is None:
            raise TypeCannotBeInferred(ast)
        elif lhs_typ is None:
            if self.checkType(ast, ast.lhs, lhs_typ, rhs_typ, param, 1) is None:
                raise TypeCannotBeInferred(ast)
        elif rhs_typ is None:
            if self.checkType(ast, ast.rhs, rhs_typ, lhs_typ, param, 1) is None:
                raise TypeCannotBeInferred(ast)
        elif type(lhs_typ) is VoidType or type(rhs_typ) is VoidType:
            raise TypeMismatchInStatement(ast)
        elif type(lhs_typ) is not type(rhs_typ):
            raise TypeMismatchInStatement(ast)
        elif type(lhs_typ) is ArrayType:
                if rhs_typ.size[:len(lhs_typ.size)] != lhs_typ.size:  # [[a,b],[3,4]] => dont know size of a,b => [a,b] size is [2,?]
                    raise TypeMismatchInStatement(ast)
                
                if rhs_typ.eleType is None:
                    if self.checkType(ast, ast.rhs, rhs_typ, lhs_typ, param, 1) is not None:
                        rhs_typ = lhs_typ
                    else:
                        raise TypeCannotBeInferred(ast)

                if rhs_typ.size != lhs_typ.size or type(rhs_typ.eleType) is not type(lhs_typ.eleType):
                    raise TypeMismatchInStatement(ast)

    def visitCallStmt(self, ast, param):
        print(ast)

        for scope in param[:-1]:
            if ast.name.name + '.var' in scope:  # a var with the same name as func
                raise TypeMismatchInStatement(ast)

        if ast.name.name + '.func' not in param[-1]:
            raise Undeclared(Function(), ast.name.name)
        
        symbol = param[-1][ast.name.name + '.func']
        if symbol.type is not None and type(symbol.type) is not VoidType:
            print('not void type')
            raise TypeMismatchInStatement(ast)
        if len(ast.args) != len(symbol.paramlst):
            raise TypeMismatchInStatement(ast)
        
        for idx in range(len(ast.args)):
            arg_typ = self.visit(ast.args[idx], param)
            arg_check = self.checkType(ast, ast.args[idx], arg_typ, symbol.paramlst[list(symbol.paramlst.keys())[idx]].type, param, 1)
            if arg_check is None:
                return None
            # arg_typ = symbol.paramlst[list(symbol.paramlst.keys())[idx]]
            # print(1)

            req_op_typ = symbol.paramlst[list(symbol.paramlst.keys())[idx]].type
            if type(arg_typ) is ArrayType:
                if arg_typ.size[:len(req_op_typ.size)] != req_op_typ.size:  # [[a,b],[3,4]] => dont know size of a,b => [a,b] size is [2,?]
                    raise TypeMismatchInStatement(ast)
                
                if arg_typ.eleType is None:
                    if type(ast.args[idx]) in [Id, CallExpr, ArrayLiteral]:
                        if self.inferType(ast.args[idx], req_op_typ, param):
                            arg_typ = symbol.paramlst[list(symbol.paramlst.keys())[idx]].type
                        else:
                            raise TypeCannotBeInferred(ast)
                    else:
                        raise TypeCannotBeInferred(ast)

                if arg_typ.size != symbol.paramlst[list(symbol.paramlst.keys())[idx]].type.size or type(arg_typ.eleType) is not type(symbol.paramlst[list(symbol.paramlst.keys())[idx]].type.eleType):
                    raise TypeMismatchInStatement(ast)
                
        if symbol.type is None:
            if not self.inferType(ast, VoidType(), param):
                raise TypeCannotBeInferred(ast)
                
        # param[-1][ast.name.name + '.func'] = FunctionSymbol()
        self.arraylst = []

    def visitNumberLiteral(self, ast, param):
        print(ast)
        return NumberType()

    def visitBooleanLiteral(self, ast, param):
        print(ast)
        return BoolType()

    def visitStringLiteral(self, ast, param):
        print(ast)
        return StringType()

    # def checkArrayLiteral(self, ast, root_ast, param):  # to call recursion



    def visitArrayLiteral(self, ast, param):
        # array literal is not empty
        # param[0]: scope list              wrong
        # param[1]: array element type in VarDecl statement     wrong
        print(ast)
        
        # if ast not in self.arraylst:
        print(f'push {ast}')
        self.arraylst += [ast]
        print(f'current arraylst: {[(str(obj)) for obj in self.arraylst]}')

        arrayele_typ = None
        for expr in ast.value:
            arrayele_typ = self.visit(expr, param)
            if arrayele_typ is not None:
                print(f'arrayele_typ: {arrayele_typ} of {expr} in {ast}')
                break

        if arrayele_typ is None:
            return None

        for expr in ast.value:
            expr_typ = self.visit(expr, param)
            print(f'expr_typ: {expr_typ} of {expr} in {ast}')
            expr_check = self.checkType(self.arraylst[0], expr, expr_typ, arrayele_typ, param)
            if expr_check is None:
                return None
            # expr_typ = arrayele_typ

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

                if expr_typ.size != arrayele_typ.size or type(expr_typ.eleType) is not type(arrayele_typ.eleType):
                    raise TypeMismatchInExpression(self.arraylst[0])

        popped = self.arraylst.pop()
        print(f'pop {popped}')
        if type(arrayele_typ) is ArrayType:
            print(f'returning arrayele_typ: {arrayele_typ}')
            return ArrayType([float(len(ast.value))] + arrayele_typ.size, arrayele_typ.eleType)
        return ArrayType([float(len(ast.value))], arrayele_typ)



class Symbol(ABC):
    pass

class VariableSymbol(Symbol):
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def print(self):
        print(f'VariableSymbol: {self.name}, {self.type}')

    def get(self):
        return f'VariableSymbol: {self.name}, {self.type}'

class FunctionSymbol(Symbol):
    def __init__(self, name, type, paramlst, body):
        self.name = name
        self.type = type
        self.paramlst = paramlst
        self.body = body

    def print(self):
        print(f'FunctionSymbol: {self.name}, {self.type}, {[self.paramlst[param].get() for param in self.paramlst]}, {self.body}')