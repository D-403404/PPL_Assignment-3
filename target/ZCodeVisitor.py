# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ZCodeParser import ZCodeParser
else:
    from ZCodeParser import ZCodeParser

# This class defines a complete generic visitor for a parse tree produced by ZCodeParser.

class ZCodeVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ZCodeParser#program.
    def visitProgram(self, ctx:ZCodeParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#declarationLst.
    def visitDeclarationLst(self, ctx:ZCodeParser.DeclarationLstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#arrayElement.
    def visitArrayElement(self, ctx:ZCodeParser.ArrayElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr_element.
    def visitExpr_element(self, ctx:ZCodeParser.Expr_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#op_index.
    def visitOp_index(self, ctx:ZCodeParser.Op_indexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#op_unary_index.
    def visitOp_unary_index(self, ctx:ZCodeParser.Op_unary_indexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#op_unary_sign.
    def visitOp_unary_sign(self, ctx:ZCodeParser.Op_unary_signContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#op_unary_logical.
    def visitOp_unary_logical(self, ctx:ZCodeParser.Op_unary_logicalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#op_binary_multiplying.
    def visitOp_binary_multiplying(self, ctx:ZCodeParser.Op_binary_multiplyingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#op_binary_adding.
    def visitOp_binary_adding(self, ctx:ZCodeParser.Op_binary_addingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#op_binary_logical.
    def visitOp_binary_logical(self, ctx:ZCodeParser.Op_binary_logicalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#op_binary_relational.
    def visitOp_binary_relational(self, ctx:ZCodeParser.Op_binary_relationalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#op_binary_string.
    def visitOp_binary_string(self, ctx:ZCodeParser.Op_binary_stringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr.
    def visitExpr(self, ctx:ZCodeParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr_string.
    def visitExpr_string(self, ctx:ZCodeParser.Expr_stringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr_relational.
    def visitExpr_relational(self, ctx:ZCodeParser.Expr_relationalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr_logical.
    def visitExpr_logical(self, ctx:ZCodeParser.Expr_logicalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr_adding.
    def visitExpr_adding(self, ctx:ZCodeParser.Expr_addingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr_multiplying.
    def visitExpr_multiplying(self, ctx:ZCodeParser.Expr_multiplyingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr_not.
    def visitExpr_not(self, ctx:ZCodeParser.Expr_notContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr_sign.
    def visitExpr_sign(self, ctx:ZCodeParser.Expr_signContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr_index.
    def visitExpr_index(self, ctx:ZCodeParser.Expr_indexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#operand.
    def visitOperand(self, ctx:ZCodeParser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr_func_call.
    def visitExpr_func_call(self, ctx:ZCodeParser.Expr_func_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#kw_type_explicit.
    def visitKw_type_explicit(self, ctx:ZCodeParser.Kw_type_explicitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#kw_type.
    def visitKw_type(self, ctx:ZCodeParser.Kw_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#stmt_declaration.
    def visitStmt_declaration(self, ctx:ZCodeParser.Stmt_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#stmt_var_declaration.
    def visitStmt_var_declaration(self, ctx:ZCodeParser.Stmt_var_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#stmt_var_declaration_explicit.
    def visitStmt_var_declaration_explicit(self, ctx:ZCodeParser.Stmt_var_declaration_explicitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#stmt_var_declaration_dynamic.
    def visitStmt_var_declaration_dynamic(self, ctx:ZCodeParser.Stmt_var_declaration_dynamicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#stmt_var_declaration_var.
    def visitStmt_var_declaration_var(self, ctx:ZCodeParser.Stmt_var_declaration_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#value_init.
    def visitValue_init(self, ctx:ZCodeParser.Value_initContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#stmt_array_declaration.
    def visitStmt_array_declaration(self, ctx:ZCodeParser.Stmt_array_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#arrayId.
    def visitArrayId(self, ctx:ZCodeParser.ArrayIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#arrayDim.
    def visitArrayDim(self, ctx:ZCodeParser.ArrayDimContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#array_init.
    def visitArray_init(self, ctx:ZCodeParser.Array_initContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#arrayValue.
    def visitArrayValue(self, ctx:ZCodeParser.ArrayValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#exprLst.
    def visitExprLst(self, ctx:ZCodeParser.ExprLstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#stmt_func_declaration.
    def visitStmt_func_declaration(self, ctx:ZCodeParser.Stmt_func_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#paramLst.
    def visitParamLst(self, ctx:ZCodeParser.ParamLstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#paramLstTail.
    def visitParamLstTail(self, ctx:ZCodeParser.ParamLstTailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#param.
    def visitParam(self, ctx:ZCodeParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#func_body.
    def visitFunc_body(self, ctx:ZCodeParser.Func_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#statement.
    def visitStatement(self, ctx:ZCodeParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#stmt_assignment.
    def visitStmt_assignment(self, ctx:ZCodeParser.Stmt_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#assignment_lhs.
    def visitAssignment_lhs(self, ctx:ZCodeParser.Assignment_lhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#if_statement.
    def visitIf_statement(self, ctx:ZCodeParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#elif_statement.
    def visitElif_statement(self, ctx:ZCodeParser.Elif_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#else_statement.
    def visitElse_statement(self, ctx:ZCodeParser.Else_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#stmt_if.
    def visitStmt_if(self, ctx:ZCodeParser.Stmt_ifContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#elifLst.
    def visitElifLst(self, ctx:ZCodeParser.ElifLstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#stmt_for.
    def visitStmt_for(self, ctx:ZCodeParser.Stmt_forContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#stmt_break.
    def visitStmt_break(self, ctx:ZCodeParser.Stmt_breakContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#stmt_continue.
    def visitStmt_continue(self, ctx:ZCodeParser.Stmt_continueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#stmt_return.
    def visitStmt_return(self, ctx:ZCodeParser.Stmt_returnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#stmt_func_call.
    def visitStmt_func_call(self, ctx:ZCodeParser.Stmt_func_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#argLst.
    def visitArgLst(self, ctx:ZCodeParser.ArgLstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#argLstTail.
    def visitArgLstTail(self, ctx:ZCodeParser.ArgLstTailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#stmt_block.
    def visitStmt_block(self, ctx:ZCodeParser.Stmt_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#statementLst.
    def visitStatementLst(self, ctx:ZCodeParser.StatementLstContext):
        return self.visitChildren(ctx)



del ZCodeParser