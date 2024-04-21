# Nguyễn Thành Đạt - 2152506

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
        expect = "No Function Definition: main"
        self.assertTrue(TestChecker.test(input, expect, 602))

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
        expect2 = "Type Mismatch In Expression: ArrayLit(NumLit(2.0), ArrayLit(NumLit(4.0), NumLit(5.0), StringLit(6)))"
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
        expect2 = "Type Mismatch In Expression: ArrayLit(ArrayLit(BooleanLit(True), ArrayLit(BooleanLit(False))), BooleanLit(True))"
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
    
    def test_3051(self):
        '''Source code 1 ver 1.2.2'''     
        input = """
            func areDivisors(number num1, number num2)
                return ((num1 % num2 = 0) or (num2 % num1 = 0))
            ## comment lollll
            func main()             ## comment\\r lollll
                begin
                    var num1 <- readNumber()
                    var num2 <- readNumber()

                    if (areDivisors(num1, num2)) writeString("Yes")
                    else writeString("No")
                end
                ## comment lollll \n"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 3051))
    
    def test_3052(self):
        '''Source code 2 ver 1.2.2'''     
        input = """
            func isPrime(number x)

            func main()
                begin
                    number x <- readNumber()
                    if (isPrime(x)) writeString("Yes")
                    else writeString("No")
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
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 3052))
    
    def test_3053(self):
        '''Block example ver 1.2.2'''     
        input = """
        func main()
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
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 3053))
    
    def test_3054(self):
        '''For example ver 1.2.2'''     
        input = """
        func main()
            begin
                var i <- 0
                for i until i >= 10 by 1
                writeNumber(i)
            end
                """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 3054))
    
    def test_3055(self):
        '''Function example ver 1.2.2'''     
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
        func main()
            begin
                ##number arr[5]
                number x <- foo([-2,-3,5,0,-1.e9], "abc")
            end
                """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 3055))
    
    def test_3056(self):
        '''Index operator example ver 1.2.2'''     
        input = """
        func foo(number x)
            return x % 2

        func main()
            begin
                number a[5] <- [1,2,3,4,5]
                number b[2,4] <- [[1,2,3,4],[-4,-3,-2,-1]]
                a[3 + foo(2)] <- a[b[2, 3]] + 4
            end
                """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 3056))
    
    def test_3057(self):
        '''Array example ver 1.2.2'''     
        input = """
        number a[5] <- [1, 2, 3, 4, 5]
        number b[2, 3] <- [[1, 2, 3], [4, 5, 6]]
        func main()
            begin
                return
            end
                """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 3057))
    
    def test_3058(self):
        input = """
        dynamic a
        func main()
            begin
                return
                a <- a % 3 + (a * (a - "2"))
            end
                """
        expect = "Type Mismatch In Expression: BinaryOp(-, Id(a), StringLit(2))"
        self.assertTrue(TestChecker.test(input, expect, 3058))
    
    def test_3059(self):        # CHECK LATER
        input = """
        func foo(number arg)
        begin
            var arg <- arg ... "abc"
        end
        dynamic a
        func main()
            return
                """
        expect = "Undeclared Identifier: arg"
        expect2 = "Type Mismatch In Expression: BinaryOp(..., Id(arg), StringLit(abc))"
        self.assertTrue(TestChecker.test(input, expect, 3059))
    
    def test_3060(self):        # CHECK LATER
        input = """
        func foo(string arg)
        begin
            var arg <- arg ... "abc"
            arg <- "abc"
        end
        dynamic a
        func main()
            return
                """
        expect = "Undeclared Identifier: arg"
        expect2 = ""
        self.assertTrue(TestChecker.test(input, expect, 3060))
    
    def test_3061(self):        # CHECK LATER
        input = """
        func foo(number arg)
        begin
            string arg <- arg + 2
            arg <- "abc"
        end
        dynamic a
        func main()
            return
                """
        expect = "Undeclared Identifier: arg"
        expect2 = "Type Mismatch In Statement: VarDecl(Id(arg), StringType, None, BinaryOp(+, Id(arg), NumLit(2.0)))"
        self.assertTrue(TestChecker.test(input, expect, 3061))
    
    def test_3062(self):        # CHECK LATER
        input = """
        func foo(number arg)
        begin
            dynamic arg <- arg + 2
            arg <- "abc"
        end
        dynamic a
        func main()
            return
                """
        expect = "Undeclared Identifier: arg"
        expect2 = "Type Mismatch In Statement: AssignStmt(Id(arg), StringLit(abc))"
        self.assertTrue(TestChecker.test(input, expect, 3062))
    
    def test_3063(self):        
        input = """
        func foo(string arg)
        begin
            dynamic arg <- 2.0
            arg <- "abc"
        end
        dynamic a
        func main()
            return
                """
        expect = "Type Mismatch In Statement: AssignStmt(Id(arg), StringLit(abc))"
        self.assertTrue(TestChecker.test(input, expect, 3063))
    
    def test_3064(self):        
        input = """
        func foo(string arg)
        begin
            dynamic a
            dynamic b
            dynamic c
            number arr[3,3,3] <- [a,b,c]
            a <- [[1,2,3],[4,5,6],[7,8,9]]
            b <- [[1,2,3],[4,5,6],[7,8,9]]
            c <- [[1,2,3],[4,5,6],[7,8,9]]
        end
        dynamic a
        func main()
            return
                """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 3064))
    
    def test_3065(self):        
        input = """
        func foo(string arg)
        begin
            dynamic a
            dynamic b
            dynamic c
            dynamic d
            dynamic e
            dynamic f
            number arr[3,3,3] <- [a,b,c]
            a <- [[1,2,3],[4,5,6],[7,8,9]]
            b <- [[1,2,3],[4,5,6],[7,8,9]]
            c <- [d,e,f]
            d <- [1,2,3]
            e <- [1,2,3]
            f <- [1,2,3]
        end
        dynamic a
        func main()
            return
                """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 3065))

    def test_3066(self):         
        input = """
func f(number x)
begin
    if (x % 2 = 0) return 0
    elif (x % 2 = 1) return 1
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
        self.assertTrue(TestChecker.test(input, expect, 3066))
    
    def test_3067(self):         
        input = """
