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

    def __(self):
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

#===============================================================

    def test_3001(self):
        input = """
        dynamic a
        dynamic b
        dynamic c
        number arr[2,3] <- [[a,b],[3,4]]
        func main()
            return
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 3001))
    
    def test_3002(self):
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
        expect = "Redeclared Identifier: foo"
        self.assertTrue(TestChecker.test(input, expect, 3002))
    
    def test_3003(self):
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
    
    def test_3004(self):
        input = """
        func main()
            return

        dynamic a
        number b <- a[0]
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 3004))
    
    def test_3005(self):
        input = """
        func main()
            return

        dynamic a
        var b <- a[0]
        """
        expect = "Type Cannot Be Inferred: "
        self.assertTrue(TestChecker.test(input, expect, 3005))
