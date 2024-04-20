import unittest
from TestUtils import TestChecker
from AST import *


class CheckSuite(unittest.TestCase):
    def test_no_entry_point(self):
        input = """number a
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 400))
    
    def test_no_entry_point_2(self):
        input = """
        number a
        number b

        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 601))
    
    def test_no_entry_point_3(self):
        input = """
        number a
        number b
        func main()
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 602))

    def test_603(self):       # DONE
        input = """
func main()
begin
    var x <- [[[[1, 2]], [3, 4, 5]], [[6, 7, 8], [9, 10, 11]]]
    writeNumber(x)
end
"""
        expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0))), ArrayLit(NumLit(3.0), NumLit(4.0), NumLit(5.0))), ArrayLit(ArrayLit(NumLit(6.0), NumLit(7.0), NumLit(8.0)), ArrayLit(NumLit(9.0), NumLit(10.0), NumLit(11.0))))"
        myret_ = "Type Mismatch In Expression: ArrayLit(ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0))), ArrayLit(NumLit(3.0), NumLit(4.0), NumLit(5.0)))"
        self.assertTrue(TestChecker.test(input, expect, 603))

    def test_604(self):         # DONE
        input = """
func f(number x)
begin
    if (x = 0) return 0
    elif (x = 1) return 1
    else return f(x - 1) + f(x - 2)
end
    
func main()
begin
    dynamic a
    number x <- f(a)
    a[0] <- [1, 2, 3]