func f(number x[5])
begin
    if (x % 2 = 0) return 0
    elif (x % 2 = 1) return 1
    else return f(x - 1) + f(x - 2)
end
    
func main()
begin
    dynamic a
    number x <- f(a)
    a[0] <- 1
end
"""
        expect = "Type Mismatch In Expression: BinaryOp(%, Id(x), NumLit(2.0))"
        self.assertTrue(TestChecker.test(input, expect, 3067))
    
    def test_3068(self):         
        input = """
func f(number x[5])
begin
    dynamic x
    if (x % 2 = 0) return 0
    elif (x % 2 = 1) return 1
    else return f(x - 1) + f(x - 2)
end
    
func main()
begin
    dynamic a
    number x <- f(a)
    a[0] <- 1
end
"""
        expect = "Type Mismatch In Expression: CallExpr(Id(f), [BinaryOp(-, Id(x), NumLit(1.0))])"
        self.assertTrue(TestChecker.test(input, expect, 3068))
    
    def test_3069(self):         
        input = """
func f(number x[5])
begin
    dynamic x
    if (x % 2 = 0) return 0
    elif (x % 2 = 1) return 1
    else return f(x - 1) + f(x - 2)
end
    
func main()
begin
    dynamic a
    number b
    number x <- f([a,b,3])
    a <- 1
end
"""
        expect = "Type Mismatch In Expression: CallExpr(Id(f), [BinaryOp(-, Id(x), NumLit(1.0))])"
        self.assertTrue(TestChecker.test(input, expect, 3069))
        
    def test_3070(self):         
        input = """
func f(number x[5])
begin
    return f(x) + f(x)
end
    
func main()
begin
    dynamic a
    number x <- f(a)
    a[0] <- 1
end
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 3070))
    
    def test_3071(self):         
        input = """
func f(number x[5])
begin
    return f(x) + f(x)
end
    
func main()
begin
    dynamic a
    a[0] <- 1
end
"""
        expect = "Type Cannot Be Inferred: AssignStmt(ArrayCell(Id(a), [NumLit(0.0)]), NumLit(1.0))"
        self.assertTrue(TestChecker.test(input, expect, 3071))
    
    def test_3072(self):         
        input = """
func f(number x[5])
begin
    return f(x) + f(x)
end
    
func main()
begin
    dynamic a
end
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 3072))
    
    def test_3073(self):         
        input = """
func f(number x[5])
begin
    return f(x) + f(x)
end
    
func main()
begin
    dynamic a
    f(a)
end
"""
        expect = "Type Mismatch In Statement: CallStmt(Id(f), [Id(a)])"
        self.assertTrue(TestChecker.test(input, expect, 3073))
    
    def test_3074(self):         
        input = """
func f(number x[5])
begin
    return f(x)
end
    
func main()
begin
    dynamic a
    a <- f(a) ... "0"
end
"""
        expect = "Type Cannot Be Inferred: Return(CallExpr(Id(f), [Id(x)]))"
        self.assertTrue(TestChecker.test(input, expect, 3074))
    
    def test_3075(self):         
        input = """
func f(number x[5])
begin
    return "f(x)"
end
    
func main()
begin
    dynamic a
    dynamic b
    b[10] <- f(a) ... "0"
