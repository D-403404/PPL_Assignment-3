# Nguyễn Thành Đạt - 2152506

from ZCodeVisitor import ZCodeVisitor
from ZCodeParser import ZCodeParser
from AST import *

# from main.zcode.utils.AST import *

class ASTGeneration(ZCodeVisitor):

    "program: declarationLst EOF;"
    def visitProgram(self, ctx: ZCodeParser.ProgramContext):
        return Program(self.visit(ctx.declarationLst()))
    
    "declarationLst: SB_NEWLINE* stmt_declaration declarationLst | SB_NEWLINE* stmt_declaration;"
    def visitDeclarationLst(self, ctx: ZCodeParser.DeclarationLstContext):
        if ctx.declarationLst():
            return [self.visit(ctx.stmt_declaration())] + self.visit(ctx.declarationLst())
        else:
            return [self.visit(ctx.stmt_declaration())]
    


    "arrayElement: IDENTIFIER expr_element | stmt_func_call expr_element;"
    def visitArrayElement(self, ctx: ZCodeParser.ArrayElementContext):
        if ctx.IDENTIFIER():
            return ArrayCell(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.expr_element()))
        elif ctx.expr_func_call():
            return ArrayCell(self.visit(ctx.expr_func_call()), self.visit(ctx.expr_element()))
    
    "expr_element: SB_LEFTSQUARE op_index SB_RIGHTSQUARE;"
    def visitExpr_element(self, ctx: ZCodeParser.Expr_elementContext):
        return self.visit(ctx.op_index())
    
    "op_index: expr SB_COMMA op_index | expr;"
    def visitOp_index(self, ctx: ZCodeParser.Op_indexContext):
        if ctx.op_index():
            return [self.visit(ctx.expr())] + self.visit(ctx.op_index())
        else:
            return [self.visit(ctx.expr())]
    

    
    "op_unary_index: arrayElement;"
    def visitOp_unary_index(self, ctx: ZCodeParser.Op_unary_indexContext):
        return self.visit(ctx.arrayElement())
    
    "op_unary_sign: OP_MINUS;"
    def visitOp_unary_sign(self, ctx: ZCodeParser.Op_unary_signContext):
        return ctx.OP_MINUS().getText()
    
    "op_unary_logical: OP_NOT;"
    def visitOp_unary_logical(self, ctx: ZCodeParser.Op_unary_logicalContext):
        return ctx.OP_NOT().getText()
    
    "op_binary_multiplying: OP_MULT | OP_DIV | OP_MOD;"
    def visitOp_binary_multiplying(self, ctx: ZCodeParser.Op_binary_multiplyingContext):
        if ctx.OP_MULT():
            return ctx.OP_MULT().getText()
        elif ctx.OP_DIV():
            return ctx.OP_DIV().getText()
        else:
            return ctx.OP_MOD().getText()
    
    "op_binary_adding: OP_PLUS | OP_MINUS;"
    def visitOp_binary_adding(self, ctx: ZCodeParser.Op_binary_addingContext):
        if ctx.OP_PLUS():
            return ctx.OP_PLUS().getText()
        else:
            return ctx.OP_MINUS().getText()
    
    "op_binary_logical: OP_AND | OP_OR;"
    def visitOp_binary_logical(self, ctx: ZCodeParser.Op_binary_logicalContext):
        if ctx.OP_AND():
            return ctx.OP_AND().getText()
        else:
            return ctx.OP_OR().getText()
    
    """
    op_binary_relational:
        OP_EQUAL_NUM
        | OP_EQUAL_STR
        | OP_UNEQUAL
        | OP_LESS
        | OP_MORE
        | OP_LESSOREQUAL
        | OP_MOREOREQUAL;
    """
    def visitOp_binary_relational(self, ctx: ZCodeParser.Op_binary_relationalContext):
        if ctx.OP_EQUAL_NUM():
            return ctx.OP_EQUAL_NUM().getText()
        elif ctx.OP_EQUAL_STR():
            return ctx.OP_EQUAL_STR().getText()
        elif ctx.OP_UNEQUAL():
            return ctx.OP_UNEQUAL().getText()
        elif ctx.OP_LESS():
            return ctx.OP_LESS().getText()
        elif ctx.OP_MORE():
            return ctx.OP_MORE().getText()
        elif ctx.OP_LESSOREQUAL():
            return ctx.OP_LESSOREQUAL().getText()
        else:
            return ctx.OP_MOREOREQUAL().getText()
    
    "op_binary_string: OP_CONCAT;"
    def visitOp_binary_string(self, ctx: ZCodeParser.Op_binary_stringContext):
        return ctx.OP_CONCAT().getText()
    


    "expr: expr_string;"
    def visitExpr(self, ctx: ZCodeParser.ExprContext):
        return self.visit(ctx.expr_string())
    
    "expr_string: expr_relational op_binary_string expr_relational | expr_relational;"
    def visitExpr_string(self, ctx: ZCodeParser.Expr_stringContext):
        if ctx.op_binary_string():
            return BinaryOp(self.visit(ctx.op_binary_string()), self.visit(ctx.expr_relational(0)), self.visit(ctx.expr_relational(1)))
        else:
            return self.visit(ctx.expr_relational(0))
    
    "expr_relational: expr_logical op_binary_relational expr_logical | expr_logical;"
    def visitExpr_relational(self, ctx: ZCodeParser.Expr_relationalContext):
        if ctx.op_binary_relational():
            return BinaryOp(self.visit(ctx.op_binary_relational()), self.visit(ctx.expr_logical(0)), self.visit(ctx.expr_logical(1)))
        else:
            return self.visit(ctx.expr_logical(0))
    
    "expr_logical: expr_logical op_binary_logical expr_adding | expr_adding;"
    def visitExpr_logical(self, ctx: ZCodeParser.Expr_logicalContext):
        if ctx.op_binary_logical():
            return BinaryOp(self.visit(ctx.op_binary_logical()), self.visit(ctx.expr_logical()), self.visit(ctx.expr_adding()))
        else:
            return self.visit(ctx.expr_adding())
    
    "expr_adding: expr_adding op_binary_adding expr_multiplying | expr_multiplying;"
    def visitExpr_adding(self, ctx: ZCodeParser.Expr_addingContext):
        if ctx.op_binary_adding():
            return BinaryOp(self.visit(ctx.op_binary_adding()), self.visit(ctx.expr_adding()), self.visit(ctx.expr_multiplying()))
        else:
            return self.visit(ctx.expr_multiplying())
    
    "expr_multiplying: expr_multiplying op_binary_multiplying expr_not | expr_not;"
    def visitExpr_multiplying(self, ctx: ZCodeParser.Expr_multiplyingContext):
        if ctx.op_binary_multiplying():
            return BinaryOp(self.visit(ctx.op_binary_multiplying()), self.visit(ctx.expr_multiplying()), self.visit(ctx.expr_not()))
        else:
            return self.visit(ctx.expr_not())
    
    "expr_not: op_unary_logical expr_not | expr_sign;"
    def visitExpr_not(self, ctx: ZCodeParser.Expr_notContext):
        if ctx.op_unary_logical():
            return UnaryOp(self.visit(ctx.op_unary_logical()), self.visit(ctx.expr_not()))
        else:
            return self.visit(ctx.expr_sign())
    
    "expr_sign: op_unary_sign expr_sign | expr_index;"
    def visitExpr_sign(self, ctx: ZCodeParser.Expr_signContext):
        if ctx.op_unary_sign():
            return UnaryOp(self.visit(ctx.op_unary_sign()), self.visit(ctx.expr_sign()))
        else:
            return self.visit(ctx.expr_index())
    
    "expr_index: op_unary_index | operand;"
    def visitExpr_index(self, ctx: ZCodeParser.Expr_indexContext):
        if ctx.op_unary_index():
            return self.visit(ctx.op_unary_index())
        else:
            return self.visit(ctx.operand())
    
    "operand: IDENTIFIER | NUMBER | BOOL | STRING | arrayValue | expr_func_call | SB_LEFTBRACKET expr SB_RIGHTBRACKET;"
    def visitOperand(self, ctx: ZCodeParser.OperandContext):
        if ctx.IDENTIFIER():
            return Id(ctx.IDENTIFIER().getText())
        elif ctx.NUMBER():
            return NumberLiteral(float(ctx.NUMBER().getText()))
        elif ctx.BOOL():
            return BooleanLiteral(ctx.BOOL().getText() == 'true')
        elif ctx.STRING():
            return StringLiteral(ctx.STRING().getText())
        elif ctx.arrayValue():
            return self.visit(ctx.arrayValue())
        elif ctx.expr_func_call():
            return self.visit(ctx.expr_func_call())
        else:
            return self.visit(ctx.expr())
    
    "expr_func_call: IDENTIFIER SB_LEFTBRACKET argLst SB_RIGHTBRACKET;"
    def visitExpr_func_call(self, ctx: ZCodeParser.Expr_func_callContext):
        return CallExpr(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.argLst()))
    


    "kw_type_explicit: KW_NUMBER | KW_BOOL | KW_STRING;"
    def visitKw_type_explicit(self, ctx: ZCodeParser.Kw_type_explicitContext):
        if ctx.KW_NUMBER():
            return NumberType()
        elif ctx.KW_BOOL():
            return BoolType()
        else:
            return StringType()
    
    "kw_type: kw_type_explicit | KW_VAR | KW_DYNAMIC;"
    def visitKw_type(self, ctx: ZCodeParser.Kw_typeContext):
        if ctx.kw_type_explicit():
            return self.visit(ctx.kw_type_explicit())
        elif ctx.KW_VAR():
            return ctx.KW_VAR().getText()
        else:
            return ctx.KW_DYNAMIC().getText()
    
    """
    stmt_declaration: 
        stmt_var_declaration SB_NEWLINE+ 
        | stmt_array_declaration SB_NEWLINE+ 
        | stmt_func_declaration SB_NEWLINE+
        ;
    """
    def visitStmt_declaration(self, ctx: ZCodeParser.Stmt_declarationContext):
        if ctx.stmt_var_declaration():
            return self.visit(ctx.stmt_var_declaration())
        elif ctx.stmt_array_declaration():
            return self.visit(ctx.stmt_array_declaration())
        else:
            return self.visit(ctx.stmt_func_declaration())
    


    "stmt_var_declaration: stmt_var_declaration_explicit | stmt_var_declaration_dynamic | stmt_var_declaration_var;"
    def visitStmt_var_declaration(self, ctx: ZCodeParser.Stmt_var_declarationContext):
        if ctx.stmt_var_declaration_explicit():
            return self.visit(ctx.stmt_var_declaration_explicit())
        elif ctx.stmt_var_declaration_dynamic():
            return self.visit(ctx.stmt_var_declaration_dynamic())
        else:
            return self.visit(ctx.stmt_var_declaration_var())
    
    "stmt_var_declaration_explicit: kw_type_explicit IDENTIFIER value_init | kw_type_explicit IDENTIFIER;"
    def visitStmt_var_declaration_explicit(self, ctx: ZCodeParser.Stmt_var_declaration_explicitContext):
        if ctx.value_init():
            return VarDecl(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.kw_type_explicit()), None, self.visit(ctx.value_init()))
        else:
            return VarDecl(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.kw_type_explicit()), None, None)
    
    "stmt_var_declaration_dynamic: KW_DYNAMIC IDENTIFIER value_init | KW_DYNAMIC IDENTIFIER;"
    def visitStmt_var_declaration_dynamic(self, ctx: ZCodeParser.Stmt_var_declaration_dynamicContext):
        if ctx.value_init():
            return VarDecl(Id(ctx.IDENTIFIER().getText()), None, ctx.KW_DYNAMIC().getText(), self.visit(ctx.value_init()))
        else:
            return VarDecl(Id(ctx.IDENTIFIER().getText()), None, ctx.KW_DYNAMIC().getText(), None)
    
    "stmt_var_declaration_var: KW_VAR IDENTIFIER value_init;"
    def visitStmt_var_declaration_var(self, ctx: ZCodeParser.Stmt_var_declaration_varContext):
        return VarDecl(Id(ctx.IDENTIFIER().getText()), None, ctx.KW_VAR().getText(), self.visit(ctx.value_init()))
    
    "value_init: OP_ASSIGN expr;"
    def visitValue_init(self, ctx: ZCodeParser.Value_initContext):
        return self.visit(ctx.expr())
    


    "stmt_array_declaration: kw_type_explicit arrayId array_init | kw_type_explicit arrayId;"
    def visitStmt_array_declaration(self, ctx: ZCodeParser.Stmt_array_declarationContext):
        array_id = self.visit(ctx.arrayId())
        if ctx.array_init():
            return VarDecl(array_id[0], ArrayType(array_id[1], self.visit(ctx.kw_type_explicit())), None, self.visit(ctx.array_init()))
        else:
            return VarDecl(array_id[0], ArrayType(array_id[1], self.visit(ctx.kw_type_explicit())), None, None)
    
    "arrayId: IDENTIFIER SB_LEFTSQUARE arrayDim SB_RIGHTSQUARE;"
    def visitArrayId(self, ctx: ZCodeParser.ArrayIdContext):
        return Id(ctx.IDENTIFIER().getText()), self.visit(ctx.arrayDim()) 
    
    "arrayDim: NUMBER SB_COMMA arrayDim | NUMBER;"
    def visitArrayDim(self, ctx: ZCodeParser.ArrayDimContext):
        if ctx.arrayDim():
            return [float(ctx.NUMBER().getText())] + self.visit(ctx.arrayDim())
        else:
            return [float(ctx.NUMBER().getText())]
    
    "array_init: value_init;"
    def visitArray_init(self, ctx: ZCodeParser.Array_initContext):
        return self.visit(ctx.value_init())
    
    "arrayValue: SB_LEFTSQUARE exprLst SB_RIGHTSQUARE;"
    def visitArrayValue(self, ctx: ZCodeParser.ArrayValueContext):
        return ArrayLiteral(self.visit(ctx.exprLst()))
    
    "exprLst: expr SB_COMMA exprLst | expr;"
    def visitExprLst(self, ctx: ZCodeParser.ExprLstContext):
        if ctx.exprLst():
            return [self.visit(ctx.expr())] + self.visit(ctx.exprLst())
        else:
            return [self.visit(ctx.expr())]
    


    """
    stmt_func_declaration:
	    KW_FUNC IDENTIFIER SB_LEFTBRACKET paramLst SB_RIGHTBRACKET SB_NEWLINE* func_body;
    """
    def visitStmt_func_declaration(self, ctx: ZCodeParser.Stmt_func_declarationContext):
        return FuncDecl(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.paramLst()), self.visit(ctx.func_body()))
    
    "paramLst: param paramLstTail | ;"
    def visitParamLst(self, ctx: ZCodeParser.ParamLstContext):
        if ctx.paramLstTail():
            return [self.visit(ctx.param())] + self.visit(ctx.paramLstTail())
        else:
            return []
    
    "paramLstTail: SB_COMMA param paramLstTail | ;"
    def visitParamLstTail(self, ctx: ZCodeParser.ParamLstTailContext):
        if ctx.paramLstTail():
            return [self.visit(ctx.param())] + self.visit(ctx.paramLstTail())
        else:
            return []
    
    "param: kw_type_explicit IDENTIFIER | kw_type_explicit arrayId;"
    def visitParam(self, ctx: ZCodeParser.ParamContext):
        if not ctx.arrayId():
            return VarDecl(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.kw_type_explicit()), None, None)
        else:
            array_id = self.visit(ctx.arrayId())
            return VarDecl(array_id[0], ArrayType(array_id[1], self.visit(ctx.kw_type_explicit())), None, None)
    
    "func_body: stmt_return | stmt_block | ;"
    def visitFunc_body(self, ctx: ZCodeParser.Func_bodyContext):
        if ctx.stmt_return():
            return self.visit(ctx.stmt_return())
        elif ctx.stmt_block():
            return self.visit(ctx.stmt_block())
        else:
            return None
    


    """
    statement:
        stmt_var_declaration SB_NEWLINE+ 
        | stmt_array_declaration SB_NEWLINE+
        | stmt_assignment SB_NEWLINE+
        | stmt_if							// No newline to prevent double newline from the stmt and its body
        | stmt_for							// No newline to prevent double newline from the stmt and its body
        | stmt_break SB_NEWLINE+
        | stmt_continue SB_NEWLINE+
        | stmt_return SB_NEWLINE+
        | stmt_func_call SB_NEWLINE+
        | stmt_block SB_NEWLINE+
        ;
    """
    def visitStatement(self, ctx: ZCodeParser.StatementContext):
        if ctx.stmt_var_declaration():
            return self.visit(ctx.stmt_var_declaration())
        elif ctx.stmt_array_declaration():
            return self.visit(ctx.stmt_array_declaration())
        elif ctx.stmt_assignment():
            return self.visit(ctx.stmt_assignment())
        elif ctx.stmt_if():
            return self.visit(ctx.stmt_if())
        elif ctx.stmt_for():
            return self.visit(ctx.stmt_for())
        elif ctx.stmt_break():
            return self.visit(ctx.stmt_break())
        elif ctx.stmt_continue():
            return self.visit(ctx.stmt_continue())
        elif ctx.stmt_return():
            return self.visit(ctx.stmt_return())
        elif ctx.stmt_func_call():
            return self.visit(ctx.stmt_func_call())
        else:
            return self.visit(ctx.stmt_block())
    


    "stmt_assignment: assignment_lhs value_init;"
    def visitStmt_assignment(self, ctx: ZCodeParser.Stmt_assignmentContext):
        return Assign(self.visit(ctx.assignment_lhs()), self.visit(ctx.value_init()))
    
    "assignment_lhs: IDENTIFIER | arrayElement;"
    def visitAssignment_lhs(self, ctx: ZCodeParser.Assignment_lhsContext):
        if ctx.IDENTIFIER():
            return Id(ctx.IDENTIFIER().getText())
        else:
            return self.visit(ctx.arrayElement())



    """
    if_statement:
	    KW_IF SB_LEFTBRACKET expr SB_RIGHTBRACKET SB_NEWLINE* statement;
    """
    def visitIf_statement(self, ctx: ZCodeParser.If_statementContext):
        return self.visit(ctx.expr()), self.visit(ctx.statement())
    
    """
    elif_statement:
	    KW_ELIF SB_LEFTBRACKET expr SB_RIGHTBRACKET SB_NEWLINE* statement;
    """
    def visitElif_statement(self, ctx: ZCodeParser.Elif_statementContext):
        return self.visit(ctx.expr()), self.visit(ctx.statement())
    
    "else_statement: KW_ELSE SB_NEWLINE* statement | ;"
    def visitElse_statement(self, ctx: ZCodeParser.Else_statementContext):
        if ctx.statement():
            return self.visit(ctx.statement())
        else:
            return None
    
    """
    stmt_if:
	    if_statement SB_NEWLINE* elifLst else_statement;
    """
    def visitStmt_if(self, ctx: ZCodeParser.Stmt_ifContext):
        if_stmt = self.visit(ctx.if_statement())
        return If(if_stmt[0], if_stmt[1], self.visit(ctx.elifLst()), self.visit(ctx.else_statement()))
    
    "elifLst: elif_statement SB_NEWLINE* elifLst | ;"
    def visitElifLst(self, ctx: ZCodeParser.ElifLstContext):
        if ctx.elifLst():
            return [self.visit(ctx.elif_statement())] + self.visit(ctx.elifLst())
        else:
            return []
    


    """
    stmt_for:
        KW_FOR IDENTIFIER KW_UNTIL expr KW_BY expr SB_NEWLINE*
            statement;
    """
    def visitStmt_for(self, ctx: ZCodeParser.Stmt_forContext):
        return For(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.expr(0)), self.visit(ctx.expr(1)), self.visit(ctx.statement()))
    
    
    
    "stmt_break: KW_BREAK;"
    def visitStmt_break(self, ctx: ZCodeParser.Stmt_breakContext):
        return Break()
    
    "stmt_continue: KW_CONTINUE;"
    def visitStmt_continue(self, ctx: ZCodeParser.Stmt_continueContext):
        return Continue()
    
    "stmt_return: KW_RETURN expr | KW_RETURN;"
    def visitStmt_return(self, ctx: ZCodeParser.Stmt_returnContext):
        if ctx.expr():
            return Return(self.visit(ctx.expr()))
        else:
            return Return(None)
    
    
    
    """
    stmt_func_call:
	    IDENTIFIER SB_LEFTBRACKET argLst SB_RIGHTBRACKET;
    """
    def visitStmt_func_call(self, ctx: ZCodeParser.Stmt_func_callContext):
        return CallStmt(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.argLst()))
    
    "argLst: expr argLstTail | ;"
    def visitArgLst(self, ctx: ZCodeParser.ArgLstContext):
        if ctx.argLstTail():
            return [self.visit(ctx.expr())] + self.visit(ctx.argLstTail())
        else:
            return []
    
    "argLstTail: SB_COMMA expr argLstTail | ;"
    def visitArgLstTail(self, ctx: ZCodeParser.ArgLstTailContext):
        if ctx.argLstTail():
            return [self.visit(ctx.expr())] + self.visit(ctx.argLstTail())
        else:
            return []
    


    "stmt_block: KW_BEGIN SB_NEWLINE+ statementLst KW_END;"
    def visitStmt_block(self, ctx: ZCodeParser.Stmt_blockContext):
        return Block(self.visit(ctx.statementLst()))
    
    "statementLst: statement statementLst | ;"
    def visitStatementLst(self, ctx: ZCodeParser.StatementLstContext):
        if ctx.statementLst():
            return [self.visit(ctx.statement())] + self.visit(ctx.statementLst())
        else:
            return []