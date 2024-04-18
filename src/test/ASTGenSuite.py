import unittest
from TestUtils import TestAST
from AST import *

# from main.zcode.utils.AST import *

class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        input = """number a
        """
        expect = str(Program([VarDecl(Id("a"), NumberType())]))
        self.assertTrue(TestAST.test(input, expect, 300))
    
    def test_simple_program_2(self):
        input = """var str <- "Hello world!"
"""
        expect = str(Program([VarDecl(Id("str"), None, "var", StringLiteral("Hello world!"))]))
        self.assertTrue(TestAST.test(input, expect, 301))
    
    def test_simple_program_3(self):
        input = """func main() return 1
"""
        expect = "Program([FuncDecl(Id(main), [], Return(NumLit(1.0)))])"
        self.assertTrue(TestAST.test(input, expect, 302))

    def test_simple_program_4(self):
        input = """func inc(number a) return a + 1
func main() begin
var a <- 1
inc(a)
writeNumber(a)
end
"""
        expect = "Program([FuncDecl(Id(inc), [VarDecl(Id(a), NumberType, None, None)], Return(BinaryOp(+, Id(a), NumLit(1.0)))), FuncDecl(Id(main), [], Block([VarDecl(Id(a), None, var, NumLit(1.0)), CallStmt(Id(inc), [Id(a)]), CallStmt(Id(writeNumber), [Id(a)])]))])"
        self.assertTrue(TestAST.test(input, expect, 303))

    def test_simple_program_5(self):
        input = """func main() begin
number a
if (5 < 2) a <- 1
elif (not true) a <- 2
elif ("h" == "6") a <- 3
end
"""
        expect = "Program([FuncDecl(Id(main), [], Block([VarDecl(Id(a), NumberType, None, None), If((BinaryOp(<, NumLit(5.0), NumLit(2.0)), AssignStmt(Id(a), NumLit(1.0))), [(UnaryOp(not, BooleanLit(True)), AssignStmt(Id(a), NumLit(2.0))), (BinaryOp(==, StringLit(h), StringLit(6)), AssignStmt(Id(a), NumLit(3.0)))], None)]))])"
        self.assertTrue(TestAST.test(input, expect, 304))
    
    def test_simple_program_6(self):
        input = """func main() begin
if (1) writeString("1")
elif (2) if(3) writeString("1")
elif (4) writeString("1")
else writeString("1")
end
"""
        expect = "Program([FuncDecl(Id(main), [], Block([If((NumLit(1.0), CallStmt(Id(writeString), [StringLit(1)])), [(NumLit(2.0), If((NumLit(3.0), CallStmt(Id(writeString), [StringLit(1)])), [(NumLit(4.0), CallStmt(Id(writeString), [StringLit(1)]))], CallStmt(Id(writeString), [StringLit(1)])))], None)]))])"
        self.assertTrue(TestAST.test(input, expect, 305))

    def test_simple_program_7(self):
        input = """
func main()
begin
    var i <- 0
    number j <- 0
    for i until i <= 10 by 2
    begin
        for j until j <= 20 by 4
            writeNumber(i*j)
    end
end
"""
        expect = "Program([FuncDecl(Id(main), [], Block([VarDecl(Id(i), None, var, NumLit(0.0)), VarDecl(Id(j), NumberType, None, NumLit(0.0)), For(Id(i), BinaryOp(<=, Id(i), NumLit(10.0)), NumLit(2.0), Block([For(Id(j), BinaryOp(<=, Id(j), NumLit(20.0)), NumLit(4.0), CallStmt(Id(writeNumber), [BinaryOp(*, Id(i), Id(j))]))]))]))])"
        self.assertTrue(TestAST.test(input, expect, 306))
    
    def test_simple_program_8(self):
        input = """
number a <- 100

func sum(number n)
begin
    if (n = 0) return 0
    return n + sum(n - 1)
end

func main()
begin
    writeNumber(sum(a))
end
"""
        expect = "Program([VarDecl(Id(a), NumberType, None, NumLit(100.0)), FuncDecl(Id(sum), [VarDecl(Id(n), NumberType, None, None)], Block([If((BinaryOp(=, Id(n), NumLit(0.0)), Return(NumLit(0.0))), [], None), Return(BinaryOp(+, Id(n), CallExpr(Id(sum), [BinaryOp(-, Id(n), NumLit(1.0))])))])), FuncDecl(Id(main), [], Block([CallStmt(Id(writeNumber), [CallExpr(Id(sum), [Id(a)])])]))])"
        self.assertTrue(TestAST.test(input, expect, 307))