end
"""
        expect = "Type Cannot Be Inferred: AssignStmt(ArrayCell(Id(b), [NumLit(10.0)]), BinaryOp(..., CallExpr(Id(f), [Id(a)]), StringLit(0)))"
        self.assertTrue(TestChecker.test(input, expect, 3075))
    
    def test_3076(self):         
        input = """
func f(number x[5])
begin
    return x[11]
end
    
func main()
begin
    dynamic a
    a[10] <- f(a) / 0
end
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 3076))
    
    def test_3077(self):
        input = """
func f()
    
func main()
begin
    bool fx <- f() and f()
end
"""
        expect = "No Function Definition: f"
        self.assertTrue(TestChecker.test(input, expect, 3077))
    
    def test_3078(self):         # CHECK LATER
        input = """
func f()
begin
    return true
end
    
func main()
begin
    bool f <- f() and f()
end
"""
        expect = "Type Mismatch In Expression: CallExpr(Id(f), [])"
        self.assertTrue(TestChecker.test(input, expect, 3078))
    
    def test_3079(self):         # CHECK LATER
        input = """
func g(number f)
begin
    f()
end

func f()
    
func main()
begin
    
end
"""
        expect = "Type Mismatch In Statement: CallStmt(Id(f), [])"
        self.assertTrue(TestChecker.test(input, expect, 3079))
    
    def test_3080(self):         
        input = """
    func f(number x)
    begin
        dynamic a
        string b[4]
        dynamic c <- b[a]
        bool d <- c == ""
        bool e <- not a
    end
    func main()
    begin
        f(1)
    end
    
    """
        expect = "Type Mismatch In Expression: UnaryOp(not, Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 3080))
    
    def test_3081(self):         
        input = """
    func f(number x)
    begin
        dynamic x
        string b[4]
        bool e <- not x
        dynamic c <- b[x]
        bool d <- c == ""
    end
    func main()
    begin
        f(1)
    end
    
    """
        expect = "Type Mismatch In Expression: ArrayCell(Id(b), [Id(x)])"
        self.assertTrue(TestChecker.test(input, expect, 3081))
    
    def test_3082(self):         
        input = """
    func f(number x)
    begin
        dynamic a <- x
        dynamic b <- [[1,2,3], a]
        var c <- a[0]
        var d <- a
    end
    func main()
    begin
        f(1)
    end
    
    """
        expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)), Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 3082))
    
    def test_3083(self):         
        input = """
    func main()
    func f(number x)
    begin
        dynamic a
        dynamic b <- [[1,2,3], a]
        var c <- a[0]
        var d <- a
    end
    func main()
    begin
        f(1)
    end
    
    """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 3083))
    
    def test_3084(self):         
        input = """
    func foo(string a) 
    begin
        dynamic a
        return a
    end
    func main() return
    
    """
        expect = "Type Cannot Be Inferred: Return(Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 3084))
    
    def test_3085(self):      
        '''visitBinaryOp: left first or right first?'''   
        input = """
        func main()
        func main()
            begin
                dynamic num
                bool a <- num and (num > num)
            end
        """
        expect = "Type Mismatch In Expression: BinaryOp(>, Id(num), Id(num))"
        self.assertTrue(TestChecker.test(input, expect, 3085))
    
    def test_3086(self):
        input = """
        func f()
        begin
            number c[3,2] <- [[6,7],[4,5],[4,5]]
            return c[2,0]
        end

        func main()
            begin
                dynamic a <- f()
                a <- 3
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 3086))
    
    def test_3087(self): 
        input = """
        func f()
        begin
            number c[3,2] <- [[-6,7],[12,81],[144,-55]]
            return c[5]
        end

        func main()
            begin
                dynamic a <- f()
                a <- a
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 3087))
    
    def test_3088(self):  
        input = """
        func f()
        begin
            number c[3,2] <- [[-6,7],[12,81],[144,-55]]
            return c[5]
        end

        func main()
            begin
                dynamic a <- f()
                a <- [8,7]
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 3088))

    def test_3089(self):       # DONE
        input = """
func main()
begin
    var x <- [[[[1, 2]], [3, 4, 5]], [[6, 7, 8], [9, 10, 11]]]
    writeNumber(x)
end
"""
        expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0))), ArrayLit(NumLit(3.0), NumLit(4.0), NumLit(5.0)))"
        expect2 = "Type Mismatch In Expression: ArrayLit(ArrayLit(ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0))), ArrayLit(NumLit(3.0), NumLit(4.0), NumLit(5.0))), ArrayLit(ArrayLit(NumLit(6.0), NumLit(7.0), NumLit(8.0)), ArrayLit(NumLit(9.0), NumLit(10.0), NumLit(11.0))))"
        self.assertTrue(TestChecker.test(input, expect, 3089))
    
    def test_3090(self):
        input = """
func main()
begin
    var x <- [[[1,2]],[3,4]]
    writeNumber(x)