end
"""
        expect = "Type Mismatch In Expression: ArrayCell(Id(a), [NumLit(0.0)])"
        myret_ = "Undeclared Function: a"
        self.assertTrue(TestChecker.test(input, expect, 604))

###===============================================================

    def test_3001(self):    # CHECK LATER
        input = """
        dynamic a
        dynamic b
        dynamic c
        number arr[2,2] <- [[a,b],[3,4]]
        func main()
            return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 3001))
    
    def test_3002(self):        # DONE
        input = """
        func foo()
        number foo

        func main()
        begin
            foo()
            return
        end

        func foo()
        begin
            number a
        end
        """
        expect = "Redeclared Variable: foo"
        self.assertTrue(TestChecker.test(input, expect, 3002))
    
    def test_3003(self):        # DONE
        input = """
        number foo
        func foo()

        func main()
        begin
            foo()
            return
        end

        func foo()
        begin
            number a
        end
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 3003))
    
    def test_3004(self):        # CHECK LATER
        input = """
        func main()
            return

        dynamic a
        number b <- a[0]
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(b), NumberType, None, ArrayCell(Id(a), [NumLit(0.0)]))"
        self.assertTrue(TestChecker.test(input, expect, 3004))
    
    def test_3005(self):        # DONE
        input = """
        func main()
            return

        dynamic a
        var b <- a[0]
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(b), None, var, ArrayCell(Id(a), [NumLit(0.0)]))"
        self.assertTrue(TestChecker.test(input, expect, 3005))
    
    def test_3006(self):        # DONE
        input = """
        func main()
        begin
            number arr[2] <- [3,4]
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 3006))
    
    def test_3007(self):        # DONE
        input = """
        func main()
            number arr[2] <- ["3",4]
        """
        expect = "Type Mismatch In Expression: ArrayLit(StringLit(3), NumLit(4.0))"
        self.assertTrue(TestChecker.test(input, expect, 3007))
    
    def test_3008(self):        # DONE
        input = """
        func main()
            number arr[2,2] <- [[3,5],4]
        """
        expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(NumLit(3.0), NumLit(5.0)), NumLit(4.0))"
        self.assertTrue(TestChecker.test(input, expect, 3008))
    
    def test_3009(self):
        input = """
        func main()
        begin
            string a
            for a until a == "123" by 1
                a <- readNumber()
        end
        """
        expect = "Type Mismatch In Statement: For(Id(a), BinaryOp(==, Id(a), StringLit(123)), NumLit(1.0), AssignStmt(Id(a), CallExpr(Id(readNumber), [])))"
        self.assertTrue(TestChecker.test(input, expect, 3009))
    
    def test_3010(self):
        input = """
        func main()
        begin
            number a
            for a until a == "123" by 1
                a <- readNumber()
        end
        """
        expect = "Type Mismatch In Expression: BinaryOp(==, Id(a), StringLit(123))"
        self.assertTrue(TestChecker.test(input, expect, 3010))
    
    def test_3011(self):
        input = """
        func main()
        begin
            number a
            for a until a == 123 by 1
                a <- readNumber()
        end
        """
        expect = "Type Mismatch In Expression: BinaryOp(==, Id(a), NumLit(123.0))"
        self.assertTrue(TestChecker.test(input, expect, 3011))
    
    def test_3012(self):
        input = """
        func main()
        begin
            number a
            for a until a = 123 by -3
                a <- readNumber()
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 3012))
    
    def test_3013(self):
        input = """
        func foo()
        begin
            number a
            for a until a = 123 by -3
                a <- readNumber()
        end
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 3013))
    
    def test_3014(self):
        input = """
        func foo()
        begin
            number a
            for a until a = 123 by -3
                a <- readNumber()
            main()
        end
        """
        expect = "Undeclared Function: main"
        self.assertTrue(TestChecker.test(input, expect, 3014))
    
    def test_3015(self):
        input = """
        func foo()
        begin
            number a
            for a until a = 123 by -3
                a <- readNumber()
            main()
        end

        func main(number args)
            return
        """
        expect = "Undeclared Function: main"
        self.assertTrue(TestChecker.test(input, expect, 3015))
    
    def test_3016(self):
        input = """
        func main()
        func foo()
        begin
            number a
            for a until a = 123 by -3
                a <- readNumber()
            main()
        end

        func main(number args)
            return
        """
        expect = "Redeclared Function: main"
        self.assertTrue(TestChecker.test(input, expect, 3016))
    
    def test_3017(self):
        input = """
        func main()
        func foo()
        begin
            number a
            for a until a = 123 by -3
                a <- readNumber()
            main(a)
        end

        func main(number args)
            return
        """
        expect = "Type Mismatch In Statement: CallStmt(Id(main), [Id(a)])"
        self.assertTrue(TestChecker.test(input, expect, 3017))
    
    def test_3018(self):
        input = """
        func main(number args)
        func foo()
        begin
            number a
            for a until a = 123 by -3
                a <- readNumber()
            main(a)
        end

        func main()
            return
        """
        expect = "Redeclared Function: main"
        self.assertTrue(TestChecker.test(input, expect, 3018))
    
    def test_3019(self):
        input = """
        func main(number args)
        func foo()
        begin
            number a
            for a until a = 123 by -3
                a <- readNumber()
            main(a)
        end

        func main(number arg)
            return
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 3019))
    
    def test_3020(self):
        input = """
        ## func main()
        func foo()
        begin
            number a
            for a until a = 123 by -3
                writeString("123")
            ##main()
        end

        func main()
            return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 3020))
    
    def test_3021(self):
        input = """
        func main()
        func foo()
        begin
            number a
            for a until a = 123 by -3
                writeString("123")
            main()
        end

        func main()
            return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 3021))
    
    def test_3022(self):
        input = """
        func main()
        func foo()
        begin
            number a
            for a until a = 123 by -3
                writeBool("123")
            main()
        end

        func main()
            return
        """
        expect = "Type Mismatch In Statement: CallStmt(Id(writeBool), [StringLit(123)])"
        self.assertTrue(TestChecker.test(input, expect, 3022))
    
    def test_3023(self):
        input = """
        func main()
            return
        func foo()
        begin
            number a
            for a until a = 123 by -3
                writeBool(false)
            main()
        end

        func main()
        """
        expect = "Redeclared Function: main"
        self.assertTrue(TestChecker.test(input, expect, 3023))
    
    def test_3024(self):        # CHECK LATER
        input = """
        func foo(number x)
        func main()
        begin
            var m <- foo(5)
        end
        func foo(number x)
            return x * 2
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(m), None, var, CallExpr(Id(foo), [NumLit(5.0)]))"
        self.assertTrue(TestChecker.test(input, expect, 3024))
    
    def test_3025(self):
        input = """
        func foo(string x)
        func main()
        begin
            var m <- foo(5)
        end
        func foo(string x)
            return x * 2
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo), [NumLit(5.0)])"
        self.assertTrue(TestChecker.test(input, expect, 3025))
        
    def test_3026(self):     # DONE
        input = """
            func main()
            begin
                dynamic c <- [1,2,3,4,5,-5,-4,-3,-2,-1] 
            end

        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 3026))

    def test_3027(self):     # DONE
        input = """
            func main()
            begin
                
                number b[3] <- [1,2,3,4,5,-5,-4,-3,-2,-1] 
                dynamic c <- b 
            end

        """
        expect = "Type Mismatch In Statement: VarDecl(Id(b), ArrayType([3.0], NumberType), None, ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0), NumLit(4.0), NumLit(5.0), UnaryOp(-, NumLit(5.0)), UnaryOp(-, NumLit(4.0)), UnaryOp(-, NumLit(3.0)), UnaryOp(-, NumLit(2.0)), UnaryOp(-, NumLit(1.0))))"
        self.assertTrue(TestChecker.test(input, expect, 3027))
    
    def test_3028(self):     
        input = """
            func main()
            begin
                
                number b[2] <- [1,-3] 
                dynamic c <- b 
            end

        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 3028))


    def test_3029(self):     
        input = """
            func foo()
                return [[2,4],5]
            func main()
            begin
    
                dynamic c <- foo()
            end

        """
        expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(NumLit(2.0), NumLit(4.0)), NumLit(5.0))"
        self.assertTrue(TestChecker.test(input, expect, 3029))
    
    def test_3030(self):     # CHECK LATER
        input = """
            func foo()
                return [2,[4,5,"6"]]
            func main()
            begin
    
                dynamic c <- foo()
            end

        """
        expect = "Type Mismatch In Expression: ArrayLit(NumLit(4.0), NumLit(5.0), StringLit(6))"
        self.assertTrue(TestChecker.test(input, expect, 3030))
    
    def test_3031(self):     # CHECK LATER
        input = """
            func foo(string s)
            begin
                if (s == "abc") return s
                if (s == "xyz") return "x"
                elif ((s..."abc") == "xxxabc") return true
                else
                    begin
                        var x <- "string"
                        return x
                        return 123
                    end
            end

            func main()
            begin
    
                dynamic c <- foo()
            end

        """
        expect = "Type Mismatch In Statement: Return(BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 3031))
    
    def test_3032(self):     
        input = """
            func foo(string s)
            begin
                if (s == "abc") return s
                if (s == "xyz") return "x"
                elif ((s..."abc") == "xxxabc") return ""
                else
                    begin
                        var x <- "string"
                        return x
                        return 123
                    end
            end

            func main()
            begin
    
                dynamic c <- foo("xxx")
            end

        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 3032))
    
    def test_3033(self):     
        input = """
            func foo(string s)
            begin
                if (s == "abc") return
                if (s == "xyz") return 
                elif ((s..."abc") == "xxxabc") return 
                else
                    begin
                        var x <- "string"
                        return 
                        return 123
                    end
            end

            func main()
            begin
    
                dynamic c <- foo("xxx")
            end

        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo), [StringLit(xxx)])"
        self.assertTrue(TestChecker.test(input, expect, 3033))
    
    def test_3034(self):     
        input = """
            func foo(string s)
            begin
                if (s == "abc") return s
                if (s == "xyz") return 123
                elif ((s..."abc") == "xxxabc") return 
                else
                    begin
                        var x <- "string"
                        return 
                        return 123
                    end
            end

            func main()
            begin
    
                dynamic c <- foo("xxx")
            end

        """
        expect = "Type Mismatch In Statement: Return(NumLit(123.0))"
        self.assertTrue(TestChecker.test(input, expect, 3034))
    
    def test_3035(self):     
        input = """
            func foo(string s)
            begin
                if (s == "abc") return 
                if (s == "xyz") return 456
                elif ((s..."abc") == "xxxabc") return 
                else
                    begin
                        var x <- "string"
                        return 
                        return 123
                    end
            end

            func main()
            begin
    
                dynamic c <- foo("xxx")
            end

        """
        expect = "Type Mismatch In Statement: Return(NumLit(456.0))"
        self.assertTrue(TestChecker.test(input, expect, 3035))
    
    def test_3036(self):     
        input = """
            func foo(string s)
            begin
                if (s == "abc") return s
                if (s == "xyz") return
                elif ((s..."abc") == "xxxabc") return "xxxabc"
                else
                    begin
                        var x <- "string"
                        return 
                        return 123
                    end
            end

            func main()
            begin
    
                dynamic c <- foo("xxx")
            end

        """
        expect = "Type Mismatch In Statement: Return()"
        self.assertTrue(TestChecker.test(input, expect, 3036))
    
    def test_3037(self):     
        input = """
            func foo(string s)
            begin
                if (s == "abc") return ss
                if (s == "xyz") return
                elif ((s..."abc") == "xxxabc") return 
                else
                    begin
                        var x <- "string"
                        return 
                        return 123
                    end
            end

            func main()
            begin
    
                dynamic c <- foo("xxx")
            end

        """
        expect = "Undeclared Identifier: ss"
        self.assertTrue(TestChecker.test(input, expect, 3037))
    
    def test_3038(self):     
        input = """
        func foo(string a)
        
        func foo(string a)
        begin
            return "Hello World"
        end
        
        func main()
        begin
            foo()
        end

        """
        expect = "Type Mismatch In Statement: CallStmt(Id(foo), [])"
        self.assertTrue(TestChecker.test(input, expect, 3038))
    
    def test_3039(self):     
        input = """
        func foo(string a)
        
        func foo(string b)
        begin
            return
        end

        func foo(number a, string b)
        
        func main()
        begin
            foo()
        end

        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 3039))
    
    def test_3040(self):     
        input = """
        func foo(string a)
        func foo1(string b)
        
        func foo1(string b)
        begin
            return 2
        end

        ##func foo(number a, string b)
        
        func main()
        begin
            foo1("x")
        end

        """
        expect = "Type Mismatch In Statement: CallStmt(Id(foo1), [StringLit(x)])"
        self.assertTrue(TestChecker.test(input, expect, 3040))
    
    def test_3041(self):     
        input = """
        func foo(string a)
        func foo1(string b)
        
        func foo1(string b)
        begin
            return
        end

        ##func foo(number a, string b)
        
        func main()
        begin
            foo1("x")
        end

        """
        expect = "No Function Definition: foo"
        self.assertTrue(TestChecker.test(input, expect, 3041))
    
    def test_3042(self):     
        input = """
        
        
        func main()
        begin
            dynamic a
            dynamic b
            dynamic c
            bool c[2,3] <- [a,[true, false, b]]
            a <- 3
            b <- false
        end

        """
        expect = "Redeclared Variable: c"
        self.assertTrue(TestChecker.test(input, expect, 3042))
    
    def test_3043(self):     
        input = """
        
        
        func main()
        begin
            dynamic a
            dynamic b
            dynamic c
            bool d[2,3] <- [a,[true, false, d]]
            a <- 3
            b <- false
        end

        """
        expect = "Undeclared Identifier: d"
        self.assertTrue(TestChecker.test(input, expect, 3043))
    
    def test_3044(self):     
        input = """
        
        
        func main()
        begin
            dynamic a
            dynamic b
            dynamic c
            bool d[2,3] <- [a,[true, false, c]]
            a <- 3
            b <- false
            c <- true
        end

        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(a), NumLit(3.0))"
        self.assertTrue(TestChecker.test(input, expect, 3044))
    
    def test_3045(self):     
        input = """
        
        
        func main()
        begin
            dynamic a
            dynamic b
            dynamic c
            bool d[2,3] <- [a,[true, false, c]]
            a <- [[true,[false]],true]
            b <- false
            c <- true
        end

        """
        expect = "Type Mismatch In Expression: ArrayLit(BooleanLit(True), ArrayLit(BooleanLit(False)))"
        self.assertTrue(TestChecker.test(input, expect, 3045))
    
    def test_3046(self):     
        input = """
        
        
        func main()
        begin
            dynamic a
            dynamic b
            dynamic c
            bool d[2,3] <- [a,[true, false, c]]
            a <- [1,2,3]
            b <- false
            c <- true
        end

        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(a), ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)))"
        self.assertTrue(TestChecker.test(input, expect, 3046))
    
    def test_3047(self):     
        input = """
        
        
        func main()
        begin
            dynamic a
            dynamic b
            dynamic c
            bool d[2,3] <- [a,[true, false, c]]
            a <- [true, true,\\tfalse]
            b <- false
            c <- true
        end

        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 3047))
    
    def test_3048(self):     
        input = """
        number a[1,2] <- [[0.0,0e2]]
        func incr(number x)
            return x + 100
        func main()
        begin
            dynamic b
            number d
            number c <- a[b,incr(d)]
            b <- incr(b)
            d <- "Hello World"
        end

        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(d), StringLit(Hello World))"
        self.assertTrue(TestChecker.test(input, expect, 3048))
    
    def test_3049(self):     
        input = """
        number a[1,2] <- [[0.0,0e2]]
        func incr(number x)
            return x + 100
        func main()
        begin
            dynamic b
            number a
            number c <- a[b,incr(d)]
            b <- incr(b)
            d <- "Hello World"
        end

        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(a), [Id(b), CallExpr(Id(incr), [Id(d)])])"
        self.assertTrue(TestChecker.test(input, expect, 3049))
    
    def test_3050(self):     
        input = """
        number a[1,2] <- [[0.0,0e2]]
        number d
        dynamic b
        func incr(number x)
            return x + 100
        func main()
        begin
            ##string b
            number d
            number c <- a[b,incr(d)]
            b <- incr(b)
            d <- b
        end

        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 3050))