#===============================================================
        
    def test_1(self):
        input = """
func main ()
begin
    if (1)
        b()
    elif (2)
        if (3)
            c()
        elif (4)
            d()
        else
            e()
end
"""
        expect = str(Program([FuncDecl(Id('main'), [], Block([If(NumberLiteral(1.), CallStmt(Id('b'), []), [(NumberLiteral(2.), If(NumberLiteral(3.), CallStmt(Id('c'), []), [(NumberLiteral(4.), CallStmt(Id('d'), []))],CallStmt(Id('e'), [])))],None)]))]))
        self.assertTrue(TestAST.test(input, expect, 2001))
    
    def test_2(self):
        input = """
func main ()
begin
    if (1)
        b()
    elif (2)
        c()
    else d()
end
"""
        expect = str(Program([FuncDecl(Id('main'), [], Block([If(NumberLiteral(1.), CallStmt(Id('b'), []), [(NumberLiteral(2.), CallStmt(Id('c'), []))], CallStmt(Id('d'), []))]))]))
        self.assertTrue(TestAST.test(input, expect, 2002))
    
    def test_3(self):
        input = """
func main ()
begin
    if (1)
        b()
    else d()
end
"""
        expect = str(Program([FuncDecl(Id('main'), [], Block([If(NumberLiteral(1.), CallStmt(Id('b'), []), [], CallStmt(Id('d'), []))]))]))
        self.assertTrue(TestAST.test(input, expect, 2003))
    
    def test_4(self):
        '''test_1001 ParserSuite'''
        input = """
            func areDivisors(number num1, number num2)
                return ((num1 % num2 = 0) or (num2 % num1 = 0))
            ## comment lollll
            func main()             ## comment\\r lollll
                begin
                    var num1 <- readNumber()
                    var num2 <- readNumber()

                    if (areDivisors(num1, num2)) printString("Yes")
                    else printString("No")
                end
                ## comment lollll \n"""
        expect = str(Program([
            FuncDecl(Id('areDivisors'), 
                [VarDecl(Id('num1'),NumberType()), 
                    VarDecl(Id('num2'), NumberType())], 
                Return(BinaryOp('or', BinaryOp('=', BinaryOp('%', Id('num1'), Id('num2')), NumberLiteral(0.)), BinaryOp('=', BinaryOp('%', Id('num2'), Id('num1')), NumberLiteral(0.))))), 
            FuncDecl(Id('main'), [], 
                Block([
                    VarDecl(Id('num1'), None, 'var', CallExpr(Id('readNumber'), [])), 
                    VarDecl(Id('num2'), None, 'var', CallExpr(Id('readNumber'), [])), 
                    If(CallExpr(Id('areDivisors'), [Id('num1'), Id('num2')]), 
                        CallStmt(Id('printString'), [StringLiteral('Yes')]), 
                        [], 
                        CallStmt(Id('printString'), [StringLiteral('No')]))]))]))
        self.assertTrue(TestAST.test(input, expect, 2004))
    
    def test_5(self):
        '''test_1002 ParserSuite'''
        input = """
            func isPrime(number x)

            func main()
                begin
                    number x <- readNumber()
                    if (isPrime(x)) printString("Yes")
                    else printString("No")
                end

            func isPrime(number x)
                begin
                    if (x <= 1) return false
                    var i <- 2
                    for i until i > x / 2 by 1
                    begin
                        if (x % i = 0) return false
                    end
                return true
                end
                """
        expect = str(Program([
            FuncDecl(Id('isPrime'), [VarDecl(Id('x'),NumberType())]), 
            FuncDecl(Id('main'), [], 
                Block([
                    VarDecl(Id('x'), NumberType(), None, CallExpr(Id('readNumber'), [])), 
                    If(CallExpr(Id('isPrime'), [Id('x')]), 
                        CallStmt(Id('printString'), [StringLiteral('Yes')]), 
                        [], 
                        CallStmt(Id('printString'), [StringLiteral('No')]))])), 
            FuncDecl(Id('isPrime'), [VarDecl(Id('x'),NumberType())],
                Block([
                    If(BinaryOp('<=', Id('x'), NumberLiteral(1.)), Return(BooleanLiteral(False)), [], None), 
                    VarDecl(Id('i'), None, 'var', NumberLiteral(2.)), 
                    For(Id('i'), 
                        BinaryOp('>', Id('i'), BinaryOp('/', Id('x'), NumberLiteral(2.))), 
                        NumberLiteral(1.), 
                        Block([If(BinaryOp('=', BinaryOp('%', Id('x'), Id('i')), NumberLiteral(0.)), Return(BooleanLiteral(False)), [], None)])),
                    Return(BooleanLiteral(True))]))]))
        self.assertTrue(TestAST.test(input, expect, 2005))
    
    def test_6(self):
        '''test_1006 ParserSuite'''
        input = """string s <- writeString("Hello this is a '"test'"") \\n"""
        expect = str(Program([VarDecl(Id('s'), StringType(), None, CallExpr(Id('writeString'), [StringLiteral('Hello this is a \'"test\'"')]))]))
        self.assertTrue(TestAST.test(input, expect, 2006))
    
    def test_7(self):
        '''test_1007 ParserSuite'''
        input = """func foo(number arr[1,2,3])
        """
        expect = str(Program([FuncDecl(Id('foo'), [VarDecl(Id('arr'), ArrayType([1., 2., 3.], NumberType()), None, None)], None)]))
        self.assertTrue(TestAST.test(input, expect, 2007))
    
    def test_8(self):
        '''test_1012 ParserSuite'''
        input = """
func foo()
    begin
        if (a < b) if (c < d) bool e
    end
        """
        expect = str(Program([FuncDecl(Id('foo'), [], Block([If(BinaryOp('<', Id('a'), Id('b')), If(BinaryOp('<', Id('c'), Id('d')), VarDecl(Id('e'), BoolType(), None, None), [], None), [], None)]))]))
        self.assertTrue(TestAST.test(input, expect, 2008))
    
    def test_9(self):
        '''test_1015 ParserSuite'''
        input = """
func foo(number a[5], string b)
begin
var i <- 0
for i until i >= 5 by 1
begin
a[i] <- i * i + 5
end
return -1
end
        """
        expect = str(Program([FuncDecl(Id('foo'), [VarDecl(Id('a'), ArrayType([5.], NumberType()), None, None), VarDecl(Id('b'), StringType(), None, None)], 
                        Block([
                            VarDecl(Id('i'), None, 'var', NumberLiteral(0.)),
                            For(Id('i'), BinaryOp('>=', Id('i'), NumberLiteral(5.)), NumberLiteral(1.), Block([Assign(ArrayCell(Id('a'), [Id('i')]), BinaryOp('+', BinaryOp('*', Id('i'), Id('i')), NumberLiteral(5.)))])),
                            Return(UnaryOp('-', NumberLiteral(1.)))]))]))
        self.assertTrue(TestAST.test(input, expect, 2009))
    
    def test_10(self):
        input = """
var a <- 23.51e-30
"""
        expect = str(Program([VarDecl(Id('a'), None, 'var', NumberLiteral(23.51e-30))]))
        self.assertTrue(TestAST.test(input, expect, 2010))
    
    def test_11(self):
        input = """

string array[1,2,3,1] <- [3,"abcd",5., true, True, False, false]

"""
        expect = str(Program([VarDecl(Id('array'), ArrayType([1., 2., 3., 1.], StringType()), None, ArrayLiteral([NumberLiteral(3.), StringLiteral('abcd'), NumberLiteral(5.), BooleanLiteral(True), Id('True'), Id('False'), BooleanLiteral(False)]))]))
        self.assertTrue(TestAST.test(input, expect, 2011))
    
    def test_12(self):
        input = """
func foo(number a[2], number __aaaaa__, string b[1,2,3], bool arr[3.3,4e4,5.,0.5])
    begin
        if (f==2)
            begin
                if (a<2) continue
                if (b>3) continue
                if (c<=4) continue
                if (d>=5) continue
                elif (d==5 and (d!=5)) break
                elif (d!=5 and ((d==__) and d==5)) break
                elif ((c!="") and (c==0)) return _bool(true)
                elif ((c==true and (c=4)) and 4=c) return
                ##else goo(1,2,3)
                elif (true) begin\nend\n
                else begin\nend\n
            end
        elif (false) begin\nend\n
    end
"""
        expect = str(Program([
                    FuncDecl(Id('foo'), [
                            VarDecl(Id('a'), ArrayType([2.], NumberType()), None, None), 
                            VarDecl(Id('__aaaaa__'), NumberType(), None, None), 
                            VarDecl(Id('b'), ArrayType([1., 2., 3.], StringType()), None, None), 
                            VarDecl(Id('arr'), ArrayType([3.3, 4e4, 5., .5], BoolType()), None, None)], 
                        Block([If(BinaryOp('==', Id('f'), NumberLiteral(2.)), 
                            Block([
                                If(BinaryOp('<', Id('a'), NumberLiteral(2.)), Continue(), [], None), 
                                If(BinaryOp('>', Id('b'), NumberLiteral(3.)), Continue(), [], None), 
                                If(BinaryOp('<=', Id('c'), NumberLiteral(4.)), Continue(), [], None), 
                                If(BinaryOp('>=', Id('d'), NumberLiteral(5.)), Continue(), [
                                    (BinaryOp('==', Id('d'), BinaryOp('and', NumberLiteral(5.), BinaryOp('!=', Id('d'), NumberLiteral(5.)))), Break()), 
                                    (BinaryOp('!=', Id('d'), BinaryOp('and', NumberLiteral(5.), BinaryOp('==', BinaryOp('and', BinaryOp('==', Id('d'), Id('__')), Id('d')), NumberLiteral(5.)))), Break()), 
                                    (BinaryOp('and', BinaryOp('!=', Id('c'), StringLiteral('')), BinaryOp('==', Id('c'), NumberLiteral(0.))), Return(CallExpr(Id('_bool'), [BooleanLiteral(True)]))), 
                                    (BinaryOp('=', BinaryOp('and', BinaryOp('==', Id('c'), BinaryOp('and', BooleanLiteral(True), BinaryOp('=', Id('c'), NumberLiteral(4.)))), NumberLiteral(4.)), Id('c')), Return(None)), 
                                    (BooleanLiteral(True), Block([]))
                                    ], Block([]))]), 
                            [(BooleanLiteral(False), Block([]))], None)]))]))
        self.assertTrue(TestAST.test(input, expect, 2012))
    
    def test_13(self):
        input = """
func foo(number a[2], number __aaaaa__, string b[1,2,3], bool arr[3.3,4e4,5.,0.5])
    begin
        if (f==2)
            begin
                if (a<2) continue
                if (b>3) continue
                if (c<=4) 
                    if (d>=5) continue
                    elif (d==5 and (d!=5)) break
                    elif (d!=5 and ((d==__) and d==5)) break
                    elif ((c!="") and (c==0)) return _bool(true)
                    elif ((c==true and (c=4)) and 4=c) return
                    else goo(1,2,3)
                elif (true) begin\nend\n
                else begin\nend\n
            end
        elif (false) begin\nend\n
    end
"""
        expect = str(Program([
                    FuncDecl(Id('foo'), [
                            VarDecl(Id('a'), ArrayType([2.], NumberType()), None, None), 
                            VarDecl(Id('__aaaaa__'), NumberType(), None, None), 
                            VarDecl(Id('b'), ArrayType([1., 2., 3.], StringType()), None, None), 
                            VarDecl(Id('arr'), ArrayType([3.3, 4e4, 5., .5], BoolType()), None, None)], 
                        Block([If(BinaryOp('==', Id('f'), NumberLiteral(2.)), 
                            Block([
                                If(BinaryOp('<', Id('a'), NumberLiteral(2.)), Continue(), [], None), 
                                If(BinaryOp('>', Id('b'), NumberLiteral(3.)), Continue(), [], None), 
                                If(BinaryOp('<=', Id('c'), NumberLiteral(4.)), 
                                    If(BinaryOp('>=', Id('d'), NumberLiteral(5.)), Continue(), [
                                        (BinaryOp('==', Id('d'), BinaryOp('and', NumberLiteral(5.), BinaryOp('!=', Id('d'), NumberLiteral(5.)))), Break()), 
                                        (BinaryOp('!=', Id('d'), BinaryOp('and', NumberLiteral(5.), BinaryOp('==', BinaryOp('and', BinaryOp('==', Id('d'), Id('__')), Id('d')), NumberLiteral(5.)))), Break()), 
                                        (BinaryOp('and', BinaryOp('!=', Id('c'), StringLiteral('')), BinaryOp('==', Id('c'), NumberLiteral(0.))), Return(CallExpr(Id('_bool'), [BooleanLiteral(True)]))), 
                                        (BinaryOp('=', BinaryOp('and', BinaryOp('==', Id('c'), BinaryOp('and', BooleanLiteral(True), BinaryOp('=', Id('c'), NumberLiteral(4.)))), NumberLiteral(4.)), Id('c')), Return(None))
                                        ], 
                                        CallStmt(Id('goo'), [NumberLiteral(1.), NumberLiteral(2.), NumberLiteral(3.)])), 
                                [(BooleanLiteral(True), Block([]))], Block([]))]), 
                        [(BooleanLiteral(False), Block([]))], None)]))]))
        self.assertTrue(TestAST.test(input, expect, 2013))
    
    def test_14(self):
        '''test_1016 ParserSuite'''
        input = """
        var a <- [abc,xyz]
        """
        expect = str(Program([VarDecl(Id('a'), None, 'var', ArrayLiteral([Id('abc'), Id('xyz')]))]))
        self.assertTrue(TestAST.test(input, expect, 2014))
    
    def test_15(self):
        '''test_1022 ParserSuite'''
        input = """##number a\nnumber a\n##\\n var b\n"""
        expect = str(Program([VarDecl(Id('a'), NumberType(), None, None)]))
        self.assertTrue(TestAST.test(input, expect, 2015))
    
    def test_16(self):
        '''test_1028 ParserSuite'''
        input = """
            dynamic engineergaming123<-e2xyz
            func foo() begin\nend
"""
        expect = str(Program([VarDecl(Id('engineergaming123'), None, 'dynamic', Id('e2xyz')), FuncDecl(Id('foo'), [], Block([]))]))
        self.assertTrue(TestAST.test(input, expect, 2016))
    
    def test_17(self):
        '''test_1029 ParserSuite'''
        input = """
            var engineergaming123<-e2xyz
            func foo() begin\n\n\n\n\r\n\r\r\rend
"""
        expect = str(Program([VarDecl(Id('engineergaming123'), None, 'var', Id('e2xyz')), FuncDecl(Id('foo'), [], Block([]))]))
        self.assertTrue(TestAST.test(input, expect, 2017))
    
    def test_18(self):
        '''test_1038 ParserSuite'''
        input = """
func main()
        begin   \\n  var i <- 0\nfoo()[3 + foo(2)] <- a[b[2, 3]] + 4
    end\\n"""
        expect = str(Program([FuncDecl(Id('main'), [], Block([VarDecl(Id('i'), None, 'var', NumberLiteral(0.)), Assign(ArrayCell(CallExpr(Id('foo'), []), [BinaryOp('+', NumberLiteral(3.), CallExpr(Id('foo'), [NumberLiteral(2.)]))]), BinaryOp('+', ArrayCell(Id('a'), [ArrayCell(Id('b'), [NumberLiteral(2.), NumberLiteral(3.)])]), NumberLiteral(4.)))]))]))
        self.assertTrue(TestAST.test(input, expect, 2018))
    
    def test_19(self):
        '''test_1039 ParserSuite'''
        input = """
func main()      \n  """
        expect = str(Program([FuncDecl(Id('main'), [], None)]))
        self.assertTrue(TestAST.test(input, expect, 2019))
    
    def test_20(self):
        '''test_1049 ParserSuite'''
        input = """
number a <- "kdoqqw123" + 42E24
bool b <- true and false or not not s[20]
string c <- [r,t,x[3]]
var d <- [3,4,[5,6,7],[8,9,0]] + [[23]]
dynamic e
        """
        expect = str(Program([
                    VarDecl(Id('a'), NumberType(), None, BinaryOp('+', StringLiteral('kdoqqw123'), NumberLiteral(42E24))), 
                    VarDecl(Id('b'), BoolType(), None, BinaryOp('or', BinaryOp('and', BooleanLiteral(True), BooleanLiteral(False)), UnaryOp('not', UnaryOp('not', ArrayCell(Id('s'), [NumberLiteral(20.)]))))), 
                    VarDecl(Id('c'), StringType(), None, ArrayLiteral([Id('r'), Id('t'), ArrayCell(Id('x'), [NumberLiteral(3.)])])), 
                    VarDecl(Id('d'), None, 'var', BinaryOp('+', ArrayLiteral([NumberLiteral(3.), NumberLiteral(4.), ArrayLiteral([NumberLiteral(5.), NumberLiteral(6.), NumberLiteral(7.)]), ArrayLiteral([NumberLiteral(8.), NumberLiteral(9.), NumberLiteral(0.)])]), ArrayLiteral([ArrayLiteral([NumberLiteral(23.)])]))), 
                    VarDecl(Id('e'), None, 'dynamic', None)
                    ]))
        self.assertTrue(TestAST.test(input, expect, 2020))
    
    def test_21(self):
        '''test_1051 ParserSuite'''
        input = """
number a <- "kdoqqw123" + 42E24
bool b <- true and false or not (not s[20] and 7E3)
string c <- ([r,t,x[3]])
dynamic e <- abc
var d <- [3,4,[5,6,7],[8,9,0]] + [foo[23],_foo(str)[foo()]]
        """
        expect = str(Program([
                    VarDecl(Id('a'), NumberType(), None, BinaryOp('+', StringLiteral('kdoqqw123'), NumberLiteral(42E24))), 
                    VarDecl(Id('b'), BoolType(), None, BinaryOp('or', BinaryOp('and', BooleanLiteral(True), BooleanLiteral(False)), UnaryOp('not', BinaryOp('and', UnaryOp('not', ArrayCell(Id('s'), [NumberLiteral(20.)])), NumberLiteral(7E3))))), 
                    VarDecl(Id('c'), StringType(), None, ArrayLiteral([Id('r'), Id('t'), ArrayCell(Id('x'), [NumberLiteral(3.)])])), 
                    VarDecl(Id('e'), None, 'dynamic', Id('abc')), 
                    VarDecl(Id('d'), None, 'var', BinaryOp('+', ArrayLiteral([NumberLiteral(3.), NumberLiteral(4.), ArrayLiteral([NumberLiteral(5.), NumberLiteral(6.), NumberLiteral(7.)]), ArrayLiteral([NumberLiteral(8.), NumberLiteral(9.), NumberLiteral(0.)])]), ArrayLiteral([ArrayCell(Id('foo'), [NumberLiteral(23.)]), ArrayCell(CallExpr(Id('_foo'), [Id('str')]), [CallExpr(Id('foo'), [])])])))
                    ]))
        self.assertTrue(TestAST.test(input, expect, 2021))
    
    def test_22(self):
        '''test_1053 ParserSuite'''
        input = """
func foo()
    begin
        if (not x)
            return ---(--1)
    end
        """
        expect = str(Program([FuncDecl(Id('foo'), [], Block([If(UnaryOp('not', Id('x')), Return(UnaryOp('-', UnaryOp('-', UnaryOp('-', UnaryOp('-', UnaryOp('-', NumberLiteral(1.))))))))]))]))
        self.assertTrue(TestAST.test(input, expect, 2022))
    
    def test_23(self):
        '''test_1054 ParserSuite'''
        input = """
func foo()
    begin
        if ((x <= (y > z) ... "abc") ... ["xyz"...foo()])
            return ---(--1)
    end
        """
        expect = str(Program([FuncDecl(Id('foo'), [], Block([If(BinaryOp('...', BinaryOp('...', BinaryOp('<=', Id('x'), BinaryOp('>', Id('y'), Id('z'))), StringLiteral('abc')), ArrayLiteral([BinaryOp('...', StringLiteral('xyz'), CallExpr(Id('foo'), []))])), Return(UnaryOp('-', UnaryOp('-', UnaryOp('-', UnaryOp('-', UnaryOp('-', NumberLiteral(1.))))))))]))]))
        self.assertTrue(TestAST.test(input, expect, 2023))
    
    def test_24(self):
        '''test_1055 ParserSuite'''
        input = """
func foo()
    begin
        if ((x <= (y > z) ... "abc") ... ["xyz"...foo([[1,23,4],[2,"abc'"abc"]])])
            return ---(--1)
    end
        """
        expect = str(Program([FuncDecl(Id('foo'), [], Block([If(BinaryOp('...', BinaryOp('...', BinaryOp('<=', Id('x'), BinaryOp('>', Id('y'), Id('z'))), StringLiteral('abc')), ArrayLiteral([BinaryOp('...', StringLiteral('xyz'), CallExpr(Id('foo'), [ArrayLiteral([ArrayLiteral([NumberLiteral(1.), NumberLiteral(23.), NumberLiteral(4.)]), ArrayLiteral([NumberLiteral(2.), StringLiteral('abc\'"abc')])])]))])), Return(UnaryOp('-', UnaryOp('-', UnaryOp('-', UnaryOp('-', UnaryOp('-', NumberLiteral(1.))))))))]))]))
        self.assertTrue(TestAST.test(input, expect, 2024))
    
    def test_25(self):
        '''test_1060 ParserSuite'''
        input = """
func foo()
    begin
        aPI <- 3.14
        value <- x%[foo(5)]
        l[3] <- value * aPi
    end
        """
        expect = str(Program([FuncDecl(Id('foo'), [], Block([
            Assign(Id('aPI'), NumberLiteral(3.14)), 
            Assign(Id('value'), BinaryOp('%', Id('x'), ArrayLiteral([CallExpr(Id('foo'), [NumberLiteral(5.)])]))), 
            Assign(ArrayCell(Id('l'), [NumberLiteral(3.)]), BinaryOp('*', Id('value'), Id('aPi'))), 
        ]))]))
        self.assertTrue(TestAST.test(input, expect, 2025))
    
    def test_26(self):
        input = """
string a[3] <- 1 * (2 + 3)
bool b[4.3,3e4] <- false
        """
        expect = str(Program([VarDecl(Id('a'), ArrayType([3.], StringType()), None, BinaryOp('*', NumberLiteral(1.), BinaryOp('+', NumberLiteral(2.), NumberLiteral(3.)))), VarDecl(Id('b'), ArrayType([4.3, 3e4], BoolType()), None, BooleanLiteral(False))]))
        self.assertTrue(TestAST.test(input, expect, 2026))
    
    def test_27(self):
        '''test_1067 ParserSuite'''
        input = """
func foo()
begin
var i <- 0
for i until i >= 10 by 1
writeNumbe(i)
end
        """
        expect = str(Program([FuncDecl(Id('foo'), [], Block([VarDecl(Id('i'), None, 'var', NumberLiteral(0.)), For(Id('i'), BinaryOp('>=', Id('i'), NumberLiteral(10.)), NumberLiteral(1.), CallStmt(Id('writeNumbe'), [Id('i')]))]))]))
        self.assertTrue(TestAST.test(input, expect, 2027))
    
    def test_28(self):
        '''test_1069 ParserSuite'''
        input = """
func foo()
begin
number i[1,2,3] <- [[1,2],3]
for i until i >= 10 by 1
writeNumbe(i)
end
        """
        expect = str(Program([FuncDecl(Id('foo'), [], Block([VarDecl(Id('i'), ArrayType([1., 2., 3.], NumberType()), None, ArrayLiteral([ArrayLiteral([NumberLiteral(1.), NumberLiteral(2.)]), NumberLiteral(3.)])), For(Id('i'), BinaryOp('>=', Id('i'), NumberLiteral(10.)), NumberLiteral(1.), CallStmt(Id('writeNumbe'), [Id('i')]))]))]))
        self.assertTrue(TestAST.test(input, expect, 2028))
    
    def test_29(self):
        '''test_1074 ParserSuite'''
        input = """
func foo()
    begin
        number r
        number s
        r <- 2.0
        number a[5]
        number b[5]
        s <- r * r * 3.14
        a[0] <- s
    end
        """
        expect = str(Program([FuncDecl(Id('foo'), [], Block([
            VarDecl(Id('r'), NumberType(), None, None), 
            VarDecl(Id('s'), NumberType(), None, None), 
            Assign(Id('r'), NumberLiteral(2.0)), 
            VarDecl(Id('a'), ArrayType([5.], NumberType()), None, None), 
            VarDecl(Id('b'), ArrayType([5.], NumberType()), None, None), 
            Assign(Id('s'), BinaryOp('*', BinaryOp('*', Id('r'), Id('r')), NumberLiteral(3.14))), 
            Assign(ArrayCell(Id('a'), [NumberLiteral(0.)]), Id('s'))
        ]))]))
        self.assertTrue(TestAST.test(input, expect, 2029))
    
    def test_30(self):
        '''test_1079 ParserSuite'''
        input = """
func foo()
    begin
        number _##"abc"^^^\n
        number s
        r <- 2.0
        number a[5]
        number b[5]
        s <- r * r * 3.14
        a[0] <- s
    end
        """
        expect = str(Program([FuncDecl(Id('foo'), [], Block([
            VarDecl(Id('_'), NumberType(), None, None), 
            VarDecl(Id('s'), NumberType(), None, None), 
            Assign(Id('r'), NumberLiteral(2.0)), 
            VarDecl(Id('a'), ArrayType([5.], NumberType()), None, None), 
            VarDecl(Id('b'), ArrayType([5.], NumberType()), None, None), 
            Assign(Id('s'), BinaryOp('*', BinaryOp('*', Id('r'), Id('r')), NumberLiteral(3.14))), 
            Assign(ArrayCell(Id('a'), [NumberLiteral(0.)]), Id('s'))
        ]))]))
        self.assertTrue(TestAST.test(input, expect, 2030))
    
    def test_31(self):
        '''test_1081 ParserSuite'''
        input = """
dynamic r <- a - b * a/b
        """
        expect = str(Program([VarDecl(Id('r'), None, 'dynamic', BinaryOp('-', Id('a'), BinaryOp('/', BinaryOp('*', Id('b'), Id('a')), Id('b'))))]))
        self.assertTrue(TestAST.test(input, expect, 2031))
    
    def test_32(self):
        '''test_1082 ParserSuite'''
        input = """
dynamic r <- (a - (b * a/b))
        """
        expect = str(Program([VarDecl(Id('r'), None, 'dynamic', BinaryOp('-', Id('a'), BinaryOp('/', BinaryOp('*', Id('b'), Id('a')), Id('b'))))]))
        self.assertTrue(TestAST.test(input, expect, 2032))
    
    def test_33(self):
        '''test_1083 ParserSuite'''
        input = """
dynamic r <- ((a - b) * (a/b))...(a%b) + (a - (b + c) * 3)
        """
        expect = str(Program([VarDecl(Id('r'), None, 'dynamic', BinaryOp('...', BinaryOp('*', BinaryOp('-', Id('a'), Id('b')), BinaryOp('/', Id('a'), Id('b'))), BinaryOp('+', BinaryOp('%', Id('a'), Id('b')), BinaryOp('-', Id('a'), BinaryOp('*', BinaryOp('+', Id('b'), Id('c')), NumberLiteral(3.))))))]))
        self.assertTrue(TestAST.test(input, expect, 2033))
    
    def test_34(self):
        '''test_1084 ParserSuite'''
        input = """
dynamic r <- not((a - b) * (a/b))...(a%b) == (a or (b + c) and 3)
        """
        expect = str(Program([VarDecl(Id('r'), None, 'dynamic', BinaryOp('...', UnaryOp('not', BinaryOp('*', BinaryOp('-', Id('a'), Id('b')), BinaryOp('/', Id('a'), Id('b')))), BinaryOp('==', BinaryOp('%', Id('a'), Id('b')), BinaryOp('and', BinaryOp('or', Id('a'), BinaryOp('+', Id('b'), Id('c'))), NumberLiteral(3.)))))]))
        self.assertTrue(TestAST.test(input, expect, 2034))
    
    def test_35(self):
        '''test_1085 ParserSuite'''
        input = """
dynamic r <- not((a - b) * (a/b))...(a%b) == (a ... (b <= c) and 3 and a[(a+(b/c)),foo([a,b,c])])
        """
        expect = str(Program([VarDecl(Id('r'), None, 'dynamic', BinaryOp('...', UnaryOp('not', BinaryOp('*', BinaryOp('-', Id('a'), Id('b')), BinaryOp('/', Id('a'), Id('b')))), BinaryOp('==', BinaryOp('%', Id('a'), Id('b')), BinaryOp('...', Id('a'), BinaryOp('and', BinaryOp('and', BinaryOp('<=', Id('b'), Id('c')), NumberLiteral(3.)), ArrayCell(Id('a'), [BinaryOp('+', Id('a'), BinaryOp('/', Id('b'), Id('c'))), CallExpr(Id('foo'), [ArrayLiteral([Id('a'), Id('b'), Id('c')])])]))))))]))
        self.assertTrue(TestAST.test(input, expect, 2035))
    
    def test_36(self):
        '''test_1090 ParserSuite'''
        input = """
dynamic r <- not(((-a - -b) * (a/b)) = ((((-a%b) == (a ... (b <= c) and 3 >= a[(a != (b/c)),foo([a,b,c])]))) < (a > [b,c()[d[e]...((a >= b)...-c)]])))
        """
        expect = str(Program([VarDecl(Id('r'), None, 'dynamic', 
                    UnaryOp('not', 
                        BinaryOp('=', 
                            BinaryOp('*', 
                                BinaryOp('-', UnaryOp('-', Id('a')), UnaryOp('-', Id('b'))), 
                                BinaryOp('/', Id('a'), Id('b'))), 
                            BinaryOp('<', 
                                BinaryOp('==', 
                                    BinaryOp('%', UnaryOp('-', Id('a')), Id('b')), 
                                    BinaryOp('...', Id('a'), 
                                        BinaryOp('>=', 
                                            BinaryOp('and', BinaryOp('<=', Id('b'), Id('c')), NumberLiteral(3.)), 
                                            ArrayCell(Id('a'), [
                                                BinaryOp('!=', Id('a'), BinaryOp('/', Id('b'), Id('c'))), 
                                                CallExpr(Id('foo'), [ArrayLiteral([Id('a'), Id('b'), Id('c')])])])))), 
                                BinaryOp('>', Id('a'), 
                                    ArrayLiteral([
                                        Id('b'), 
                                        ArrayCell(CallExpr(Id('c'), []), [BinaryOp('...', ArrayCell(Id('d'), [Id('e')]), BinaryOp('...', BinaryOp('>=', Id('a'), Id('b')), UnaryOp('-', Id('c'))))])])))), 
                    ))]))
        self.assertTrue(TestAST.test(input, expect, 2036))
    
    def test_37(self):
        '''test_1093 ParserSuite'''
        input = """func main()\nbegin\nend\n"""
        expect = str(Program([FuncDecl(Id('main'), [], Block([]))]))
        self.assertTrue(TestAST.test(input, expect, 2037))
    
    def test_38(self):
        '''test_1095 ParserSuite'''
        input = """
func goo (number a, number b)
    return 1 - foo(1, a, b)
"""
        expect = str(Program([FuncDecl(Id('goo'), [VarDecl(Id('a'), NumberType()), VarDecl(Id('b'), NumberType())], Return(BinaryOp('-', NumberLiteral(1.), CallExpr(Id('foo'), [NumberLiteral(1.), Id('a'), Id('b')]))))]))
        self.assertTrue(TestAST.test(input, expect, 2038))
    
    def test_39(self):
        '''test_1098 ParserSuite'''
        input = """
number a
number b
number c

func foo(number a, string c, bool d)
    begin
        dynamic e
        e <- a + 4
        c <- a * d / 2.0
        return c + 1
    end

func goo (number a, number b)
    return foo(1, a, b)
"""
        expect = str(Program([
                    VarDecl(Id('a'), NumberType(), None, None), 
                    VarDecl(Id('b'), NumberType(), None, None), 
                    VarDecl(Id('c'), NumberType(), None, None), 
                    FuncDecl(Id('foo'), [VarDecl(Id('a'), NumberType()), VarDecl(Id('c'), StringType()), VarDecl(Id('d'), BoolType())], Block([
                        VarDecl(Id('e'), None, 'dynamic', None), 
                        Assign(Id('e'), BinaryOp('+', Id('a'), NumberLiteral(4.))), 
                        Assign(Id('c'), BinaryOp('/', BinaryOp('*', Id('a'), Id('d')), NumberLiteral(2.))), 
                        Return(BinaryOp('+', Id('c'), NumberLiteral(1.)))
                    ])), 
                    FuncDecl(Id('goo'), [VarDecl(Id('a'), NumberType()), VarDecl(Id('b'), NumberType())], Return(CallExpr(Id('foo'), [NumberLiteral(1.), Id('a'), Id('b')])))]))
        self.assertTrue(TestAST.test(input, expect, 2039))
    
    def test_40(self):
        '''Quick sort'''
        input = """
func partition(number arr, number start, number _end)
begin
	number pivot <- arr[start]

	number count <- 0
    i <- start + 1
	for i until i > _end by 1
		if (arr[i] <= pivot)
			count <- count + 1

	## Giving pivot element its correct position
	number pivotIndex <- start + count
	swap(arr[pivotIndex], arr[start])

	## Sorting left and right parts of the pivot element
    number i <- start
    number j <- _end

	return pivotIndex
end

func quickSort(number arr, number start, number _end)
begin

	## base case
	if (start >= _end)
		return

	## partitioning the array
	number p <- partition(arr, start, _end)

	## Sorting the left part
	quickSort(arr, start, p - 1)

	## Sorting the right part
	quickSort(arr, p + 1, _end)
end
"""
        expect = 'Program([FuncDecl(Id(partition), [VarDecl(Id(arr), NumberType, None, None), VarDecl(Id(start), NumberType, None, None), VarDecl(Id(_end), NumberType, None, None)], Block([VarDecl(Id(pivot), NumberType, None, ArrayCell(Id(arr), [Id(start)])), VarDecl(Id(count), NumberType, None, NumLit(0.0)), AssignStmt(Id(i), BinaryOp(+, Id(start), NumLit(1.0))), For(Id(i), BinaryOp(>, Id(i), Id(_end)), NumLit(1.0), If((BinaryOp(<=, ArrayCell(Id(arr), [Id(i)]), Id(pivot)), AssignStmt(Id(count), BinaryOp(+, Id(count), NumLit(1.0)))), [], None)), VarDecl(Id(pivotIndex), NumberType, None, BinaryOp(+, Id(start), Id(count))), CallStmt(Id(swap), [ArrayCell(Id(arr), [Id(pivotIndex)]), ArrayCell(Id(arr), [Id(start)])]), VarDecl(Id(i), NumberType, None, Id(start)), VarDecl(Id(j), NumberType, None, Id(_end)), Return(Id(pivotIndex))])), FuncDecl(Id(quickSort), [VarDecl(Id(arr), NumberType, None, None), VarDecl(Id(start), NumberType, None, None), VarDecl(Id(_end), NumberType, None, None)], Block([If((BinaryOp(>=, Id(start), Id(_end)), Return()), [], None), VarDecl(Id(p), NumberType, None, CallExpr(Id(partition), [Id(arr), Id(start), Id(_end)])), CallStmt(Id(quickSort), [Id(arr), Id(start), BinaryOp(-, Id(p), NumLit(1.0))]), CallStmt(Id(quickSort), [Id(arr), BinaryOp(+, Id(p), NumLit(1.0)), Id(_end)])]))])'
        self.assertTrue(TestAST.test(input, expect, 2040))
    
    def test_41(self):
        input = """
func area(number r)
begin
    return math_pi * r*r
end

func main()
begin
    res <- area(102.45)
    expect <- 32974.164346060104
    delta <- 0.000000001
    print((res > expect - delta) and (res < expect + delta))
end
"""
        expect = 'Program([FuncDecl(Id(area), [VarDecl(Id(r), NumberType, None, None)], Block([Return(BinaryOp(*, BinaryOp(*, Id(math_pi), Id(r)), Id(r)))])), FuncDecl(Id(main), [], Block([AssignStmt(Id(res), CallExpr(Id(area), [NumLit(102.45)])), AssignStmt(Id(expect), NumLit(32974.164346060104)), AssignStmt(Id(delta), NumLit(1e-09)), CallStmt(Id(print), [BinaryOp(and, BinaryOp(>, Id(res), BinaryOp(-, Id(expect), Id(delta))), BinaryOp(<, Id(res), BinaryOp(+, Id(expect), Id(delta))))])]))])'
        self.assertTrue(TestAST.test(input, expect, 2041))
    
    def test_42(self):
        input = """
func check(number lst, number n)
begin
    if (lst == [0]) return true
    return lst[0] > n and check(lst[1 ... len(lst)],n)
end

func main()
begin
    print(check([21,12,1000,100,90],11))
end
"""
        expect = 'Program([FuncDecl(Id(check), [VarDecl(Id(lst), NumberType, None, None), VarDecl(Id(n), NumberType, None, None)], Block([If((BinaryOp(==, Id(lst), ArrayLit(NumLit(0.0))), Return(BooleanLit(True))), [], None), Return(BinaryOp(>, ArrayCell(Id(lst), [NumLit(0.0)]), BinaryOp(and, Id(n), CallExpr(Id(check), [ArrayCell(Id(lst), [BinaryOp(..., NumLit(1.0), CallExpr(Id(len), [Id(lst)]))]), Id(n)]))))])), FuncDecl(Id(main), [], Block([CallStmt(Id(print), [CallExpr(Id(check), [ArrayLit(NumLit(21.0), NumLit(12.0), NumLit(1000.0), NumLit(100.0), NumLit(90.0)), NumLit(11.0)])])]))])'
        self.assertTrue(TestAST.test(input, expect, 2042))
    
    def test_43(self):
        input = """
func gcd(number a, number b)
begin
    if (a=b) return b
    if (a>b) return gcd(a-b,b)
    return gcd(a,b-a)
end

func main()
begin
    print(gcd(1071,462))
end
"""
        expect = 'Program([FuncDecl(Id(gcd), [VarDecl(Id(a), NumberType, None, None), VarDecl(Id(b), NumberType, None, None)], Block([If((BinaryOp(=, Id(a), Id(b)), Return(Id(b))), [], None), If((BinaryOp(>, Id(a), Id(b)), Return(CallExpr(Id(gcd), [BinaryOp(-, Id(a), Id(b)), Id(b)]))), [], None), Return(CallExpr(Id(gcd), [Id(a), BinaryOp(-, Id(b), Id(a))]))])), FuncDecl(Id(main), [], Block([CallStmt(Id(print), [CallExpr(Id(gcd), [NumLit(1071.0), NumLit(462.0)])])]))])'
        self.assertTrue(TestAST.test(input, expect, 2043))
    
    def test_44(self):
        input = """
func foo()
begin
    lst <- input()
    print(split(","))
    print(tuple(split(",")))
end

func main()
begin
    print(gcd(1071,462))
end
"""
        expect = 'Program([FuncDecl(Id(foo), [], Block([AssignStmt(Id(lst), CallExpr(Id(input), [])), CallStmt(Id(print), [CallExpr(Id(split), [StringLit(,)])]), CallStmt(Id(print), [CallExpr(Id(tuple), [CallExpr(Id(split), [StringLit(,)])])])])), FuncDecl(Id(main), [], Block([CallStmt(Id(print), [CallExpr(Id(gcd), [NumLit(1071.0), NumLit(462.0)])])]))])'
        self.assertTrue(TestAST.test(input, expect, 2044))
    
    def test_45(self):
        input = """
func f(number lst)
begin
    return [split(","), tuple(split(","))]
end
    
func main()
begin
    lst <- input()
    res <- f(lst)
    print(res[0])
    print(res[1])
end
"""
        expect = 'Program([FuncDecl(Id(f), [VarDecl(Id(lst), NumberType, None, None)], Block([Return(ArrayLit(CallExpr(Id(split), [StringLit(,)]), CallExpr(Id(tuple), [CallExpr(Id(split), [StringLit(,)])])))])), FuncDecl(Id(main), [], Block([AssignStmt(Id(lst), CallExpr(Id(input), [])), AssignStmt(Id(res), CallExpr(Id(f), [Id(lst)])), CallStmt(Id(print), [ArrayCell(Id(res), [NumLit(0.0)])]), CallStmt(Id(print), [ArrayCell(Id(res), [NumLit(1.0)])])]))])'
        self.assertTrue(TestAST.test(input, expect, 2045))
    
    def test_46(self):
        input = """
func product(number lst)
begin
    if (lst == [0]) return 1
    return lst[0] * product(lst[1 ... len(lst)])
end

func main()
begin
    print(product([3,4,7,11]))
end
"""
        expect = 'Program([FuncDecl(Id(product), [VarDecl(Id(lst), NumberType, None, None)], Block([If((BinaryOp(==, Id(lst), ArrayLit(NumLit(0.0))), Return(NumLit(1.0))), [], None), Return(BinaryOp(*, ArrayCell(Id(lst), [NumLit(0.0)]), CallExpr(Id(product), [ArrayCell(Id(lst), [BinaryOp(..., NumLit(1.0), CallExpr(Id(len), [Id(lst)]))])])))])), FuncDecl(Id(main), [], Block([CallStmt(Id(print), [CallExpr(Id(product), [ArrayLit(NumLit(3.0), NumLit(4.0), NumLit(7.0), NumLit(11.0))])])]))])'
        self.assertTrue(TestAST.test(input, expect, 2046))
    
    def test_47(self):
        input = """
func sum_of_cube(number n)
begin
    if (n == 1) return 0
    return (n-1)*(n-1)*(n-1) + sum_of_cube(n-1)
end

func main()
begin
    print(sum_of_cube(12))
end
"""
        expect = 'Program([FuncDecl(Id(sum_of_cube), [VarDecl(Id(n), NumberType, None, None)], Block([If((BinaryOp(==, Id(n), NumLit(1.0)), Return(NumLit(0.0))), [], None), Return(BinaryOp(+, BinaryOp(*, BinaryOp(*, BinaryOp(-, Id(n), NumLit(1.0)), BinaryOp(-, Id(n), NumLit(1.0))), BinaryOp(-, Id(n), NumLit(1.0))), CallExpr(Id(sum_of_cube), [BinaryOp(-, Id(n), NumLit(1.0))])))])), FuncDecl(Id(main), [], Block([CallStmt(Id(print), [CallExpr(Id(sum_of_cube), [NumLit(12.0)])])]))])'
        self.assertTrue(TestAST.test(input, expect, 2047))
    
    def test_48(self):
        input = """
func dist(number lst, number n)
begin
    return list(map(lambda(x,n), lst))
end

func main()
begin
    print(dist([3,4,1,5],6))
    print(dist([1,2,3],"a"))
    print(dist([1],"a"))
end
"""
        expect = 'Program([FuncDecl(Id(dist), [VarDecl(Id(lst), NumberType, None, None), VarDecl(Id(n), NumberType, None, None)], Block([Return(CallExpr(Id(list), [CallExpr(Id(map), [CallExpr(Id(lambda), [Id(x), Id(n)]), Id(lst)])]))])), FuncDecl(Id(main), [], Block([CallStmt(Id(print), [CallExpr(Id(dist), [ArrayLit(NumLit(3.0), NumLit(4.0), NumLit(1.0), NumLit(5.0)), NumLit(6.0)])]), CallStmt(Id(print), [CallExpr(Id(dist), [ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)), StringLit(a)])]), CallStmt(Id(print), [CallExpr(Id(dist), [ArrayLit(NumLit(1.0)), StringLit(a)])])]))])'
        self.assertTrue(TestAST.test(input, expect, 2048))
    
    def test_49(self):
        input = """
func dist(number lst, number n)
begin
    if (not lst)
        return
    return [tuple(lst[0],n)] + dist(lst[tail],n)
end

func main()
begin
    print(dist([3,4,1,5],6))
    print(dist([1,2,3],"a"))
    print(dist([1],"a"))
end
"""
        expect = 'Program([FuncDecl(Id(dist), [VarDecl(Id(lst), NumberType, None, None), VarDecl(Id(n), NumberType, None, None)], Block([If((UnaryOp(not, Id(lst)), Return()), [], None), Return(BinaryOp(+, ArrayLit(CallExpr(Id(tuple), [ArrayCell(Id(lst), [NumLit(0.0)]), Id(n)])), CallExpr(Id(dist), [ArrayCell(Id(lst), [Id(tail)]), Id(n)])))])), FuncDecl(Id(main), [], Block([CallStmt(Id(print), [CallExpr(Id(dist), [ArrayLit(NumLit(3.0), NumLit(4.0), NumLit(1.0), NumLit(5.0)), NumLit(6.0)])]), CallStmt(Id(print), [CallExpr(Id(dist), [ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)), StringLit(a)])]), CallStmt(Id(print), [CallExpr(Id(dist), [ArrayLit(NumLit(1.0)), StringLit(a)])])]))])'
        self.assertTrue(TestAST.test(input, expect, 2049))
    
    def test_50(self):
        input = """
func flatten(number lst)
begin
    return list(reduce(lambda(res + xs), lst, [0]))
end

func main()
begin
    print(flatten([[1],[2],[3],[4],[5,6,7]]))
    print(flatten([[1,2,3]]))
    print(flatten([[1,2,3],[4,5],[6,7]]))
end
"""
        expect = 'Program([FuncDecl(Id(flatten), [VarDecl(Id(lst), NumberType, None, None)], Block([Return(CallExpr(Id(list), [CallExpr(Id(reduce), [CallExpr(Id(lambda), [BinaryOp(+, Id(res), Id(xs))]), Id(lst), ArrayLit(NumLit(0.0))])]))])), FuncDecl(Id(main), [], Block([CallStmt(Id(print), [CallExpr(Id(flatten), [ArrayLit(ArrayLit(NumLit(1.0)), ArrayLit(NumLit(2.0)), ArrayLit(NumLit(3.0)), ArrayLit(NumLit(4.0)), ArrayLit(NumLit(5.0), NumLit(6.0), NumLit(7.0)))])]), CallStmt(Id(print), [CallExpr(Id(flatten), [ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)))])]), CallStmt(Id(print), [CallExpr(Id(flatten), [ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)), ArrayLit(NumLit(4.0), NumLit(5.0)), ArrayLit(NumLit(6.0), NumLit(7.0)))])])]))])'
        self.assertTrue(TestAST.test(input, expect, 2050))
    
    def test_51(self):
        input = """
func flatten(number lst)
begin
    if (not lst)
        return
    return lst[0] + flatten(lst[tail])
end

func main()
begin
    print(flatten([[1],[2],[3],[4],[5,6,7]]))
    print(flatten([[1,2,3]]))
    print(flatten([[1,2,3],[4,5],[6,7]]))
end
"""
        expect = 'Program([FuncDecl(Id(flatten), [VarDecl(Id(lst), NumberType, None, None)], Block([If((UnaryOp(not, Id(lst)), Return()), [], None), Return(BinaryOp(+, ArrayCell(Id(lst), [NumLit(0.0)]), CallExpr(Id(flatten), [ArrayCell(Id(lst), [Id(tail)])])))])), FuncDecl(Id(main), [], Block([CallStmt(Id(print), [CallExpr(Id(flatten), [ArrayLit(ArrayLit(NumLit(1.0)), ArrayLit(NumLit(2.0)), ArrayLit(NumLit(3.0)), ArrayLit(NumLit(4.0)), ArrayLit(NumLit(5.0), NumLit(6.0), NumLit(7.0)))])]), CallStmt(Id(print), [CallExpr(Id(flatten), [ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)))])]), CallStmt(Id(print), [CallExpr(Id(flatten), [ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)), ArrayLit(NumLit(4.0), NumLit(5.0)), ArrayLit(NumLit(6.0), NumLit(7.0)))])])]))])'
        self.assertTrue(TestAST.test(input, expect, 2051))
    
    def test_52(self):
        input = """
func lessThan(number lst)
    return filter(lambda(x < n), lst)

func main()
begin
    print(lessThan([1,2,3,-1,0],6))
    print(lessThan([1,2,3,4,5],4))
end
"""
        expect = 'Program([FuncDecl(Id(lessThan), [VarDecl(Id(lst), NumberType, None, None)], Return(CallExpr(Id(filter), [CallExpr(Id(lambda), [BinaryOp(<, Id(x), Id(n))]), Id(lst)]))), FuncDecl(Id(main), [], Block([CallStmt(Id(print), [CallExpr(Id(lessThan), [ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0), UnaryOp(-, NumLit(1.0)), NumLit(0.0)), NumLit(6.0)])]), CallStmt(Id(print), [CallExpr(Id(lessThan), [ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0), NumLit(4.0), NumLit(5.0)), NumLit(4.0)])])]))])'
        self.assertTrue(TestAST.test(input, expect, 2052))
    
    def test_53(self):
        input = """
func lessThan(number lst)
begin
    if (not lst)
        return
    if (lst[0] < n)
        return [lst[0]] + lessThan(lst[tail],n)
    return lessThan(lst[tail],n)
end

func main()
begin
    print(lessThan([1,2,3,-1,0],6))
    print(lessThan([1,2,3,4,5],4))
end
"""
        expect = 'Program([FuncDecl(Id(lessThan), [VarDecl(Id(lst), NumberType, None, None)], Block([If((UnaryOp(not, Id(lst)), Return()), [], None), If((BinaryOp(<, ArrayCell(Id(lst), [NumLit(0.0)]), Id(n)), Return(BinaryOp(+, ArrayLit(ArrayCell(Id(lst), [NumLit(0.0)])), CallExpr(Id(lessThan), [ArrayCell(Id(lst), [Id(tail)]), Id(n)])))), [], None), Return(CallExpr(Id(lessThan), [ArrayCell(Id(lst), [Id(tail)]), Id(n)]))])), FuncDecl(Id(main), [], Block([CallStmt(Id(print), [CallExpr(Id(lessThan), [ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0), UnaryOp(-, NumLit(1.0)), NumLit(0.0)), NumLit(6.0)])]), CallStmt(Id(print), [CallExpr(Id(lessThan), [ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0), NumLit(4.0), NumLit(5.0)), NumLit(4.0)])])]))])'
        self.assertTrue(TestAST.test(input, expect, 2053))
    
    def test_54(self):
        input = """
func lstSquare(number n)
begin
    if (n = 0)
        return
    return lstSquare(n - 1) + [n * n]
end

func main()
begin
    print(lstSquare(3.14159e37))
end
"""
        expect = 'Program([FuncDecl(Id(lstSquare), [VarDecl(Id(n), NumberType, None, None)], Block([If((BinaryOp(=, Id(n), NumLit(0.0)), Return()), [], None), Return(BinaryOp(+, CallExpr(Id(lstSquare), [BinaryOp(-, Id(n), NumLit(1.0))]), ArrayLit(BinaryOp(*, Id(n), Id(n)))))])), FuncDecl(Id(main), [], Block([CallStmt(Id(print), [CallExpr(Id(lstSquare), [NumLit(3.14159e+37)])])]))])'
        self.assertTrue(TestAST.test(input, expect, 2054))
    
    def test_55(self):
        input = """
func lstSquare(number n)
    return list(map(lambda(x * x), range(1, n + 1)))

func main()
begin
    print(lstSquare(3.14159e37))
end
"""
        expect = 'Program([FuncDecl(Id(lstSquare), [VarDecl(Id(n), NumberType, None, None)], Return(CallExpr(Id(list), [CallExpr(Id(map), [CallExpr(Id(lambda), [BinaryOp(*, Id(x), Id(x))]), CallExpr(Id(range), [NumLit(1.0), BinaryOp(+, Id(n), NumLit(1.0))])])]))), FuncDecl(Id(main), [], Block([CallStmt(Id(print), [CallExpr(Id(lstSquare), [NumLit(3.14159e+37)])])]))])'
        self.assertTrue(TestAST.test(input, expect, 2055))
    
    def test_56(self):
        input = """
func compose(string f1, bool f2, number fs)
begin
    var innerFunc <- reduce(lambda(f(res)), fs[-1] + tuple(f2,f1), x)
    return innerFunc
end

func main()
begin
    var f <- compose(increase,square)
    print(f(3)) ##increase(square(3)) = 10

    dynamic f <- compose(increase,square,double,decrease)
    print(f(3))

    string f <- compose()
    print("compose() missing 1 required positional argument")
end
"""
        expect = 'Program([FuncDecl(Id(compose), [VarDecl(Id(f1), StringType, None, None), VarDecl(Id(f2), BoolType, None, None), VarDecl(Id(fs), NumberType, None, None)], Block([VarDecl(Id(innerFunc), None, var, CallExpr(Id(reduce), [CallExpr(Id(lambda), [CallExpr(Id(f), [Id(res)])]), BinaryOp(+, ArrayCell(Id(fs), [UnaryOp(-, NumLit(1.0))]), CallExpr(Id(tuple), [Id(f2), Id(f1)])), Id(x)])), Return(Id(innerFunc))])), FuncDecl(Id(main), [], Block([VarDecl(Id(f), None, var, CallExpr(Id(compose), [Id(increase), Id(square)])), CallStmt(Id(print), [CallExpr(Id(f), [NumLit(3.0)])]), VarDecl(Id(f), None, dynamic, CallExpr(Id(compose), [Id(increase), Id(square), Id(double), Id(decrease)])), CallStmt(Id(print), [CallExpr(Id(f), [NumLit(3.0)])]), VarDecl(Id(f), StringType, None, CallExpr(Id(compose), [])), CallStmt(Id(print), [StringLit(compose() missing 1 required positional argument)])]))])'
        self.assertTrue(TestAST.test(input, expect, 2056))
    
    def test_57(self):
        input = """
func multiply(number F[2,2], number M[2,2]) 

func power(number F[2,2], number n) 
  
func fib(number n) 
begin
    number F[2,2] <- [ [ 1, 1 ], [ 1, 0 ] ]
      
    if (n == 0) 
        return 0 
          
    power(F, n - 1) 
      
    return F[0,0] 
end
  
func multiply(number F[2,2], number M[2,2]) 
begin
    number x <- F[0,0] * M[0,0] + F[0,1] * M[1,0] 
    number y <- F[0,0] * M[0,1] + F[0,1] * M[1,1] 
    number z <- F[1,0] * M[0,0] + F[1,1] * M[1,0] 
    number w <- F[1,0] * M[0,1] + F[1,1] * M[1,1] 
      
    F[0,0] <- x 
    F[0,1] <- y 
    F[1,0] <- z 
    F[1,1] <- w 
end
  
func power(number F[2,2], number n) 
begin
    number i 
    number M[2,2] <- [ [ 1, 1 ], [ 1, 0 ] ]
      
    ## n - 1 times multiply the  
    ## matrix to [[1,1], [1,0]]
    i <- 2
    for i until i > n by 1 
        multiply(F, M) 
end
  
## Driver code 
func main() 
begin
    number n <- 9 
    print(" "...fib(n)) 
end
"""
        expect = 'Program([FuncDecl(Id(multiply), [VarDecl(Id(F), ArrayType([2.0, 2.0], NumberType), None, None), VarDecl(Id(M), ArrayType([2.0, 2.0], NumberType), None, None)], None), FuncDecl(Id(power), [VarDecl(Id(F), ArrayType([2.0, 2.0], NumberType), None, None), VarDecl(Id(n), NumberType, None, None)], None), FuncDecl(Id(fib), [VarDecl(Id(n), NumberType, None, None)], Block([VarDecl(Id(F), ArrayType([2.0, 2.0], NumberType), None, ArrayLit(ArrayLit(NumLit(1.0), NumLit(1.0)), ArrayLit(NumLit(1.0), NumLit(0.0)))), If((BinaryOp(==, Id(n), NumLit(0.0)), Return(NumLit(0.0))), [], None), CallStmt(Id(power), [Id(F), BinaryOp(-, Id(n), NumLit(1.0))]), Return(ArrayCell(Id(F), [NumLit(0.0), NumLit(0.0)]))])), FuncDecl(Id(multiply), [VarDecl(Id(F), ArrayType([2.0, 2.0], NumberType), None, None), VarDecl(Id(M), ArrayType([2.0, 2.0], NumberType), None, None)], Block([VarDecl(Id(x), NumberType, None, BinaryOp(+, BinaryOp(*, ArrayCell(Id(F), [NumLit(0.0), NumLit(0.0)]), ArrayCell(Id(M), [NumLit(0.0), NumLit(0.0)])), BinaryOp(*, ArrayCell(Id(F), [NumLit(0.0), NumLit(1.0)]), ArrayCell(Id(M), [NumLit(1.0), NumLit(0.0)])))), VarDecl(Id(y), NumberType, None, BinaryOp(+, BinaryOp(*, ArrayCell(Id(F), [NumLit(0.0), NumLit(0.0)]), ArrayCell(Id(M), [NumLit(0.0), NumLit(1.0)])), BinaryOp(*, ArrayCell(Id(F), [NumLit(0.0), NumLit(1.0)]), ArrayCell(Id(M), [NumLit(1.0), NumLit(1.0)])))), VarDecl(Id(z), NumberType, None, BinaryOp(+, BinaryOp(*, ArrayCell(Id(F), [NumLit(1.0), NumLit(0.0)]), ArrayCell(Id(M), [NumLit(0.0), NumLit(0.0)])), BinaryOp(*, ArrayCell(Id(F), [NumLit(1.0), NumLit(1.0)]), ArrayCell(Id(M), [NumLit(1.0), NumLit(0.0)])))), VarDecl(Id(w), NumberType, None, BinaryOp(+, BinaryOp(*, ArrayCell(Id(F), [NumLit(1.0), NumLit(0.0)]), ArrayCell(Id(M), [NumLit(0.0), NumLit(1.0)])), BinaryOp(*, ArrayCell(Id(F), [NumLit(1.0), NumLit(1.0)]), ArrayCell(Id(M), [NumLit(1.0), NumLit(1.0)])))), AssignStmt(ArrayCell(Id(F), [NumLit(0.0), NumLit(0.0)]), Id(x)), AssignStmt(ArrayCell(Id(F), [NumLit(0.0), NumLit(1.0)]), Id(y)), AssignStmt(ArrayCell(Id(F), [NumLit(1.0), NumLit(0.0)]), Id(z)), AssignStmt(ArrayCell(Id(F), [NumLit(1.0), NumLit(1.0)]), Id(w))])), FuncDecl(Id(power), [VarDecl(Id(F), ArrayType([2.0, 2.0], NumberType), None, None), VarDecl(Id(n), NumberType, None, None)], Block([VarDecl(Id(i), NumberType, None, None), VarDecl(Id(M), ArrayType([2.0, 2.0], NumberType), None, ArrayLit(ArrayLit(NumLit(1.0), NumLit(1.0)), ArrayLit(NumLit(1.0), NumLit(0.0)))), AssignStmt(Id(i), NumLit(2.0)), For(Id(i), BinaryOp(>, Id(i), Id(n)), NumLit(1.0), CallStmt(Id(multiply), [Id(F), Id(M)]))])), FuncDecl(Id(main), [], Block([VarDecl(Id(n), NumberType, None, NumLit(9.0)), CallStmt(Id(print), [BinaryOp(..., StringLit( ), CallExpr(Id(fib), [Id(n)]))])]))])'
        self.assertTrue(TestAST.test(input, expect, 2057))
    
    def test_58(self):
        input = """
func fib(number n) 
begin
    number a <- 0
    number b <- 1
    number c
    number i <- 2
    if( n == 0) 
        return a 
    for i until i > n by 1 
    begin
       c <- a + b 
       a <- b 
       b <- c 
    end
    return b 
end
  
## Driver code 
func main() 
begin
    number n <- 9 
    print(" "...fib(n)) 
end
"""
        expect = 'Program([FuncDecl(Id(fib), [VarDecl(Id(n), NumberType, None, None)], Block([VarDecl(Id(a), NumberType, None, NumLit(0.0)), VarDecl(Id(b), NumberType, None, NumLit(1.0)), VarDecl(Id(c), NumberType, None, None), VarDecl(Id(i), NumberType, None, NumLit(2.0)), If((BinaryOp(==, Id(n), NumLit(0.0)), Return(Id(a))), [], None), For(Id(i), BinaryOp(>, Id(i), Id(n)), NumLit(1.0), Block([AssignStmt(Id(c), BinaryOp(+, Id(a), Id(b))), AssignStmt(Id(a), Id(b)), AssignStmt(Id(b), Id(c))])), Return(Id(b))])), FuncDecl(Id(main), [], Block([VarDecl(Id(n), NumberType, None, NumLit(9.0)), CallStmt(Id(print), [BinaryOp(..., StringLit( ), CallExpr(Id(fib), [Id(n)]))])]))])'
        self.assertTrue(TestAST.test(input, expect, 2058))
    
    def test_59(self):
        input = """
func reverseDigits(number num) 
begin
    number rev_num <- 0
    for num until num <= 0 by -9*num/10
    begin
        rev_num <- rev_num * 10 + num % 10
    end
    return rev_num
end
  
## Driver code 
func main() 
begin
    number n <- 123456
    print(reverseDigits(n)) 
end
"""
        expect = 'Program([FuncDecl(Id(reverseDigits), [VarDecl(Id(num), NumberType, None, None)], Block([VarDecl(Id(rev_num), NumberType, None, NumLit(0.0)), For(Id(num), BinaryOp(<=, Id(num), NumLit(0.0)), BinaryOp(/, BinaryOp(*, UnaryOp(-, NumLit(9.0)), Id(num)), NumLit(10.0)), Block([AssignStmt(Id(rev_num), BinaryOp(+, BinaryOp(*, Id(rev_num), NumLit(10.0)), BinaryOp(%, Id(num), NumLit(10.0))))])), Return(Id(rev_num))])), FuncDecl(Id(main), [], Block([VarDecl(Id(n), NumberType, None, NumLit(123456.0)), CallStmt(Id(print), [CallExpr(Id(reverseDigits), [Id(n)])])]))])'
        self.assertTrue(TestAST.test(input, expect, 2059))
    
    def test_60(self):
        input = """
func factorial(number n)
begin
    number res <- 1
    number i <- 2
    for i until i > n by 1
        res <- res * i
    return res
end
  
## Driver code 
func main() 
begin
    number n <- 123456
    print(factorial(n)) 
end
"""
        expect = 'Program([FuncDecl(Id(factorial), [VarDecl(Id(n), NumberType, None, None)], Block([VarDecl(Id(res), NumberType, None, NumLit(1.0)), VarDecl(Id(i), NumberType, None, NumLit(2.0)), For(Id(i), BinaryOp(>, Id(i), Id(n)), NumLit(1.0), AssignStmt(Id(res), BinaryOp(*, Id(res), Id(i)))), Return(Id(res))])), FuncDecl(Id(main), [], Block([VarDecl(Id(n), NumberType, None, NumLit(123456.0)), CallStmt(Id(print), [CallExpr(Id(factorial), [Id(n)])])]))])'
        self.assertTrue(TestAST.test(input, expect, 2060))
    
    def test_61(self):
        input = """
func factorial(number n)
begin
    ## Single line to find factorial
    if (n = 1)
        return (n = 1) or (n = 0)
    else
        return n * factorial(n - 1)
end
  
## Driver code 
func main() 
begin
    number n <- 123456
    print(factorial(n)) 
end
"""
        expect = 'Program([FuncDecl(Id(factorial), [VarDecl(Id(n), NumberType, None, None)], Block([If((BinaryOp(=, Id(n), NumLit(1.0)), Return(BinaryOp(or, BinaryOp(=, Id(n), NumLit(1.0)), BinaryOp(=, Id(n), NumLit(0.0))))), [], Return(BinaryOp(*, Id(n), CallExpr(Id(factorial), [BinaryOp(-, Id(n), NumLit(1.0))]))))])), FuncDecl(Id(main), [], Block([VarDecl(Id(n), NumberType, None, NumLit(123456.0)), CallStmt(Id(print), [CallExpr(Id(factorial), [Id(n)])])]))])'
        self.assertTrue(TestAST.test(input, expect, 2061))
    
    def test_62(self):
        input = """
func foo(number n)
begin
    number res <- 1
    number i <- 2
    for i until i > n by 1
        if (i < 5) res <- res + 1
        elif (i < 7) 
            if (res < 100) 
                for res until res >= 100 by 5
                    continue
            elif (res < 200) res <- res + 2
            else res <- res / 2
        elif (i < 10)
        begin
            print(i % 2)
            res <- i
        end
        else break
    return res
end
  
## Driver code 
func main() 
begin
    number n <- 123456
    print(foo(n)) 
end
"""
        expect = 'Program([FuncDecl(Id(foo), [VarDecl(Id(n), NumberType, None, None)], Block([VarDecl(Id(res), NumberType, None, NumLit(1.0)), VarDecl(Id(i), NumberType, None, NumLit(2.0)), For(Id(i), BinaryOp(>, Id(i), Id(n)), NumLit(1.0), If((BinaryOp(<, Id(i), NumLit(5.0)), AssignStmt(Id(res), BinaryOp(+, Id(res), NumLit(1.0)))), [(BinaryOp(<, Id(i), NumLit(7.0)), If((BinaryOp(<, Id(res), NumLit(100.0)), For(Id(res), BinaryOp(>=, Id(res), NumLit(100.0)), NumLit(5.0), Continue)), [(BinaryOp(<, Id(res), NumLit(200.0)), AssignStmt(Id(res), BinaryOp(+, Id(res), NumLit(2.0))))], AssignStmt(Id(res), BinaryOp(/, Id(res), NumLit(2.0))))), (BinaryOp(<, Id(i), NumLit(10.0)), Block([CallStmt(Id(print), [BinaryOp(%, Id(i), NumLit(2.0))]), AssignStmt(Id(res), Id(i))]))], Break)), Return(Id(res))])), FuncDecl(Id(main), [], Block([VarDecl(Id(n), NumberType, None, NumLit(123456.0)), CallStmt(Id(print), [CallExpr(Id(foo), [Id(n)])])]))])'
        self.assertTrue(TestAST.test(input, expect, 2062))
    
    def test_63(self):
        input = """
## Driver code 
func main()
begin
    string op
    number num1
    number num2
 
    ## It allows user to enter operator
    ## i.e. +, -, *, /
    readNumber(op)
 
    ## It allow user to enter the operands
    readNumber(num1) 
    readNumber(num2)
 
    ## If user enter +
    if (op == "+")
        writeNumber(num1 + num2)
 
    ## If user enter -
    elif (op == "-")
        writeNumber(num1 - num2)
 
    ## If user enter *
    elif (op == "*")
        writeNumber(num1 * num2)
 
    ## If user enter /
    elif (op == "/")
        writeNumber(num1 / num2)
 
    ## If the operator is other than +, -, * or /,
    ## error message will display
    else
        writeString("Error! operator is not correct")
end
"""
        expect = 'Program([FuncDecl(Id(main), [], Block([VarDecl(Id(op), StringType, None, None), VarDecl(Id(num1), NumberType, None, None), VarDecl(Id(num2), NumberType, None, None), CallStmt(Id(readNumber), [Id(op)]), CallStmt(Id(readNumber), [Id(num1)]), CallStmt(Id(readNumber), [Id(num2)]), If((BinaryOp(==, Id(op), StringLit(+)), CallStmt(Id(writeNumber), [BinaryOp(+, Id(num1), Id(num2))])), [(BinaryOp(==, Id(op), StringLit(-)), CallStmt(Id(writeNumber), [BinaryOp(-, Id(num1), Id(num2))])), (BinaryOp(==, Id(op), StringLit(*)), CallStmt(Id(writeNumber), [BinaryOp(*, Id(num1), Id(num2))])), (BinaryOp(==, Id(op), StringLit(/)), CallStmt(Id(writeNumber), [BinaryOp(/, Id(num1), Id(num2))]))], CallStmt(Id(writeString), [StringLit(Error! operator is not correct)]))]))])'
        self.assertTrue(TestAST.test(input, expect, 2063))
    
    def test_64(self):
        input = """
## Driver code 
func main()
begin
    number ord1
    number ord2
    number ord3
    number total_sum
 
    writeString("All the Armstrong numbers between 1 to 1000 : ")
   
    ## Loop which will run from 1 to 1000
    number num <- 1
    for num until num > 1000 by 1
    begin
        ## All the single-digit numbers are
        ## armstrong number.
        if (num <= 9)
        begin
            writeString(num ... " ")
        end
        else
        begin
            ord1 <- num % 10
            ord2 <- (num % 100 - ord1) / 10
            ord3 <- (num % 1000 - ord2) / 100
 
            total_sum <- ((ord1 * ord1 * ord1) + (ord2 * ord2 * ord2) + (ord3 * ord3 * ord3))
            if (total_sum == num)
            begin
                writeString(num ... " ")
            end
        end
    end
end
"""
        expect = 'Program([FuncDecl(Id(main), [], Block([VarDecl(Id(ord1), NumberType, None, None), VarDecl(Id(ord2), NumberType, None, None), VarDecl(Id(ord3), NumberType, None, None), VarDecl(Id(total_sum), NumberType, None, None), CallStmt(Id(writeString), [StringLit(All the Armstrong numbers between 1 to 1000 : )]), VarDecl(Id(num), NumberType, None, NumLit(1.0)), For(Id(num), BinaryOp(>, Id(num), NumLit(1000.0)), NumLit(1.0), Block([If((BinaryOp(<=, Id(num), NumLit(9.0)), Block([CallStmt(Id(writeString), [BinaryOp(..., Id(num), StringLit( ))])])), [], Block([AssignStmt(Id(ord1), BinaryOp(%, Id(num), NumLit(10.0))), AssignStmt(Id(ord2), BinaryOp(/, BinaryOp(-, BinaryOp(%, Id(num), NumLit(100.0)), Id(ord1)), NumLit(10.0))), AssignStmt(Id(ord3), BinaryOp(/, BinaryOp(-, BinaryOp(%, Id(num), NumLit(1000.0)), Id(ord2)), NumLit(100.0))), AssignStmt(Id(total_sum), BinaryOp(+, BinaryOp(+, BinaryOp(*, BinaryOp(*, Id(ord1), Id(ord1)), Id(ord1)), BinaryOp(*, BinaryOp(*, Id(ord2), Id(ord2)), Id(ord2))), BinaryOp(*, BinaryOp(*, Id(ord3), Id(ord3)), Id(ord3)))), If((BinaryOp(==, Id(total_sum), Id(num)), Block([CallStmt(Id(writeString), [BinaryOp(..., Id(num), StringLit( ))])])), [], None)]))]))]))])'
        self.assertTrue(TestAST.test(input, expect, 2064))
    
    def test_65(self):
        input = """
## Driver code 
func main()
begin
    number n <- 5
    number rows
    number columns
    ## for loop is used to identify the number of rows and
    ## it is used to print upper triangle
    rows <- 1
    for rows until rows > n by 1 begin
        ## used for printing the spaces
        columns <- n
        for columns until columns <= rows by -1 begin
            writeString(" ")
        end
        ## print star
        writeString("*")
        ## again print the spaces
        columns <- 1
        for columns until columns >= (rows - 1) * 2 by 1
        begin
            writeString(" ")
        end
        if (rows == 1) begin
            writeString("\\\\n")
        end
        else begin
            writeString("*\\\\n")
        end
    end
    ## for loop is used to identify the number of rows and
    ## it is used to print lower triangle
    rows <- n - 1
    for rows until rows < 1 by -1 begin
        ## used for printing the spaces
        columns <- n
        for columns until columns <= rows by -1 begin
            writeString(" ")
        end
        ## print star
        writeString("*")
        columns <- 1
        for columns until columns >= (rows - 1) * 2 by 1
        begin
            writeString(" ")
        end
        if (rows == 1) begin
            writeString("\\\\n")
        end
        else begin
            writeString("*\\\\n")
        end
    end
end
"""
        expect = 'Program([FuncDecl(Id(main), [], Block([VarDecl(Id(n), NumberType, None, NumLit(5.0)), VarDecl(Id(rows), NumberType, None, None), VarDecl(Id(columns), NumberType, None, None), AssignStmt(Id(rows), NumLit(1.0)), For(Id(rows), BinaryOp(>, Id(rows), Id(n)), NumLit(1.0), Block([AssignStmt(Id(columns), Id(n)), For(Id(columns), BinaryOp(<=, Id(columns), Id(rows)), UnaryOp(-, NumLit(1.0)), Block([CallStmt(Id(writeString), [StringLit( )])])), CallStmt(Id(writeString), [StringLit(*)]), AssignStmt(Id(columns), NumLit(1.0)), For(Id(columns), BinaryOp(>=, Id(columns), BinaryOp(*, BinaryOp(-, Id(rows), NumLit(1.0)), NumLit(2.0))), NumLit(1.0), Block([CallStmt(Id(writeString), [StringLit( )])])), If((BinaryOp(==, Id(rows), NumLit(1.0)), Block([CallStmt(Id(writeString), [StringLit(\\\\n)])])), [], Block([CallStmt(Id(writeString), [StringLit(*\\\\n)])]))])), AssignStmt(Id(rows), BinaryOp(-, Id(n), NumLit(1.0))), For(Id(rows), BinaryOp(<, Id(rows), NumLit(1.0)), UnaryOp(-, NumLit(1.0)), Block([AssignStmt(Id(columns), Id(n)), For(Id(columns), BinaryOp(<=, Id(columns), Id(rows)), UnaryOp(-, NumLit(1.0)), Block([CallStmt(Id(writeString), [StringLit( )])])), CallStmt(Id(writeString), [StringLit(*)]), AssignStmt(Id(columns), NumLit(1.0)), For(Id(columns), BinaryOp(>=, Id(columns), BinaryOp(*, BinaryOp(-, Id(rows), NumLit(1.0)), NumLit(2.0))), NumLit(1.0), Block([CallStmt(Id(writeString), [StringLit( )])])), If((BinaryOp(==, Id(rows), NumLit(1.0)), Block([CallStmt(Id(writeString), [StringLit(\\\\n)])])), [], Block([CallStmt(Id(writeString), [StringLit(*\\\\n)])]))]))]))])'
        self.assertTrue(TestAST.test(input, expect, 2065))
    
    def test_66(self):
        input = """
func printReverseFloyd(number n) 
begin 
    number curr_val <- n * (n + 1) / 2
    number i <- n 
    for i until i < 1 by -1
    begin 
        number j <- i
        for j until j < 1 by -1
        begin 
            writeString((curr_val-1) ... "  ")
        end 
  
        writeString("\\\\n")
    end 
end 
  
## Driver's Code 
func main() 
begin 
    number n <- 7 
    printReverseFloyd(n) 
end 
"""
        expect = 'Program([FuncDecl(Id(printReverseFloyd), [VarDecl(Id(n), NumberType, None, None)], Block([VarDecl(Id(curr_val), NumberType, None, BinaryOp(/, BinaryOp(*, Id(n), BinaryOp(+, Id(n), NumLit(1.0))), NumLit(2.0))), VarDecl(Id(i), NumberType, None, Id(n)), For(Id(i), BinaryOp(<, Id(i), NumLit(1.0)), UnaryOp(-, NumLit(1.0)), Block([VarDecl(Id(j), NumberType, None, Id(i)), For(Id(j), BinaryOp(<, Id(j), NumLit(1.0)), UnaryOp(-, NumLit(1.0)), Block([CallStmt(Id(writeString), [BinaryOp(..., BinaryOp(-, Id(curr_val), NumLit(1.0)), StringLit(  ))])])), CallStmt(Id(writeString), [StringLit(\\\\n)])]))])), FuncDecl(Id(main), [], Block([VarDecl(Id(n), NumberType, None, NumLit(7.0)), CallStmt(Id(printReverseFloyd), [Id(n)])]))])'
        self.assertTrue(TestAST.test(input, expect, 2066))
    
    def test_67(self):
        input = """
func print_patt(number R)
begin
    ## To iterate through the rows
    number i <- 1
    for i until i > R by 1
    begin
        ## To print the  beginning spaces 
        number sp <- 1 
        for sp until sp > i - 1 by 1
        begin
            writeString(" ")
        end
       
        ## Iterating from ith column to
        ## last column (R*2 - (2*i - 1))
        number last_col <- (R * 2 - (2 * i - 1))
            
        ## To iterate through column
        number j <- 1
        for j until j > last_col by 1
        begin
            ## To Print all star for first 
            ## row (i==1) ith column (j==1) 
            ## and for last column 
            ## (R*2 - (2*i - 1))
            if(i == 1)
                writeString("*")
            elif(j == 1)
                writeString("*")
            elif(j == last_col)
                writeString("*")
            else
                writeString(" ")
        end
         
    ## After printing a row proceed 
    ## to the next row
    writeString("\\\\n")
    end
end
  
## Driver's Code 
func main() 
begin 
    number n <- 7 
    print_patt(n) 
end 
"""
        expect = 'Program([FuncDecl(Id(print_patt), [VarDecl(Id(R), NumberType, None, None)], Block([VarDecl(Id(i), NumberType, None, NumLit(1.0)), For(Id(i), BinaryOp(>, Id(i), Id(R)), NumLit(1.0), Block([VarDecl(Id(sp), NumberType, None, NumLit(1.0)), For(Id(sp), BinaryOp(>, Id(sp), BinaryOp(-, Id(i), NumLit(1.0))), NumLit(1.0), Block([CallStmt(Id(writeString), [StringLit( )])])), VarDecl(Id(last_col), NumberType, None, BinaryOp(-, BinaryOp(*, Id(R), NumLit(2.0)), BinaryOp(-, BinaryOp(*, NumLit(2.0), Id(i)), NumLit(1.0)))), VarDecl(Id(j), NumberType, None, NumLit(1.0)), For(Id(j), BinaryOp(>, Id(j), Id(last_col)), NumLit(1.0), Block([If((BinaryOp(==, Id(i), NumLit(1.0)), CallStmt(Id(writeString), [StringLit(*)])), [(BinaryOp(==, Id(j), NumLit(1.0)), CallStmt(Id(writeString), [StringLit(*)])), (BinaryOp(==, Id(j), Id(last_col)), CallStmt(Id(writeString), [StringLit(*)]))], CallStmt(Id(writeString), [StringLit( )]))])), CallStmt(Id(writeString), [StringLit(\\\\n)])]))])), FuncDecl(Id(main), [], Block([VarDecl(Id(n), NumberType, None, NumLit(7.0)), CallStmt(Id(print_patt), [Id(n)])]))])'
        self.assertTrue(TestAST.test(input, expect, 2067))
    
    def test_68(self):
        input = """
func binomialCoeff(number n, number k) 
  
## Function to print first 
## n lines of Pascal's  
## Triangle 

func printPascal(number n) 
begin 
    ## Iterate through every line and 
    ## print entries in it 
    number line <- 0 
    for line until line >= n by 1
    begin 
        ## Every line has number of  
        ## integers equal to line  
        ## number 
        number i <- 0
        for i until i > line by 1 
            writeString(" "...binomialCoeff(line, i))
        writeString("\\\\n") 
    end 
end 
  
func binomialCoeff(number n, number k) 
begin 
    number res <- 1 
    if (k > n - k) 
        k <- n - k 
    number i <- 0
    for i until i >= k by 1 
    begin 
        res <- res * (n - i) 
        res <- res / (i + 1) 
    end 
      
    return res 
end 
  
## Driver program  
func main() 
begin 
    number n <- 7 
    printPascal(n) 
end 
"""
        expect = 'Program([FuncDecl(Id(binomialCoeff), [VarDecl(Id(n), NumberType, None, None), VarDecl(Id(k), NumberType, None, None)], None), FuncDecl(Id(printPascal), [VarDecl(Id(n), NumberType, None, None)], Block([VarDecl(Id(line), NumberType, None, NumLit(0.0)), For(Id(line), BinaryOp(>=, Id(line), Id(n)), NumLit(1.0), Block([VarDecl(Id(i), NumberType, None, NumLit(0.0)), For(Id(i), BinaryOp(>, Id(i), Id(line)), NumLit(1.0), CallStmt(Id(writeString), [BinaryOp(..., StringLit( ), CallExpr(Id(binomialCoeff), [Id(line), Id(i)]))])), CallStmt(Id(writeString), [StringLit(\\\\n)])]))])), FuncDecl(Id(binomialCoeff), [VarDecl(Id(n), NumberType, None, None), VarDecl(Id(k), NumberType, None, None)], Block([VarDecl(Id(res), NumberType, None, NumLit(1.0)), If((BinaryOp(>, Id(k), BinaryOp(-, Id(n), Id(k))), AssignStmt(Id(k), BinaryOp(-, Id(n), Id(k)))), [], None), VarDecl(Id(i), NumberType, None, NumLit(0.0)), For(Id(i), BinaryOp(>=, Id(i), Id(k)), NumLit(1.0), Block([AssignStmt(Id(res), BinaryOp(*, Id(res), BinaryOp(-, Id(n), Id(i)))), AssignStmt(Id(res), BinaryOp(/, Id(res), BinaryOp(+, Id(i), NumLit(1.0))))])), Return(Id(res))])), FuncDecl(Id(main), [], Block([VarDecl(Id(n), NumberType, None, NumLit(7.0)), CallStmt(Id(printPascal), [Id(n)])]))])'
        self.assertTrue(TestAST.test(input, expect, 2068))
    
    def test_69(self):
        input = """
func printPascal() 
begin 
      
    ## An auxiliary array to store  
    ## generated pascal triangle values 
    number arr[10,10]  
  
    ## Iterate through every line and  
    ## print integer(s) in it 
    number line <- 0
    for line until line >= 10 by 1
    begin 
        ## Every line has number of integers  
        ## equal to line number 
        number i <- 0 
        for i until i > line by 1
        begin 
            ## First and last values in every row are 1 
            if ((line == i) or( i == 0)) 
                arr[line,i] <- 1 
            ## Other values are sum of values just  
            ## above and left of above 
            else
                arr[line,i] <- arr[line - 1,i - 1] + arr[line - 1,i] 
            writeString(arr[line,i] ... " " )
        end 
        writeString("\\\\n")
    end 
end 
  
## Driver code 
func main() 
begin 
    printPascal() 
end 
"""
        expect = 'Program([FuncDecl(Id(printPascal), [], Block([VarDecl(Id(arr), ArrayType([10.0, 10.0], NumberType), None, None), VarDecl(Id(line), NumberType, None, NumLit(0.0)), For(Id(line), BinaryOp(>=, Id(line), NumLit(10.0)), NumLit(1.0), Block([VarDecl(Id(i), NumberType, None, NumLit(0.0)), For(Id(i), BinaryOp(>, Id(i), Id(line)), NumLit(1.0), Block([If((BinaryOp(or, BinaryOp(==, Id(line), Id(i)), BinaryOp(==, Id(i), NumLit(0.0))), AssignStmt(ArrayCell(Id(arr), [Id(line), Id(i)]), NumLit(1.0))), [], AssignStmt(ArrayCell(Id(arr), [Id(line), Id(i)]), BinaryOp(+, ArrayCell(Id(arr), [BinaryOp(-, Id(line), NumLit(1.0)), BinaryOp(-, Id(i), NumLit(1.0))]), ArrayCell(Id(arr), [BinaryOp(-, Id(line), NumLit(1.0)), Id(i)])))), CallStmt(Id(writeString), [BinaryOp(..., ArrayCell(Id(arr), [Id(line), Id(i)]), StringLit( ))])])), CallStmt(Id(writeString), [StringLit(\\\\n)])]))])), FuncDecl(Id(main), [], Block([CallStmt(Id(printPascal), [])]))])'
        self.assertTrue(TestAST.test(input, expect, 2069))
    
    def test_70(self):
        input = """
func reverse(string str, number index, number n)  
begin 
    if(index == n)      ## return if we reached at last index or at the end of the string 
        return 
    string temp <- str[index]    ## storing each character starting from index 0 in function call stack 
    reverse(str, index+1, n)  ## calling recursive function by increasing index everytime 
    writeString(temp)              ## printing each stored character while recurring back 
end 
"""
        expect = 'Program([FuncDecl(Id(reverse), [VarDecl(Id(str), StringType, None, None), VarDecl(Id(index), NumberType, None, None), VarDecl(Id(n), NumberType, None, None)], Block([If((BinaryOp(==, Id(index), Id(n)), Return()), [], None), VarDecl(Id(temp), StringType, None, ArrayCell(Id(str), [Id(index)])), CallStmt(Id(reverse), [Id(str), BinaryOp(+, Id(index), NumLit(1.0)), Id(n)]), CallStmt(Id(writeString), [Id(temp)])]))])'
        self.assertTrue(TestAST.test(input, expect, 2070))
    
    def test_71(self):
        '''Selection sort'''
        input = """
##Swap function 
func swap(number xp, number yp)  
begin  
    number temp <- xp  
    xp <- yp  
    yp <- temp  
end  
  
func selectionSort(number arr, number n)  
begin  
    number i
    number j
    number min_idx  
  
    ## One by one move boundary of  
    ## unsorted subarray  
    i <- 0
    for i until i >= n-1 by 1 
    begin  
        
        ## Find the minimum element in  
        ## unsorted array  
        min_idx <- i  
        j <- i+1
        for j until j >= n by 1
        if (arr[j] < arr[min_idx])  
            min_idx <- j  
  
        ## Swap the found minimum element  
        ## with the first element  
        swap(arr[min_idx], arr[i])  
    end  
end  
  
##Function to print an array 
func printArray(number arr, number size)  
begin  
    number i <- 0
    for i until i >= size by 1 
        writeString(arr[i] ... " ")  
    writeString("\\\\n")  
end  
  
## Driver program to test above functions  
func main()  
begin  
    number arr[8] <- [64, 25, 12, 22, 11, 33, 69, 42]  
    selectionSort(arr, 8)  
    writeString("Sorted array: ")  
    printArray(arr, 8)  
end  
"""
        expect = 'Program([FuncDecl(Id(swap), [VarDecl(Id(xp), NumberType, None, None), VarDecl(Id(yp), NumberType, None, None)], Block([VarDecl(Id(temp), NumberType, None, Id(xp)), AssignStmt(Id(xp), Id(yp)), AssignStmt(Id(yp), Id(temp))])), FuncDecl(Id(selectionSort), [VarDecl(Id(arr), NumberType, None, None), VarDecl(Id(n), NumberType, None, None)], Block([VarDecl(Id(i), NumberType, None, None), VarDecl(Id(j), NumberType, None, None), VarDecl(Id(min_idx), NumberType, None, None), AssignStmt(Id(i), NumLit(0.0)), For(Id(i), BinaryOp(>=, Id(i), BinaryOp(-, Id(n), NumLit(1.0))), NumLit(1.0), Block([AssignStmt(Id(min_idx), Id(i)), AssignStmt(Id(j), BinaryOp(+, Id(i), NumLit(1.0))), For(Id(j), BinaryOp(>=, Id(j), Id(n)), NumLit(1.0), If((BinaryOp(<, ArrayCell(Id(arr), [Id(j)]), ArrayCell(Id(arr), [Id(min_idx)])), AssignStmt(Id(min_idx), Id(j))), [], None)), CallStmt(Id(swap), [ArrayCell(Id(arr), [Id(min_idx)]), ArrayCell(Id(arr), [Id(i)])])]))])), FuncDecl(Id(printArray), [VarDecl(Id(arr), NumberType, None, None), VarDecl(Id(size), NumberType, None, None)], Block([VarDecl(Id(i), NumberType, None, NumLit(0.0)), For(Id(i), BinaryOp(>=, Id(i), Id(size)), NumLit(1.0), CallStmt(Id(writeString), [BinaryOp(..., ArrayCell(Id(arr), [Id(i)]), StringLit( ))])), CallStmt(Id(writeString), [StringLit(\\\\n)])])), FuncDecl(Id(main), [], Block([VarDecl(Id(arr), ArrayType([8.0], NumberType), None, ArrayLit(NumLit(64.0), NumLit(25.0), NumLit(12.0), NumLit(22.0), NumLit(11.0), NumLit(33.0), NumLit(69.0), NumLit(42.0))), CallStmt(Id(selectionSort), [Id(arr), NumLit(8.0)]), CallStmt(Id(writeString), [StringLit(Sorted array: )]), CallStmt(Id(printArray), [Id(arr), NumLit(8.0)])]))])'
        self.assertTrue(TestAST.test(input, expect, 2071))
    
    def test_72(self):
        '''Bubble sort'''
        input = """
## Swap function
func swap(number a, number b)
begin
    number temp <- a
    a <- b
    b <- temp
end
 
## An optimized version of Bubble Sort
func bubbleSort(number arr, number n)
begin
    ## swapped variable to signal if there is a
    ## swap happened in the inner loop
    ## initially set to false
    number i <- 0
    for i until i >= n - 1 by 1 begin
        ## swapped is initialized as false at the start
        bool swapped <- false
        number j <- 0
        for j until j >= n - i - 1 by 1 begin
            if (arr[j] > arr[j + 1]) begin
                swap(arr + j, arr + j + 1)
                ## swapped is set to true if the swap is
                ## done
                swapped <- true
            end
        end
 
        ## If no two elements were swapped
        ## by inner loop, then break
        if (swapped == false)
            break
    end
end
 
## Function to print an array
func printArray(number arr, number size)
begin
    number i <- 0
    for i until i >= size by 1
        writeString(arr[i])
end
 
## Driver code
func main()
begin
    number arr[8] <- [5, 3, 1, 9, 8, 2, 4, 7]
 
    ## bubbleSort function called
    bubbleSort(arr, 8)
 
    writeString("Sorted array: ")
    printArray(arr, 8)
end
"""
        expect = 'Program([FuncDecl(Id(swap), [VarDecl(Id(a), NumberType, None, None), VarDecl(Id(b), NumberType, None, None)], Block([VarDecl(Id(temp), NumberType, None, Id(a)), AssignStmt(Id(a), Id(b)), AssignStmt(Id(b), Id(temp))])), FuncDecl(Id(bubbleSort), [VarDecl(Id(arr), NumberType, None, None), VarDecl(Id(n), NumberType, None, None)], Block([VarDecl(Id(i), NumberType, None, NumLit(0.0)), For(Id(i), BinaryOp(>=, Id(i), BinaryOp(-, Id(n), NumLit(1.0))), NumLit(1.0), Block([VarDecl(Id(swapped), BoolType, None, BooleanLit(False)), VarDecl(Id(j), NumberType, None, NumLit(0.0)), For(Id(j), BinaryOp(>=, Id(j), BinaryOp(-, BinaryOp(-, Id(n), Id(i)), NumLit(1.0))), NumLit(1.0), Block([If((BinaryOp(>, ArrayCell(Id(arr), [Id(j)]), ArrayCell(Id(arr), [BinaryOp(+, Id(j), NumLit(1.0))])), Block([CallStmt(Id(swap), [BinaryOp(+, Id(arr), Id(j)), BinaryOp(+, BinaryOp(+, Id(arr), Id(j)), NumLit(1.0))]), AssignStmt(Id(swapped), BooleanLit(True))])), [], None)])), If((BinaryOp(==, Id(swapped), BooleanLit(False)), Break), [], None)]))])), FuncDecl(Id(printArray), [VarDecl(Id(arr), NumberType, None, None), VarDecl(Id(size), NumberType, None, None)], Block([VarDecl(Id(i), NumberType, None, NumLit(0.0)), For(Id(i), BinaryOp(>=, Id(i), Id(size)), NumLit(1.0), CallStmt(Id(writeString), [ArrayCell(Id(arr), [Id(i)])]))])), FuncDecl(Id(main), [], Block([VarDecl(Id(arr), ArrayType([8.0], NumberType), None, ArrayLit(NumLit(5.0), NumLit(3.0), NumLit(1.0), NumLit(9.0), NumLit(8.0), NumLit(2.0), NumLit(4.0), NumLit(7.0))), CallStmt(Id(bubbleSort), [Id(arr), NumLit(8.0)]), CallStmt(Id(writeString), [StringLit(Sorted array: )]), CallStmt(Id(printArray), [Id(arr), NumLit(8.0)])]))])'
        self.assertTrue(TestAST.test(input, expect, 2072))
    
    def test_73(self):
        input = """
## Prints roots of quadratic equation
## ax*2 + bx + x
func findRoots(number a, number b, number c)
begin
    ## If a is 0, then equation is
    ## not quadratic, but linear
    if (a == 0) begin
        writeString("Invalid")
        return
    end
 
    number d <- b * b - 4 * a * c
    number sqrt_val <- sqrt(abs(d))
 
    if (d > 0) begin
        writeString("Roots are real and different ")
        writeString((str((-b + sqrt_val) / (2 * a)) ... " ") ... str((-b - sqrt_val) / (2 * a)))
    end
    else if (d == 0) begin
        writeString("Roots are real and same ")
        writeNumber(-b / (2 * a))
    end
 
    ## d < 0
    else begin
        writeString("Roots are complex ")
        writeString((((((str(-b / (2 * a)) ... " + i") ... str(sqrt_val / (2 * a))) ... " ") ... str(-b / (2 * a))) ... " - i") ... str(sqrt_val / (2 * a)))
    end
end
 
## Driver code
func main()
begin
    number a <- 1
    number b <- -7
    number c <- 12
 
    ## Function call
    findRoots(a, b, c)
end
"""
        expect = 'Program([FuncDecl(Id(findRoots), [VarDecl(Id(a), NumberType, None, None), VarDecl(Id(b), NumberType, None, None), VarDecl(Id(c), NumberType, None, None)], Block([If((BinaryOp(==, Id(a), NumLit(0.0)), Block([CallStmt(Id(writeString), [StringLit(Invalid)]), Return()])), [], None), VarDecl(Id(d), NumberType, None, BinaryOp(-, BinaryOp(*, Id(b), Id(b)), BinaryOp(*, BinaryOp(*, NumLit(4.0), Id(a)), Id(c)))), VarDecl(Id(sqrt_val), NumberType, None, CallExpr(Id(sqrt), [CallExpr(Id(abs), [Id(d)])])), If((BinaryOp(>, Id(d), NumLit(0.0)), Block([CallStmt(Id(writeString), [StringLit(Roots are real and different )]), CallStmt(Id(writeString), [BinaryOp(..., BinaryOp(..., CallExpr(Id(str), [BinaryOp(/, BinaryOp(+, UnaryOp(-, Id(b)), Id(sqrt_val)), BinaryOp(*, NumLit(2.0), Id(a)))]), StringLit( )), CallExpr(Id(str), [BinaryOp(/, BinaryOp(-, UnaryOp(-, Id(b)), Id(sqrt_val)), BinaryOp(*, NumLit(2.0), Id(a)))]))])])), [], If((BinaryOp(==, Id(d), NumLit(0.0)), Block([CallStmt(Id(writeString), [StringLit(Roots are real and same )]), CallStmt(Id(writeNumber), [BinaryOp(/, UnaryOp(-, Id(b)), BinaryOp(*, NumLit(2.0), Id(a)))])])), [], Block([CallStmt(Id(writeString), [StringLit(Roots are complex )]), CallStmt(Id(writeString), [BinaryOp(..., BinaryOp(..., BinaryOp(..., BinaryOp(..., BinaryOp(..., BinaryOp(..., CallExpr(Id(str), [BinaryOp(/, UnaryOp(-, Id(b)), BinaryOp(*, NumLit(2.0), Id(a)))]), StringLit( + i)), CallExpr(Id(str), [BinaryOp(/, Id(sqrt_val), BinaryOp(*, NumLit(2.0), Id(a)))])), StringLit( )), CallExpr(Id(str), [BinaryOp(/, UnaryOp(-, Id(b)), BinaryOp(*, NumLit(2.0), Id(a)))])), StringLit( - i)), CallExpr(Id(str), [BinaryOp(/, Id(sqrt_val), BinaryOp(*, NumLit(2.0), Id(a)))]))])])))])), FuncDecl(Id(main), [], Block([VarDecl(Id(a), NumberType, None, NumLit(1.0)), VarDecl(Id(b), NumberType, None, UnaryOp(-, NumLit(7.0))), VarDecl(Id(c), NumberType, None, NumLit(12.0)), CallStmt(Id(findRoots), [Id(a), Id(b), Id(c)])]))])'
        self.assertTrue(TestAST.test(input, expect, 2073))
    
    def test_74(self):
        input = """
## Function to print string  
## in sorted order 
func sortString(string str) 
begin 
    ## Hash array to keep count of characters. 
    ## Initially count of all characters is  
    ## initialized to zero
    number charCount[26] <- [0] 
      
    ## Traverse string and increment  
    ## count of characters 
    number i <- 0
    for i until i >= length(str) by 1
  
        ## 'a'-'a' will be 0, 'b'-'a' will be 1, 
        ## so for location of character in count  
        ## array we will do str[i]-'a'
        charCount[str[i]-"a"] <- charCount[str[i]-"a"] + 1
      
    ## Traverse the hash array and print  
    ## characters 
    number i <- 0
    for i until i >= 26 by 1 
    begin
        number j <- 0
        for j until j >= charCount[i] by 1
            writeString("a"...str(i)) 
    end
end 
"""
        expect = 'Program([FuncDecl(Id(sortString), [VarDecl(Id(str), StringType, None, None)], Block([VarDecl(Id(charCount), ArrayType([26.0], NumberType), None, ArrayLit(NumLit(0.0))), VarDecl(Id(i), NumberType, None, NumLit(0.0)), For(Id(i), BinaryOp(>=, Id(i), CallExpr(Id(length), [Id(str)])), NumLit(1.0), AssignStmt(ArrayCell(Id(charCount), [BinaryOp(-, ArrayCell(Id(str), [Id(i)]), StringLit(a))]), BinaryOp(+, ArrayCell(Id(charCount), [BinaryOp(-, ArrayCell(Id(str), [Id(i)]), StringLit(a))]), NumLit(1.0)))), VarDecl(Id(i), NumberType, None, NumLit(0.0)), For(Id(i), BinaryOp(>=, Id(i), NumLit(26.0)), NumLit(1.0), Block([VarDecl(Id(j), NumberType, None, NumLit(0.0)), For(Id(j), BinaryOp(>=, Id(j), ArrayCell(Id(charCount), [Id(i)])), NumLit(1.0), CallStmt(Id(writeString), [BinaryOp(..., StringLit(a), CallExpr(Id(str), [Id(i)]))]))]))]))])'
        self.assertTrue(TestAST.test(input, expect, 2074))

    def test_75(self):
        '''Row-wise sort for 2D array'''
        input = """
func sortRowWise(number m, number r, number c)
begin
    ## Loop for rows of matrix
    number i <- 0
    for i until i >= r by 1
    begin
        ## Loop for column of matrix
        number j <- 0
        for j until j >= c by 1
        begin
            ## Loop for comparison and swapping
            number k <- 0
            for k until k >= c - j - 1 by 1
            begin
                if (m[i,k] > m[i,k + 1]) 
                begin
                    ## Swapping of elements
                    swap(m[i,k], m[i,k + 1])
                end
            end
        end
    end
 
    ## Printing the sorted matrix
    number i <- 0
    for i until i >= r by 1 
    begin
        number j <- 0
        for j until j >= c by 1
            writeString(m[i,j] ... " ")
        writeString("\\\\n")
    end
end
 
## Driver code
func main()
begin
    number m[4,4] <- [[9, 8, 7, 1], [7, 3, 0, 2], [9, 5, 3, 2], [6, 3, 1, 2]]
    sortRowWise(m, 4, 4)
end
"""
        expect = 'Program([FuncDecl(Id(sortRowWise), [VarDecl(Id(m), NumberType, None, None), VarDecl(Id(r), NumberType, None, None), VarDecl(Id(c), NumberType, None, None)], Block([VarDecl(Id(i), NumberType, None, NumLit(0.0)), For(Id(i), BinaryOp(>=, Id(i), Id(r)), NumLit(1.0), Block([VarDecl(Id(j), NumberType, None, NumLit(0.0)), For(Id(j), BinaryOp(>=, Id(j), Id(c)), NumLit(1.0), Block([VarDecl(Id(k), NumberType, None, NumLit(0.0)), For(Id(k), BinaryOp(>=, Id(k), BinaryOp(-, BinaryOp(-, Id(c), Id(j)), NumLit(1.0))), NumLit(1.0), Block([If((BinaryOp(>, ArrayCell(Id(m), [Id(i), Id(k)]), ArrayCell(Id(m), [Id(i), BinaryOp(+, Id(k), NumLit(1.0))])), Block([CallStmt(Id(swap), [ArrayCell(Id(m), [Id(i), Id(k)]), ArrayCell(Id(m), [Id(i), BinaryOp(+, Id(k), NumLit(1.0))])])])), [], None)]))]))])), VarDecl(Id(i), NumberType, None, NumLit(0.0)), For(Id(i), BinaryOp(>=, Id(i), Id(r)), NumLit(1.0), Block([VarDecl(Id(j), NumberType, None, NumLit(0.0)), For(Id(j), BinaryOp(>=, Id(j), Id(c)), NumLit(1.0), CallStmt(Id(writeString), [BinaryOp(..., ArrayCell(Id(m), [Id(i), Id(j)]), StringLit( ))])), CallStmt(Id(writeString), [StringLit(\\\\n)])]))])), FuncDecl(Id(main), [], Block([VarDecl(Id(m), ArrayType([4.0, 4.0], NumberType), None, ArrayLit(ArrayLit(NumLit(9.0), NumLit(8.0), NumLit(7.0), NumLit(1.0)), ArrayLit(NumLit(7.0), NumLit(3.0), NumLit(0.0), NumLit(2.0)), ArrayLit(NumLit(9.0), NumLit(5.0), NumLit(3.0), NumLit(2.0)), ArrayLit(NumLit(6.0), NumLit(3.0), NumLit(1.0), NumLit(2.0)))), CallStmt(Id(sortRowWise), [Id(m), NumLit(4.0), NumLit(4.0)])]))])'
        self.assertTrue(TestAST.test(input, expect, 2075))
    
    def test_76(self):
        '''Linear search'''
        input = """
func search(number arr, number n, number x)
begin
    number i <- 0
    for i until i >= n by 1
        if (arr[i] == x)
            return i
    return -1
end
 
## Driver code
func main()
begin
    number arr[5] <- [2, 3, 4, 10, 40]
    number x <- 10
   
    number result <- search(arr, 5, x)
    if (result == -1) 
        writeString("Element is not present in array" )
    else
        writeString("Element is present at index " ... str(result))
end
"""
        expect = 'Program([FuncDecl(Id(search), [VarDecl(Id(arr), NumberType, None, None), VarDecl(Id(n), NumberType, None, None), VarDecl(Id(x), NumberType, None, None)], Block([VarDecl(Id(i), NumberType, None, NumLit(0.0)), For(Id(i), BinaryOp(>=, Id(i), Id(n)), NumLit(1.0), If((BinaryOp(==, ArrayCell(Id(arr), [Id(i)]), Id(x)), Return(Id(i))), [], None)), Return(UnaryOp(-, NumLit(1.0)))])), FuncDecl(Id(main), [], Block([VarDecl(Id(arr), ArrayType([5.0], NumberType), None, ArrayLit(NumLit(2.0), NumLit(3.0), NumLit(4.0), NumLit(10.0), NumLit(40.0))), VarDecl(Id(x), NumberType, None, NumLit(10.0)), VarDecl(Id(result), NumberType, None, CallExpr(Id(search), [Id(arr), NumLit(5.0), Id(x)])), If((BinaryOp(==, Id(result), UnaryOp(-, NumLit(1.0))), CallStmt(Id(writeString), [StringLit(Element is not present in array)])), [], CallStmt(Id(writeString), [BinaryOp(..., StringLit(Element is present at index ), CallExpr(Id(str), [Id(result)]))]))]))])'
        self.assertTrue(TestAST.test(input, expect, 2076))
    
    def test_77(self):
        '''Binary search'''
        input = """
func binarySearch(number arr, number low, number high, number x) 
begin 
    ## Base case: If the search space becomes empty, the 
    ## element is not present in the array 
    if (high >= low) begin 
        ## Calculate the middle index to divide the search 
        ## space in half 
        number mid <- low + (high - low) / 2 
  
        ## If the middle element is equal to 'x', we have 
        ## found the element, return its index 
        if (arr[mid] == x) 
            return mid 
  
        ## If the middle element is greater than 'x', search 
        ## in the left half of the array 
        if (arr[mid] > x) 
            return binarySearch(arr, low, mid - 1, x) 
  
        ## If the middle element is less than 'x', search in 
        ## the right half of the array 
        return binarySearch(arr, mid + 1, high, x) 
    end 
  
    ## If the base case is reached, the element is not 
    ## present in the array, return -1 
    return -1 
end 
  
## Driver code 
func main() 
begin 
    number arr[5] <- [2, 3, 4, 10, 40]
    number x <- 10
   
    number result <- search(arr, 5, x)
    if (result == -1) 
        writeString("Element is not present in array" )
    else
        writeString("Element is present at index " ... str(result))
end
"""
        expect = 'Program([FuncDecl(Id(binarySearch), [VarDecl(Id(arr), NumberType, None, None), VarDecl(Id(low), NumberType, None, None), VarDecl(Id(high), NumberType, None, None), VarDecl(Id(x), NumberType, None, None)], Block([If((BinaryOp(>=, Id(high), Id(low)), Block([VarDecl(Id(mid), NumberType, None, BinaryOp(+, Id(low), BinaryOp(/, BinaryOp(-, Id(high), Id(low)), NumLit(2.0)))), If((BinaryOp(==, ArrayCell(Id(arr), [Id(mid)]), Id(x)), Return(Id(mid))), [], None), If((BinaryOp(>, ArrayCell(Id(arr), [Id(mid)]), Id(x)), Return(CallExpr(Id(binarySearch), [Id(arr), Id(low), BinaryOp(-, Id(mid), NumLit(1.0)), Id(x)]))), [], None), Return(CallExpr(Id(binarySearch), [Id(arr), BinaryOp(+, Id(mid), NumLit(1.0)), Id(high), Id(x)]))])), [], None), Return(UnaryOp(-, NumLit(1.0)))])), FuncDecl(Id(main), [], Block([VarDecl(Id(arr), ArrayType([5.0], NumberType), None, ArrayLit(NumLit(2.0), NumLit(3.0), NumLit(4.0), NumLit(10.0), NumLit(40.0))), VarDecl(Id(x), NumberType, None, NumLit(10.0)), VarDecl(Id(result), NumberType, None, CallExpr(Id(search), [Id(arr), NumLit(5.0), Id(x)])), If((BinaryOp(==, Id(result), UnaryOp(-, NumLit(1.0))), CallStmt(Id(writeString), [StringLit(Element is not present in array)])), [], CallStmt(Id(writeString), [BinaryOp(..., StringLit(Element is present at index ), CallExpr(Id(str), [Id(result)]))]))]))])'
        self.assertTrue(TestAST.test(input, expect, 2077))
    
    def test_78(self):
        input = """
## Works only if a >= 0  
## and b >= 0  
func pow(number a, number b)  
begin  
    if (b == 0)  
        return 1  
    number answer <- a  
    number increment <- a  
    number i
    number j  
    i <- 1
    for i until i >= b by 1  
    begin  
        j <- 1
        for j until j >= a by 1   
        begin  
            answer <- answer + increment  
        end  
        increment <- answer  
    end  
    return answer  
end  
  
## Driver Code 
func main()  
begin  
    writeNumber(pow(5, 3))
end  
"""
        expect = 'Program([FuncDecl(Id(pow), [VarDecl(Id(a), NumberType, None, None), VarDecl(Id(b), NumberType, None, None)], Block([If((BinaryOp(==, Id(b), NumLit(0.0)), Return(NumLit(1.0))), [], None), VarDecl(Id(answer), NumberType, None, Id(a)), VarDecl(Id(increment), NumberType, None, Id(a)), VarDecl(Id(i), NumberType, None, None), VarDecl(Id(j), NumberType, None, None), AssignStmt(Id(i), NumLit(1.0)), For(Id(i), BinaryOp(>=, Id(i), Id(b)), NumLit(1.0), Block([AssignStmt(Id(j), NumLit(1.0)), For(Id(j), BinaryOp(>=, Id(j), Id(a)), NumLit(1.0), Block([AssignStmt(Id(answer), BinaryOp(+, Id(answer), Id(increment)))])), AssignStmt(Id(increment), Id(answer))])), Return(Id(answer))])), FuncDecl(Id(main), [], Block([CallStmt(Id(writeNumber), [CallExpr(Id(pow), [NumLit(5.0), NumLit(3.0)])])]))])'
        self.assertTrue(TestAST.test(input, expect, 2078))
    
    def test_79(self):
        input = """ 
func multiply(number x, number y) 
begin 
    if(y) 
        return (x + multiply(x, y - 1)) 
    else
        return 0 
end 
  
## A recursive function to get a^b 
## Works only if a >= 0 and b >= 0 
func pow(number a, number b) 
begin 
    if(b) 
        return multiply(a, pow(a, b - 1)) 
    else
        return 1 
end  
  
## Driver Code 
func main() 
begin 
    writeNumber(pow(5, 3))
end 
"""
        expect = 'Program([FuncDecl(Id(multiply), [VarDecl(Id(x), NumberType, None, None), VarDecl(Id(y), NumberType, None, None)], Block([If((Id(y), Return(BinaryOp(+, Id(x), CallExpr(Id(multiply), [Id(x), BinaryOp(-, Id(y), NumLit(1.0))])))), [], Return(NumLit(0.0)))])), FuncDecl(Id(pow), [VarDecl(Id(a), NumberType, None, None), VarDecl(Id(b), NumberType, None, None)], Block([If((Id(b), Return(CallExpr(Id(multiply), [Id(a), CallExpr(Id(pow), [Id(a), BinaryOp(-, Id(b), NumLit(1.0))])]))), [], Return(NumLit(1.0)))])), FuncDecl(Id(main), [], Block([CallStmt(Id(writeNumber), [CallExpr(Id(pow), [NumLit(5.0), NumLit(3.0)])])]))])'
        self.assertTrue(TestAST.test(input, expect, 2079))
    
    def test_80(self):
        '''Bin to Dec'''
        input = """ 
## Function to convert binary 
## to decimal 
func binaryToDecimal(string n) 
begin 
    string num <- n 
    number dec_value <- 0 
  
    ## Initializing base value to 1, i.e 2^0 
    number base <- 1 
  
    number len <- length(num) 
    number i <- len - 1
    for i until i >= 0 by 1 begin 
        if (num[i] == "1") 
            dec_value <- dec_value + base 
        base <- base * 2 
    end 
  
    return dec_value 
end 
  
## Driver code 
func main() 
begin 
    string num <- "10101001" 
    writeNumber(binaryToDecimal(num))
end
"""
        expect = 'Program([FuncDecl(Id(binaryToDecimal), [VarDecl(Id(n), StringType, None, None)], Block([VarDecl(Id(num), StringType, None, Id(n)), VarDecl(Id(dec_value), NumberType, None, NumLit(0.0)), VarDecl(Id(base), NumberType, None, NumLit(1.0)), VarDecl(Id(len), NumberType, None, CallExpr(Id(length), [Id(num)])), VarDecl(Id(i), NumberType, None, BinaryOp(-, Id(len), NumLit(1.0))), For(Id(i), BinaryOp(>=, Id(i), NumLit(0.0)), NumLit(1.0), Block([If((BinaryOp(==, ArrayCell(Id(num), [Id(i)]), StringLit(1)), AssignStmt(Id(dec_value), BinaryOp(+, Id(dec_value), Id(base)))), [], None), AssignStmt(Id(base), BinaryOp(*, Id(base), NumLit(2.0)))])), Return(Id(dec_value))])), FuncDecl(Id(main), [], Block([VarDecl(Id(num), StringType, None, StringLit(10101001)), CallStmt(Id(writeNumber), [CallExpr(Id(binaryToDecimal), [Id(num)])])]))])'
        self.assertTrue(TestAST.test(input, expect, 2080))
    
    def test_81(self):
        '''Dec to Bin'''
        input = """ 
## Function to convert decimal
## to binary
func decToBinary(number n)
begin
    ## Array to store binary number
    number binaryNum[32]
 
    ## Counter for binary array
    number i <- 0
    for n until n <= 0 by -n/2
    begin
        ## Storing remainder in binary
        ## array
        binaryNum[i] <- n % 2
        i <- i + 1
    end
 
    ## Printing binary array in reverse
    ## order
    number j <- i - 1
    for j until j < 0 by -1
        writeNumber(binaryNum[j])
end
 
## Driver code
func main()
begin
    number n <- 10
    decToBinary(n)
end
"""
        expect = 'Program([FuncDecl(Id(decToBinary), [VarDecl(Id(n), NumberType, None, None)], Block([VarDecl(Id(binaryNum), ArrayType([32.0], NumberType), None, None), VarDecl(Id(i), NumberType, None, NumLit(0.0)), For(Id(n), BinaryOp(<=, Id(n), NumLit(0.0)), BinaryOp(/, UnaryOp(-, Id(n)), NumLit(2.0)), Block([AssignStmt(ArrayCell(Id(binaryNum), [Id(i)]), BinaryOp(%, Id(n), NumLit(2.0))), AssignStmt(Id(i), BinaryOp(+, Id(i), NumLit(1.0)))])), VarDecl(Id(j), NumberType, None, BinaryOp(-, Id(i), NumLit(1.0))), For(Id(j), BinaryOp(<, Id(j), NumLit(0.0)), UnaryOp(-, NumLit(1.0)), CallStmt(Id(writeNumber), [ArrayCell(Id(binaryNum), [Id(j)])]))])), FuncDecl(Id(main), [], Block([VarDecl(Id(n), NumberType, None, NumLit(10.0)), CallStmt(Id(decToBinary), [Id(n)])]))])'
        self.assertTrue(TestAST.test(input, expect, 2081))
    
    def test_82(self):
        '''Hex to Dec'''
        input = """ 
## Function to convert hexadecimal 
## to decimal 
func hexadecimalToDecimal(string hexVal) 
begin 
    number len <- size(hexVal) 
  
    ## Initializing base value to 1, 
    ## i.e 16^0 
    number base <- 1 
  
    number dec_val <- 0 
  
    ## Extracting characters as digits 
    ## from last character 
    number i <- len - 1
    for i until i < 0 by -1 begin 
        ## If character lies in '0'-'9', 
        ## converting it to integral 0-9 
        ## by subtracting 48 from ASCII value 
        if ((hexVal[i] >= "0") and (hexVal[i] <= "9")) begin 
            dec_val <- dec_val + ((hexVal[i]) - 48) * base 
  
            ## incrementing base by power 
            base <- base * 16 
        end 
  
        ## If character lies in 'A'-'F' , converting 
        ## it to integral 10 - 15 by subtracting 55 
        ## from ASCII value 
        else if ((hexVal[i] >= "A") and( hexVal[i] <= "F")) begin 
            dec_val <- dec_val + ((hexVal[i]) - 55) * base 
  
            ## Incrementing base by power 
            base <- base * 16 
        end 
    end 
    return dec_val 
end 
  
## Driver code 
func main() 
begin 
    string hexNum <- "FFFF1111" 
    writeNumber(hexadecimalToDecimal(hexNum)) 
end
"""
        expect = 'Program([FuncDecl(Id(hexadecimalToDecimal), [VarDecl(Id(hexVal), StringType, None, None)], Block([VarDecl(Id(len), NumberType, None, CallExpr(Id(size), [Id(hexVal)])), VarDecl(Id(base), NumberType, None, NumLit(1.0)), VarDecl(Id(dec_val), NumberType, None, NumLit(0.0)), VarDecl(Id(i), NumberType, None, BinaryOp(-, Id(len), NumLit(1.0))), For(Id(i), BinaryOp(<, Id(i), NumLit(0.0)), UnaryOp(-, NumLit(1.0)), Block([If((BinaryOp(and, BinaryOp(>=, ArrayCell(Id(hexVal), [Id(i)]), StringLit(0)), BinaryOp(<=, ArrayCell(Id(hexVal), [Id(i)]), StringLit(9))), Block([AssignStmt(Id(dec_val), BinaryOp(+, Id(dec_val), BinaryOp(*, BinaryOp(-, ArrayCell(Id(hexVal), [Id(i)]), NumLit(48.0)), Id(base)))), AssignStmt(Id(base), BinaryOp(*, Id(base), NumLit(16.0)))])), [], If((BinaryOp(and, BinaryOp(>=, ArrayCell(Id(hexVal), [Id(i)]), StringLit(A)), BinaryOp(<=, ArrayCell(Id(hexVal), [Id(i)]), StringLit(F))), Block([AssignStmt(Id(dec_val), BinaryOp(+, Id(dec_val), BinaryOp(*, BinaryOp(-, ArrayCell(Id(hexVal), [Id(i)]), NumLit(55.0)), Id(base)))), AssignStmt(Id(base), BinaryOp(*, Id(base), NumLit(16.0)))])), [], None))])), Return(Id(dec_val))])), FuncDecl(Id(main), [], Block([VarDecl(Id(hexNum), StringType, None, StringLit(FFFF1111)), CallStmt(Id(writeNumber), [CallExpr(Id(hexadecimalToDecimal), [Id(hexNum)])])]))])'
        self.assertTrue(TestAST.test(input, expect, 2082))
    
    def test_83(self):
        '''Dec to Hex'''
        input = """ 
## Function to convert decimal 
## to hexadecimal 
func decToHexa(number n) 
begin 
    ## char array to store hexadecimal number 
    string hexaDeciNum[100] 
  
    ## Counter for hexadecimal number array 
    number i <- 0 
    for n until n <= 0 by -15*n/16
    begin 
        ## Temporary variable to store remainder 
        number temp <- 0 
  
        ## Storing remainder in temp variable. 
        temp <- n % 16 
  
        ## Check if temp < 10 
        if (temp < 10) begin 
            hexaDeciNum[i] <- temp + 48 
            i <- i + 1
        end 
        else begin 
            hexaDeciNum[i] <- temp + 55 
            i <- i + 1
        end 
  
        n <- n / 16 
    end 
  
    ## Printing hexadecimal number 
    ## array in reverse order 
    number j <- i - 1
    for j until j < 0 by -1
        writeString(hexaDeciNum[j])
end 
  
## Driver code 
func main() 
begin 
    number n <- 1007 
    decToHexa(n) 
end
"""
        expect = 'Program([FuncDecl(Id(decToHexa), [VarDecl(Id(n), NumberType, None, None)], Block([VarDecl(Id(hexaDeciNum), ArrayType([100.0], StringType), None, None), VarDecl(Id(i), NumberType, None, NumLit(0.0)), For(Id(n), BinaryOp(<=, Id(n), NumLit(0.0)), BinaryOp(/, BinaryOp(*, UnaryOp(-, NumLit(15.0)), Id(n)), NumLit(16.0)), Block([VarDecl(Id(temp), NumberType, None, NumLit(0.0)), AssignStmt(Id(temp), BinaryOp(%, Id(n), NumLit(16.0))), If((BinaryOp(<, Id(temp), NumLit(10.0)), Block([AssignStmt(ArrayCell(Id(hexaDeciNum), [Id(i)]), BinaryOp(+, Id(temp), NumLit(48.0))), AssignStmt(Id(i), BinaryOp(+, Id(i), NumLit(1.0)))])), [], Block([AssignStmt(ArrayCell(Id(hexaDeciNum), [Id(i)]), BinaryOp(+, Id(temp), NumLit(55.0))), AssignStmt(Id(i), BinaryOp(+, Id(i), NumLit(1.0)))])), AssignStmt(Id(n), BinaryOp(/, Id(n), NumLit(16.0)))])), VarDecl(Id(j), NumberType, None, BinaryOp(-, Id(i), NumLit(1.0))), For(Id(j), BinaryOp(<, Id(j), NumLit(0.0)), UnaryOp(-, NumLit(1.0)), CallStmt(Id(writeString), [ArrayCell(Id(hexaDeciNum), [Id(j)])]))])), FuncDecl(Id(main), [], Block([VarDecl(Id(n), NumberType, None, NumLit(1007.0)), CallStmt(Id(decToHexa), [Id(n)])]))])'
        self.assertTrue(TestAST.test(input, expect, 2083))
    
    def test_84(self):
        input = """ 
## Function to reverse a string
func reverseStr(string str)
begin
    number n <- length(str)
 
    ## Swap character starting from two
    ## corners
    number i <- 0
    for i until i >= n / 2 by 1
        swap(str[i], str[n - i - 1])
end
 
## Driver program
func main()
begin
    string str <- "I Am A Rock"
    reverseStr(str)
    writeString(str)
end
"""
        expect = 'Program([FuncDecl(Id(reverseStr), [VarDecl(Id(str), StringType, None, None)], Block([VarDecl(Id(n), NumberType, None, CallExpr(Id(length), [Id(str)])), VarDecl(Id(i), NumberType, None, NumLit(0.0)), For(Id(i), BinaryOp(>=, Id(i), BinaryOp(/, Id(n), NumLit(2.0))), NumLit(1.0), CallStmt(Id(swap), [ArrayCell(Id(str), [Id(i)]), ArrayCell(Id(str), [BinaryOp(-, BinaryOp(-, Id(n), Id(i)), NumLit(1.0))])]))])), FuncDecl(Id(main), [], Block([VarDecl(Id(str), StringType, None, StringLit(I Am A Rock)), CallStmt(Id(reverseStr), [Id(str)]), CallStmt(Id(writeString), [Id(str)])]))])'
        self.assertTrue(TestAST.test(input, expect, 2084))
    
    def test_85(self):
        input = """ 
func replace(string s, string c1, string c2)
begin
    number l <- length(s)
 
    ## loop to traverse in the string
    number i <- 0
    for i until i >= l by 1
    begin
        ## check for c1 and replace
        if (s[i] == c1)
            s[i] <- c2
 
        ## check for c2 and replace
        elif (s[i] == c2)
            s[i] <- c1
    end
    return s
end
 
## Driver code
func main()
begin
    string s <- "wwwwwwwwwwwwrrrrrrrrreyy"
    string c1 <- "e"
    string c2 <- "r"
    writeString(replace(s, c1, c2))
end
"""
        expect = 'Program([FuncDecl(Id(replace), [VarDecl(Id(s), StringType, None, None), VarDecl(Id(c1), StringType, None, None), VarDecl(Id(c2), StringType, None, None)], Block([VarDecl(Id(l), NumberType, None, CallExpr(Id(length), [Id(s)])), VarDecl(Id(i), NumberType, None, NumLit(0.0)), For(Id(i), BinaryOp(>=, Id(i), Id(l)), NumLit(1.0), Block([If((BinaryOp(==, ArrayCell(Id(s), [Id(i)]), Id(c1)), AssignStmt(ArrayCell(Id(s), [Id(i)]), Id(c2))), [(BinaryOp(==, ArrayCell(Id(s), [Id(i)]), Id(c2)), AssignStmt(ArrayCell(Id(s), [Id(i)]), Id(c1)))], None)])), Return(Id(s))])), FuncDecl(Id(main), [], Block([VarDecl(Id(s), StringType, None, StringLit(wwwwwwwwwwwwrrrrrrrrreyy)), VarDecl(Id(c1), StringType, None, StringLit(e)), VarDecl(Id(c2), StringType, None, StringLit(r)), CallStmt(Id(writeString), [CallExpr(Id(replace), [Id(s), Id(c1), Id(c2)])])]))])'
        self.assertTrue(TestAST.test(input, expect, 2085))
    
    def test_86(self):
        input = """ 
## Function to find string which has 
## first character of each word.
func firstLetterWord(string str)
begin
    string result <- ""
 
    ## Traverse the string
    bool v <- true
    number i <- 0
    for i until i >= length(str) by 1
    begin
        ## If it is space, set v as true.
        if (str[i] == " ")
            v <- true
 
        ## Else check if v is true or not.
        ## If true, copy character in output
        ## string and set v as false.
        elif ((str[i] != " ") and (v == true))
        begin
            push_back(result, str[i])
            v <- false
        end
    end
 
    return result
end
 
## Driver code
func main()
begin
    string str <- "World Health Organization and some kid s"
    writeString(firstLetterWord(str))
end
"""
        expect = 'Program([FuncDecl(Id(firstLetterWord), [VarDecl(Id(str), StringType, None, None)], Block([VarDecl(Id(result), StringType, None, StringLit()), VarDecl(Id(v), BoolType, None, BooleanLit(True)), VarDecl(Id(i), NumberType, None, NumLit(0.0)), For(Id(i), BinaryOp(>=, Id(i), CallExpr(Id(length), [Id(str)])), NumLit(1.0), Block([If((BinaryOp(==, ArrayCell(Id(str), [Id(i)]), StringLit( )), AssignStmt(Id(v), BooleanLit(True))), [(BinaryOp(and, BinaryOp(!=, ArrayCell(Id(str), [Id(i)]), StringLit( )), BinaryOp(==, Id(v), BooleanLit(True))), Block([CallStmt(Id(push_back), [Id(result), ArrayCell(Id(str), [Id(i)])]), AssignStmt(Id(v), BooleanLit(False))]))], None)])), Return(Id(result))])), FuncDecl(Id(main), [], Block([VarDecl(Id(str), StringType, None, StringLit(World Health Organization and some kid s)), CallStmt(Id(writeString), [CallExpr(Id(firstLetterWord), [Id(str)])])]))])'
        self.assertTrue(TestAST.test(input, expect, 2086))
    
    def test_87(self):
        input = """ 
## Function to check whether string
## is palindrome
func isPalindrome(string S)
begin
    ## Iterate over the range [0, N/2]
    number i <- 0
    for i until i >= length(S) / 2 by 1 begin
 
        ## If S[i] is not equal to
        ## the S[N-i-1]
        if (S[i] != S[length(S) - i - 1]) begin
            return "No"
        end
    end
    return "Yes"
end
 
## Driver Code
func main()
begin
    string S <- "_xyzYzyx_"
    writeString(isPalindrome(S))
end
"""
        expect = 'Program([FuncDecl(Id(isPalindrome), [VarDecl(Id(S), StringType, None, None)], Block([VarDecl(Id(i), NumberType, None, NumLit(0.0)), For(Id(i), BinaryOp(>=, Id(i), BinaryOp(/, CallExpr(Id(length), [Id(S)]), NumLit(2.0))), NumLit(1.0), Block([If((BinaryOp(!=, ArrayCell(Id(S), [Id(i)]), ArrayCell(Id(S), [BinaryOp(-, BinaryOp(-, CallExpr(Id(length), [Id(S)]), Id(i)), NumLit(1.0))])), Block([Return(StringLit(No))])), [], None)])), Return(StringLit(Yes))])), FuncDecl(Id(main), [], Block([VarDecl(Id(S), StringType, None, StringLit(_xyzYzyx_)), CallStmt(Id(writeString), [CallExpr(Id(isPalindrome), [Id(S)])])]))])'
        self.assertTrue(TestAST.test(input, expect, 2087))
    
    def test_88(self):
        input = """ 
## Returns true if the string is
## pangram else false
func checkPangram(string str)
begin
    ## Create a hash table to mark
    ## the characters
    ## present in the string
    bool mark[26] <- [false]
 
    ## For indexing in mark[]
    number index
 
    ## Traverse all characters
    number i <- 0
    for i until i >= length(str) by 1 begin
 
        ## If uppercase character,
        ## subtract 'A' to find index.
        if (("A" <= str[i]) and (str[i] <= "Z"))
            index <- str[i] - "A"
 
        ## If lowercase character,
        ## subtract 'a' to find index.
        else if (("a" <= str[i]) and (str[i] <= "z"))
            index <- str[i] - "a"
 
        ## If this character is not
        ## an alphabet, skip to next one.
        else
            continue
 
        mark[index] <- true
    end
 
    ## Return false
    ## if any character is unmarked
    number i <- 0
    for i until i > 25 by 1
        if (mark[i] == false)
            return (false)
 
    ## If all characters were present
    return (true)
end
 
## Driver Code
func main()
begin
    string str <- "The quick brown fox jumps over the lazy dog"
 
    if (checkPangram(str) == true)
        writeString("Yes")
    else
        writeString("No")
end
"""
        expect = 'Program([FuncDecl(Id(checkPangram), [VarDecl(Id(str), StringType, None, None)], Block([VarDecl(Id(mark), ArrayType([26.0], BoolType), None, ArrayLit(BooleanLit(False))), VarDecl(Id(index), NumberType, None, None), VarDecl(Id(i), NumberType, None, NumLit(0.0)), For(Id(i), BinaryOp(>=, Id(i), CallExpr(Id(length), [Id(str)])), NumLit(1.0), Block([If((BinaryOp(and, BinaryOp(<=, StringLit(A), ArrayCell(Id(str), [Id(i)])), BinaryOp(<=, ArrayCell(Id(str), [Id(i)]), StringLit(Z))), AssignStmt(Id(index), BinaryOp(-, ArrayCell(Id(str), [Id(i)]), StringLit(A)))), [], If((BinaryOp(and, BinaryOp(<=, StringLit(a), ArrayCell(Id(str), [Id(i)])), BinaryOp(<=, ArrayCell(Id(str), [Id(i)]), StringLit(z))), AssignStmt(Id(index), BinaryOp(-, ArrayCell(Id(str), [Id(i)]), StringLit(a)))), [], Continue)), AssignStmt(ArrayCell(Id(mark), [Id(index)]), BooleanLit(True))])), VarDecl(Id(i), NumberType, None, NumLit(0.0)), For(Id(i), BinaryOp(>, Id(i), NumLit(25.0)), NumLit(1.0), If((BinaryOp(==, ArrayCell(Id(mark), [Id(i)]), BooleanLit(False)), Return(BooleanLit(False))), [], None)), Return(BooleanLit(True))])), FuncDecl(Id(main), [], Block([VarDecl(Id(str), StringType, None, StringLit(The quick brown fox jumps over the lazy dog)), If((BinaryOp(==, CallExpr(Id(checkPangram), [Id(str)]), BooleanLit(True)), CallStmt(Id(writeString), [StringLit(Yes)])), [], CallStmt(Id(writeString), [StringLit(No)]))]))])'
        self.assertTrue(TestAST.test(input, expect, 2088))
    
    def test_89(self):
        input = """ 
func split(string str, string del)
begin
    ## declaring temp string to store the curr "word" upto del
    string temp <- ""

    number i <- 0
    for i until i >= size(str) by 1
    begin
        ## If cur char is not del, then append it to the cur "word", otherwise
        ## you have completed the word, print it, and start a new word
        if (str[i] != del)
        begin
            temp <- temp +str[i]
        end
        else
        begin
            writeString(temp ... " ")
            temp <- ""
        end
    end
       
    writeString(temp)
end
 
func main() begin
 
    string str <- "abc.xyz.mno.ghi.abcdefu.s.a"    ## string to be split
    dynamic del <- "."    ## delimiter around which string is to be split
   
    split(str, del)
end
"""
        expect = 'Program([FuncDecl(Id(split), [VarDecl(Id(str), StringType, None, None), VarDecl(Id(del), StringType, None, None)], Block([VarDecl(Id(temp), StringType, None, StringLit()), VarDecl(Id(i), NumberType, None, NumLit(0.0)), For(Id(i), BinaryOp(>=, Id(i), CallExpr(Id(size), [Id(str)])), NumLit(1.0), Block([If((BinaryOp(!=, ArrayCell(Id(str), [Id(i)]), Id(del)), Block([AssignStmt(Id(temp), BinaryOp(+, Id(temp), ArrayCell(Id(str), [Id(i)])))])), [], Block([CallStmt(Id(writeString), [BinaryOp(..., Id(temp), StringLit( ))]), AssignStmt(Id(temp), StringLit())]))])), CallStmt(Id(writeString), [Id(temp)])])), FuncDecl(Id(main), [], Block([VarDecl(Id(str), StringType, None, StringLit(abc.xyz.mno.ghi.abcdefu.s.a)), VarDecl(Id(del), None, dynamic, StringLit(.)), CallStmt(Id(split), [Id(str), Id(del)])]))])'
        self.assertTrue(TestAST.test(input, expect, 2089))
    
    def test_90(self):
        input = """ 
func average(number a, number n)
begin
    ## Find sum of array element
    number sum <- 0
    number i <- 0
    for i until i >= n by 1
        sum <- sum+ a[i]
 
    return sum / n
end
"""
        expect = 'Program([FuncDecl(Id(average), [VarDecl(Id(a), NumberType, None, None), VarDecl(Id(n), NumberType, None, None)], Block([VarDecl(Id(sum), NumberType, None, NumLit(0.0)), VarDecl(Id(i), NumberType, None, NumLit(0.0)), For(Id(i), BinaryOp(>=, Id(i), Id(n)), NumLit(1.0), AssignStmt(Id(sum), BinaryOp(+, Id(sum), ArrayCell(Id(a), [Id(i)])))), Return(BinaryOp(/, Id(sum), Id(n)))]))])'
        self.assertTrue(TestAST.test(input, expect, 2090))
    
    def test_91(self):
        input = """ 
func remove_all_occurrence(number arr, number target, number n)
begin
    number cnt <- 0
    
    ## Shifting non target elements 
    ## to the left side
    number i <- 0
    for i until i >= n by 1
    begin
        if(arr[i] != target)
            arr[i - cnt] <- arr[i] 
        else
            cnt <- 1+cnt
    end
    
    ## Printing the array
    number i <- 0
    for i until i >= n - cnt by 1
    begin
        writeString(arr[i] ... " ")
    end
    return
end
 
## Driver code
func main() 
begin
    number arr[11] <- [1, 4, 3, 6, 8, 3, 9, 10, 3, 3, 7]
    number target <- 3
    remove_all_occurrence(arr, target, 11)
end
"""
        expect = 'Program([FuncDecl(Id(remove_all_occurrence), [VarDecl(Id(arr), NumberType, None, None), VarDecl(Id(target), NumberType, None, None), VarDecl(Id(n), NumberType, None, None)], Block([VarDecl(Id(cnt), NumberType, None, NumLit(0.0)), VarDecl(Id(i), NumberType, None, NumLit(0.0)), For(Id(i), BinaryOp(>=, Id(i), Id(n)), NumLit(1.0), Block([If((BinaryOp(!=, ArrayCell(Id(arr), [Id(i)]), Id(target)), AssignStmt(ArrayCell(Id(arr), [BinaryOp(-, Id(i), Id(cnt))]), ArrayCell(Id(arr), [Id(i)]))), [], AssignStmt(Id(cnt), BinaryOp(+, NumLit(1.0), Id(cnt))))])), VarDecl(Id(i), NumberType, None, NumLit(0.0)), For(Id(i), BinaryOp(>=, Id(i), BinaryOp(-, Id(n), Id(cnt))), NumLit(1.0), Block([CallStmt(Id(writeString), [BinaryOp(..., ArrayCell(Id(arr), [Id(i)]), StringLit( ))])])), Return()])), FuncDecl(Id(main), [], Block([VarDecl(Id(arr), ArrayType([11.0], NumberType), None, ArrayLit(NumLit(1.0), NumLit(4.0), NumLit(3.0), NumLit(6.0), NumLit(8.0), NumLit(3.0), NumLit(9.0), NumLit(10.0), NumLit(3.0), NumLit(3.0), NumLit(7.0))), VarDecl(Id(target), NumberType, None, NumLit(3.0)), CallStmt(Id(remove_all_occurrence), [Id(arr), Id(target), NumLit(11.0)])]))])'
        self.assertTrue(TestAST.test(input, expect, 2091))
    
    def test_92(self):
        input = """ 
## This function returns new size of modified array
func removeDuplicates(number arr) 
begin 
  
    number temp[10] 
  
    ## Start traversing elements 
    number j <- 0 
  
    ## If current element is not equal  
    ## to next element then store that  
    ## current element 
    number i <- 0
    for i until i >= (n - 1) by 1
        if (arr[i] != arr[i + 1]) 
        begin
            temp[j+1] <- arr[i] 
            j <- 1+j
        end
  
    ## Store the last element as whether  
    ## it is unique or repeated, it hasn't  
    ## stored previously 
    temp[j] <- arr[n - 1] 
    j <- j+1
  
    ## Modify original array 
    i <- 0
    for i until i >= j by 1
        arr[i] <- temp[i] 
  
    return j 
end 
  
## Driver code 
func main() 
begin 
    number arr[10] <- [1, 2, 2, 3, 4, 4, 4, 5, 5, 1]
  
    ## RemoveDuplicates() returns  
    ## new size of array
    n <- removeDuplicates(arr) 
  
    ## Print updated array 
    number i <- 0
    for i until i >= n by 1
        writeString(arr[i] ... " " )
end 
"""
        expect = 'Program([FuncDecl(Id(removeDuplicates), [VarDecl(Id(arr), NumberType, None, None)], Block([VarDecl(Id(temp), ArrayType([10.0], NumberType), None, None), VarDecl(Id(j), NumberType, None, NumLit(0.0)), VarDecl(Id(i), NumberType, None, NumLit(0.0)), For(Id(i), BinaryOp(>=, Id(i), BinaryOp(-, Id(n), NumLit(1.0))), NumLit(1.0), If((BinaryOp(!=, ArrayCell(Id(arr), [Id(i)]), ArrayCell(Id(arr), [BinaryOp(+, Id(i), NumLit(1.0))])), Block([AssignStmt(ArrayCell(Id(temp), [BinaryOp(+, Id(j), NumLit(1.0))]), ArrayCell(Id(arr), [Id(i)])), AssignStmt(Id(j), BinaryOp(+, NumLit(1.0), Id(j)))])), [], None)), AssignStmt(ArrayCell(Id(temp), [Id(j)]), ArrayCell(Id(arr), [BinaryOp(-, Id(n), NumLit(1.0))])), AssignStmt(Id(j), BinaryOp(+, Id(j), NumLit(1.0))), AssignStmt(Id(i), NumLit(0.0)), For(Id(i), BinaryOp(>=, Id(i), Id(j)), NumLit(1.0), AssignStmt(ArrayCell(Id(arr), [Id(i)]), ArrayCell(Id(temp), [Id(i)]))), Return(Id(j))])), FuncDecl(Id(main), [], Block([VarDecl(Id(arr), ArrayType([10.0], NumberType), None, ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(2.0), NumLit(3.0), NumLit(4.0), NumLit(4.0), NumLit(4.0), NumLit(5.0), NumLit(5.0), NumLit(1.0))), AssignStmt(Id(n), CallExpr(Id(removeDuplicates), [Id(arr)])), VarDecl(Id(i), NumberType, None, NumLit(0.0)), For(Id(i), BinaryOp(>=, Id(i), Id(n)), NumLit(1.0), CallStmt(Id(writeString), [BinaryOp(..., ArrayCell(Id(arr), [Id(i)]), StringLit( ))]))]))])'
        self.assertTrue(TestAST.test(input, expect, 2092))
    
    def test_93(self):
        input = """ 
## This function returns new size of modified array
func removeDuplicates(number arr, number n) 
begin 
    ## To store index of next  
    ## unique element 
    number j <- 0 
    number i <- 0 
  
    for i until i >= n - 1 by 1
        if (arr[i] != arr[i + 1]) begin
            arr[j] <- arr[i] 
            j <- 1 +j
            end
  
    arr[j] <- arr[n - 1] 
    j <- j +1
  
    return j 
end 
  
## Driver code 
func main() 
begin 
    number arr[10] <- [1, 2, 2, 3, 4, 4, 4, 5, 5, 1]
  
    ## RemoveDuplicates() returns  
    ## new size of array
    n <- removeDuplicates(arr, 10) 
  
    ## Print updated array 
    number i <- 0
    for i until i >= n by 1
        writeString(  \t  arr[i]       ...  \t" " )
end 
"""
        expect = 'Program([FuncDecl(Id(removeDuplicates), [VarDecl(Id(arr), NumberType, None, None), VarDecl(Id(n), NumberType, None, None)], Block([VarDecl(Id(j), NumberType, None, NumLit(0.0)), VarDecl(Id(i), NumberType, None, NumLit(0.0)), For(Id(i), BinaryOp(>=, Id(i), BinaryOp(-, Id(n), NumLit(1.0))), NumLit(1.0), If((BinaryOp(!=, ArrayCell(Id(arr), [Id(i)]), ArrayCell(Id(arr), [BinaryOp(+, Id(i), NumLit(1.0))])), Block([AssignStmt(ArrayCell(Id(arr), [Id(j)]), ArrayCell(Id(arr), [Id(i)])), AssignStmt(Id(j), BinaryOp(+, NumLit(1.0), Id(j)))])), [], None)), AssignStmt(ArrayCell(Id(arr), [Id(j)]), ArrayCell(Id(arr), [BinaryOp(-, Id(n), NumLit(1.0))])), AssignStmt(Id(j), BinaryOp(+, Id(j), NumLit(1.0))), Return(Id(j))])), FuncDecl(Id(main), [], Block([VarDecl(Id(arr), ArrayType([10.0], NumberType), None, ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(2.0), NumLit(3.0), NumLit(4.0), NumLit(4.0), NumLit(4.0), NumLit(5.0), NumLit(5.0), NumLit(1.0))), AssignStmt(Id(n), CallExpr(Id(removeDuplicates), [Id(arr), NumLit(10.0)])), VarDecl(Id(i), NumberType, None, NumLit(0.0)), For(Id(i), BinaryOp(>=, Id(i), Id(n)), NumLit(1.0), CallStmt(Id(writeString), [BinaryOp(..., ArrayCell(Id(arr), [Id(i)]), StringLit( ))]))]))])'
        self.assertTrue(TestAST.test(input, expect, 2093))
    
    def test_94(self):
        input = """ 
## Function to rotate array to the left by d times
func Rotate(number arr, number d)
begin
    ## Storing rotated version of array
    number temp[20]
    number n <- size(arr)
 
    ## Keeping track of the current index
    ## of temp[]
    number k <- 0
 
    ## Storing the n - d elements of
    ## array arr[] to the front of temp[]
    number i <- d
    for i until i >= n by 1 begin
        temp[k] <- arr[i]
        k<-k+1
    end
 
    ## Storing the first d elements of array arr[]
    ##  into temp
    i <- 0
    for i until i >= d by 1 begin
        temp[k] <- arr[i]
        k<-1+k
    end
 
    ## Copying the elements of temp[] in arr[]
    ## to get the final rotated array
    i <- 0
    for i until i >= n by 1 begin
        arr[i] <- temp[i]
    end
end
"""
        expect = 'Program([FuncDecl(Id(Rotate), [VarDecl(Id(arr), NumberType, None, None), VarDecl(Id(d), NumberType, None, None)], Block([VarDecl(Id(temp), ArrayType([20.0], NumberType), None, None), VarDecl(Id(n), NumberType, None, CallExpr(Id(size), [Id(arr)])), VarDecl(Id(k), NumberType, None, NumLit(0.0)), VarDecl(Id(i), NumberType, None, Id(d)), For(Id(i), BinaryOp(>=, Id(i), Id(n)), NumLit(1.0), Block([AssignStmt(ArrayCell(Id(temp), [Id(k)]), ArrayCell(Id(arr), [Id(i)])), AssignStmt(Id(k), BinaryOp(+, Id(k), NumLit(1.0)))])), AssignStmt(Id(i), NumLit(0.0)), For(Id(i), BinaryOp(>=, Id(i), Id(d)), NumLit(1.0), Block([AssignStmt(ArrayCell(Id(temp), [Id(k)]), ArrayCell(Id(arr), [Id(i)])), AssignStmt(Id(k), BinaryOp(+, NumLit(1.0), Id(k)))])), AssignStmt(Id(i), NumLit(0.0)), For(Id(i), BinaryOp(>=, Id(i), Id(n)), NumLit(1.0), Block([AssignStmt(ArrayCell(Id(arr), [Id(i)]), ArrayCell(Id(temp), [Id(i)]))]))]))])'
        self.assertTrue(TestAST.test(input, expect, 2094))
    
    def test_95(self):
        input = """ 
## Function to rotate array to the left by d times
func Rotate(number arr, number d, number n)
begin
    number p <- 1
    for p until p>d by 1
    begin
        number last <- arr[0]
        number i <- 0
        for i until i >= n - 1 by 1begin
            arr[i] <- arr[i + 1]
        end
        arr[n - 1] <- last
    end
end
"""
        expect = 'Program([FuncDecl(Id(Rotate), [VarDecl(Id(arr), NumberType, None, None), VarDecl(Id(d), NumberType, None, None), VarDecl(Id(n), NumberType, None, None)], Block([VarDecl(Id(p), NumberType, None, NumLit(1.0)), For(Id(p), BinaryOp(>, Id(p), Id(d)), NumLit(1.0), Block([VarDecl(Id(last), NumberType, None, ArrayCell(Id(arr), [NumLit(0.0)])), VarDecl(Id(i), NumberType, None, NumLit(0.0)), For(Id(i), BinaryOp(>=, Id(i), BinaryOp(-, Id(n), NumLit(1.0))), NumLit(1.0), Block([AssignStmt(ArrayCell(Id(arr), [Id(i)]), ArrayCell(Id(arr), [BinaryOp(+, Id(i), NumLit(1.0))]))])), AssignStmt(ArrayCell(Id(arr), [BinaryOp(-, Id(n), NumLit(1.0))]), Id(last))]))]))])'
        self.assertTrue(TestAST.test(input, expect, 2095))
    
    def test_96(self):
        input = """ 
## Function for print prime
## number in given range
func primeInRange(number L, number R)
begin
    number flag
 
    ## Traverse each number in the
    ## interval with the help of for loop
    number i <- L
    for i until i > R by 1 begin
 
        ## Skip 0 and 1 as they are
        ## neither prime nor composite
        if (i == 1 or (i == 0))
            continue
 
        ## flag variable to tell
        ## if i is prime or not
        flag <- 1
 
        ## Iterate to check if i is prime
        ## or not
        number j <- 2
        for j until j > i / 2 by 1 begin
            if (i % j = 0)begin
                flag <- 0
                break
            end
        end
 
        ## flag = 1 means i is prime
        ## and flag = 0 means i is not prime
        if (flag = 1)
            writeString(i ... " ")
    end
end
"""
        expect = 'Program([FuncDecl(Id(primeInRange), [VarDecl(Id(L), NumberType, None, None), VarDecl(Id(R), NumberType, None, None)], Block([VarDecl(Id(flag), NumberType, None, None), VarDecl(Id(i), NumberType, None, Id(L)), For(Id(i), BinaryOp(>, Id(i), Id(R)), NumLit(1.0), Block([If((BinaryOp(==, Id(i), BinaryOp(or, NumLit(1.0), BinaryOp(==, Id(i), NumLit(0.0)))), Continue), [], None), AssignStmt(Id(flag), NumLit(1.0)), VarDecl(Id(j), NumberType, None, NumLit(2.0)), For(Id(j), BinaryOp(>, Id(j), BinaryOp(/, Id(i), NumLit(2.0))), NumLit(1.0), Block([If((BinaryOp(=, BinaryOp(%, Id(i), Id(j)), NumLit(0.0)), Block([AssignStmt(Id(flag), NumLit(0.0)), Break])), [], None)])), If((BinaryOp(=, Id(flag), NumLit(1.0)), CallStmt(Id(writeString), [BinaryOp(..., Id(i), StringLit( ))])), [], None)]))]))])'
        self.assertTrue(TestAST.test(input, expect, 2096))
    
    def test_97(self):
        input = """ 
## Function check whether a number
## is prime or not
func isPrime(number n)
begin
    ## Check if n=2 or n=3
    if ((n == 2) or (n = 3))
        return true
    ## Check whether n is divisible by 2 or 3
    if ((n % 2 =0) or (n % 3==0))
        return false
 
    ## Check from 5 to square root of n
    ## Iterate i by (i+6)
    number i <- 5
    for  i until i * i > n by 6
        if ((n % i == 0) or (n % (i + 2) == 0))
            return false
 
    return true
end
 
## Function for print prime
## number in given range
func primeInRange(number L, number R)
begin
 
    ## Skip 0 and 1 as they are
    ## neither prime nor composite
    ## and also if 2 is in range
    ## then print it
    if ((R >= 2) and (L <= 2)) begin
        writeNumber(2)
        L <- 3
    end
 
    ## Making sure that L is odd before
    ## beginning the loop
    if (L % 2 == 0)
        L<-L+1
 
    ## NOTE : We traverse through
    ## odd numbers only
    number i <- L
    for i until i > R by 2 begin
 
        ## If number is prime print it
        if (isPrime(i))
            writeNumber(i)
    end
end
"""
        expect = 'Program([FuncDecl(Id(isPrime), [VarDecl(Id(n), NumberType, None, None)], Block([If((BinaryOp(or, BinaryOp(==, Id(n), NumLit(2.0)), BinaryOp(=, Id(n), NumLit(3.0))), Return(BooleanLit(True))), [], None), If((BinaryOp(or, BinaryOp(=, BinaryOp(%, Id(n), NumLit(2.0)), NumLit(0.0)), BinaryOp(==, BinaryOp(%, Id(n), NumLit(3.0)), NumLit(0.0))), Return(BooleanLit(False))), [], None), VarDecl(Id(i), NumberType, None, NumLit(5.0)), For(Id(i), BinaryOp(>, BinaryOp(*, Id(i), Id(i)), Id(n)), NumLit(6.0), If((BinaryOp(or, BinaryOp(==, BinaryOp(%, Id(n), Id(i)), NumLit(0.0)), BinaryOp(==, BinaryOp(%, Id(n), BinaryOp(+, Id(i), NumLit(2.0))), NumLit(0.0))), Return(BooleanLit(False))), [], None)), Return(BooleanLit(True))])), FuncDecl(Id(primeInRange), [VarDecl(Id(L), NumberType, None, None), VarDecl(Id(R), NumberType, None, None)], Block([If((BinaryOp(and, BinaryOp(>=, Id(R), NumLit(2.0)), BinaryOp(<=, Id(L), NumLit(2.0))), Block([CallStmt(Id(writeNumber), [NumLit(2.0)]), AssignStmt(Id(L), NumLit(3.0))])), [], None), If((BinaryOp(==, BinaryOp(%, Id(L), NumLit(2.0)), NumLit(0.0)), AssignStmt(Id(L), BinaryOp(+, Id(L), NumLit(1.0)))), [], None), VarDecl(Id(i), NumberType, None, Id(L)), For(Id(i), BinaryOp(>, Id(i), Id(R)), NumLit(2.0), Block([If((CallExpr(Id(isPrime), [Id(i)]), CallStmt(Id(writeNumber), [Id(i)])), [], None)]))]))])'
        self.assertTrue(TestAST.test(input, expect, 2097))
    
    def test_98(self):
        input = """ 
## Function to print the divisors 
func printDivisors(number n) 
begin 
    ## Note that this loop runs  
    ## till square root 
    number i <- 1
    for i until i > sqrt(n) by 1 
    begin 
        if (n % i == 0) 
        begin 
            ## If divisors are equal,  
            ## print only one 
            if (n / i == i) 
                writeString(" "... i )
  
            ## Otherwise print both 
            else 
                writeString((" "... i) ... (" " ...str( n / i)) )
        end 
    end 
end 
"""
        expect = 'Program([FuncDecl(Id(printDivisors), [VarDecl(Id(n), NumberType, None, None)], Block([VarDecl(Id(i), NumberType, None, NumLit(1.0)), For(Id(i), BinaryOp(>, Id(i), CallExpr(Id(sqrt), [Id(n)])), NumLit(1.0), Block([If((BinaryOp(==, BinaryOp(%, Id(n), Id(i)), NumLit(0.0)), Block([If((BinaryOp(==, BinaryOp(/, Id(n), Id(i)), Id(i)), CallStmt(Id(writeString), [BinaryOp(..., StringLit( ), Id(i))])), [], CallStmt(Id(writeString), [BinaryOp(..., BinaryOp(..., StringLit( ), Id(i)), BinaryOp(..., StringLit( ), CallExpr(Id(str), [BinaryOp(/, Id(n), Id(i))])))]))])), [], None)]))]))])'
        self.assertTrue(TestAST.test(input, expect, 2098))
    
    def test_99(self):
        input = """ 
## Print the multiplication table of a number up to a range
func main()
begin
    ## Change here to change
    ## input number
    number n <- 8
 
    number range <- readNumber()
    number i <- 1
    for i until i > range by 1
        writeString((n ... (" * " ... i) )... (" = " ...(str( n * i)..."\\\\n")))
end
"""
        expect = 'Program([FuncDecl(Id(main), [], Block([VarDecl(Id(n), NumberType, None, NumLit(8.0)), VarDecl(Id(range), NumberType, None, CallExpr(Id(readNumber), [])), VarDecl(Id(i), NumberType, None, NumLit(1.0)), For(Id(i), BinaryOp(>, Id(i), Id(range)), NumLit(1.0), CallStmt(Id(writeString), [BinaryOp(..., BinaryOp(..., Id(n), BinaryOp(..., StringLit( * ), Id(i))), BinaryOp(..., StringLit( = ), BinaryOp(..., CallExpr(Id(str), [BinaryOp(*, Id(n), Id(i))]), StringLit(\\\\n))))]))]))])'
        self.assertTrue(TestAST.test(input, expect, 2099))
    
    def test_100(self):
        input = """
func main(string str)
    return str(12-03-2024)
"""
        expect = 'Program([FuncDecl(Id(main), [VarDecl(Id(str), StringType, None, None)], Return(CallExpr(Id(str), [BinaryOp(-, BinaryOp(-, NumLit(12.0), NumLit(3.0)), NumLit(2024.0))])))])'
        self.assertTrue(TestAST.test(input, expect, 2100))