end
"""
        expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0))), ArrayLit(NumLit(3.0), NumLit(4.0)))"
        self.assertTrue(TestChecker.test(input, expect, 3090))
    
    def test_3091(self):
        input = """
func main()
begin
    var x <- [[[1,true]],[3,4]]
    writeNumber(x)
end
"""
        expect = "Type Mismatch In Expression: ArrayLit(NumLit(1.0), BooleanLit(True))"
        expect2 = "Type Mismatch In Expression: ArrayLit(ArrayLit(ArrayLit(NumLit(1.0), BooleanLit(True))), ArrayLit(NumLit(3.0), NumLit(4.0)))"
        self.assertTrue(TestChecker.test(input, expect, 3091))
    
    def test_3092(self):
        input = """

func main()
begin
    number arr[10] <- [1,4,1,5,7,8,9,3,2,10]
    
    continue
end
"""
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 3092))
    
    def test_3093(self):
        input = """

func main()
begin
    number arr[10] <- [1,4,1,5,7,8,9,3,2,10]
    break
    continue
end
"""
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 3093))
    
    def test_3094(self):
        '''test_40 ASTGenSuite'''
        input = """
func swap(number a, number b)
begin
    number temp <- a
    a <- b
    b <- temp
end

func partition(number arr[10], number start, number _end)
begin
	number pivot <- arr[start]

	number count <- 0
    number i
    number j
    i <- start + 1
	for i until i > _end by 1
		if (arr[i] <= pivot)
			count <- count + 1

	## Giving pivot element its correct position
	number pivotIndex <- start + count
	swap(arr[pivotIndex], arr[start])

	## Sorting left and right parts of the pivot element
    i <- start
    j <- _end

	return pivotIndex
end

func quickSort(number arr[10], number start, number _end)
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

func main()
begin
    number arr[10] <- [1,4,1,5,7,8,9,3,2,10]
    quickSort(arr, arr[0], arr[10])
end
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 3094))
    
    def test_3095(self):
        '''test_64 ASTGenSuite'''
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
            writeNumber(num)
            writeString(" ")
        end
        else
        begin
            ord1 <- num % 10
            ord2 <- (num % 100 - ord1) / 10
            ord3 <- (num % 1000 - ord2) / 100
 
            total_sum <- ((ord1 * ord1 * ord1) + (ord2 * ord2 * ord2) + (ord3 * ord3 * ord3))
            if (total_sum = num)
            begin
                writeNumber(num)
                writeString(" ")
            end
        end
    end
end
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 3095))
    
    def test_3096(self):
        '''test_65 ASTGenSuite'''
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
        if (rows = 1) begin
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
        if (rows = 1) begin
            writeString("\\\\n")
        end
        else begin
            writeString("*\\\\n")
        end
    end
end
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 3096))
    
    def test_3097(self):
        '''test_77 ASTGenSuite'''
        input = """
number n
func binarySearch(number arr[5], number low, number high, number x) 
begin 
    ## Base case: If the search space becomes empty, the 
    ## element is not present in the array 
    if (high >= low) begin 
        ## Calculate the middle index to divide the search 
        ## space in half 
        number mid <- low + (high - low) / 2 
  
        ## If the middle element is equal to 'x', we have 
        ## found the element, return its index 
        if (arr[mid] = x) 
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
   
    number result <- binarySearch(arr, arr[0], arr[4], x)
    if (result = -1) 
        writeString("Element is not present in array" )
    else
        writeString("Element is present at index ")
        writeNumber(result)
end
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 3097))
    
    def test_3098(self):
        '''test_72 ASTGenSuite'''
        input = """
## Swap function
func swap(number a, number b)
begin
    number temp <- a
    a <- b
    b <- temp
end
 
## An optimized version of Bubble Sort
func bubbleSort(number arr[8], number n)
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
                swap(arr[j], arr[j + 1])
                ## swapped is set to true if the swap is
                ## done
                swapped <- true
            end
        end
 
        ## If no two elements were swapped
        ## by inner loop, then break
        if (not swapped)
            break
    end
end
 
## Function to print an array
func printArray(number arr[8], number size)
begin
    number i <- 0
    for i until i >= size by 1
    begin
        writeNumber(arr[i])
        writeString(" ")
    end
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
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 3098))
    
    def test_3099(self):
        '''test_93 ASTGenSuite'''
        input = """ 
## This function returns new size of modified array
func removeDuplicates(number arr[10], number n) 
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
    dynamic n <- removeDuplicates(arr, 10) 
  
    ## Print updated array 
    number i <- 0
    for i until i >= n by 1 begin
        writeNumber( arr[i] )
        writeString(  \t  \t" " )
        end
end 
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 3099))
    
    def test_3100(self):
        input = """
func str(number date)
    return date

func main()
begin
    writeNumber(21-04-2024)
end
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 3100))