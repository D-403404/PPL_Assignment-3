Set environment variable ANTLR_JAR to the file antlr-4.9.2-complete.jar in your computer
Change current directory to initial/src where there is file run.py
Type: python run.py gen 
Then type: python run.py test LexerSuite
Then type: python run.py test ParserSuite
Then type: python run.py test ASTGenSuite
Then type: python run.py test CheckerSuite

* Note:
- dynamic a <- f() is invalid (no function-storing variable) (?)
    => Dynamic for Function
- No recursive call in testcases
    => Recursive function first use
- dynamic c <- [1,2,3,4,5] is valid (can assign an array expr to a variable)
    => Implicit keyword for Array
- Input with no error => return "" => see updated TestUtils.py
    => Expect result when there is no error in the program

* Todo:
- Check visitId later
- Check visitArrayLiteral later => hardest
- Check visitReturn later
- Do visitVarDecl           DONE
- Check inferType (CallExpr) later