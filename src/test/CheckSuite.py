import unittest
from TestUtils import TestChecker
from AST import *


class CheckSuite(unittest.TestCase):
#     def test_no_entry_point(self):
#         input = """number a
#         """
#         expect = "No Entry Point"
#         self.assertTrue(TestChecker.test(input, expect, 400))
    
#     def test_no_entry_point_2(self):
#         input = """
#         number a
#         number b

#         """
#         expect = "No Entry Point"
#         self.assertTrue(TestChecker.test(input, expect, 601))
    
#     def test_no_entry_point_3(self):
#         input = """
#         number a
#         number b
#         func main()
#         """
#         expect = "No Entry Point"
#         self.assertTrue(TestChecker.test(input, expect, 602))

    def test_603(self):       # CHECK LATER
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

#     def test_604(self):         # DONE
#         input = """
# func f(number x)
# begin
#     if (x = 0) return 0
#     elif (x = 1) return 1
#     else return f(x - 1) + f(x - 2)
# end
    
# func main()
# begin
#     dynamic a
#     number x <- f(a)
#     a[0] <- [1, 2, 3]
# end
# """
#         expect = "Type Mismatch In Expression: ArrayCell(Id(a), [NumLit(0.0)])"
#         myret_ = "Undeclared Function: a"
#         self.assertTrue(TestChecker.test(input, expect, 604))

#===============================================================

    # def test_3001(self):    # DONE
    #     input = """
    #     dynamic a
    #     dynamic b
    #     dynamic c
    #     number arr[2,2] <- [[a,b],[3,4]]
    #     func main()
    #         return
    #     """
    #     expect = "Type Mismatch In Statement: VarDecl(Id(arr), ArrayType([2.0, 2.0], NumberType), None, ArrayLit(ArrayLit(Id(a), Id(b)), ArrayLit(NumLit(3.0), NumLit(4.0))))"
    #     self.assertTrue(TestChecker.test(input, expect, 3001))
    
    # def test_3002(self):        # DONE
    #     input = """
    #     func foo()
    #     number foo

    #     func main()
    #     begin
    #         foo()
    #         return
    #     end

    #     func foo()
    #     begin
    #         number a
    #     end
    #     """
    #     expect = "Redeclared Variable: foo"
    #     self.assertTrue(TestChecker.test(input, expect, 3002))
    
    # def test_3003(self):        # DONE
    #     input = """
    #     number foo
    #     func foo()

    #     func main()
    #     begin
    #         foo()
    #         return
    #     end

    #     func foo()
    #     begin
    #         number a
    #     end
    #     """
    #     expect = "Redeclared Function: foo"
    #     self.assertTrue(TestChecker.test(input, expect, 3003))
    
    # def test_3004(self):        # CHECK LATER
    #     input = """
    #     func main()
    #         return

    #     dynamic a
    #     number b <- a[0]
    #     """
    #     expect = "Type Cannot Be Inferred: VarDecl(Id(b), NumberType, None, ArrayCell(Id(a), [NumLit(0.0)]))"
    #     self.assertTrue(TestChecker.test(input, expect, 3004))
    
    # def test_3005(self):        # DONE
    #     input = """
    #     func main()
    #         return

    #     dynamic a
    #     var b <- a[0]
    #     """
    #     expect = "Type Cannot Be Inferred: VarDecl(Id(b), None, var, ArrayCell(Id(a), [NumLit(0.0)]))"
    #     self.assertTrue(TestChecker.test(input, expect, 3005))
    
    # def test_3006(self):        # DONE
    #     input = """
    #     func main()
    #     begin
    #         number arr[2] <- [3,4]
    #     end
    #     """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 3006))
    
    # def test_3007(self):        # DONE
    #     input = """
    #     func main()
    #         number arr[2] <- ["3",4]
    #     """
    #     expect = "Type Mismatch In Expression: ArrayLit(StringLit(3), NumLit(4.0))"
    #     self.assertTrue(TestChecker.test(input, expect, 3007))
    
    # def test_3008(self):        # DONE
    #     input = """
    #     func main()
    #         number arr[2,2] <- [[3,5],4]
    #     """
    #     expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(NumLit(3.0), NumLit(5.0)), NumLit(4.0))"
    #     self.assertTrue(TestChecker.test(input, expect, 3008))
