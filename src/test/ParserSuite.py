import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_a(self):
        input = """var a <- true[3,4]
        """
        expect = """Error on line 1 col 13: ["""
        self.assertTrue(TestParser.test(input,expect,401))
    
    def test_b(self):
        input = """
func main()
func main1()
    begin
        func main2()
            return
    end
        """
        expect = """Error on line 5 col 8: func"""
        self.assertTrue(TestParser.test(input,expect,402))
    
    def test_c(self):
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
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,403))
    
    def test_d(self):
        input = """
number a <- b[1][2] + c
"""
        expect = """Error on line 2 col 16: ["""
        self.assertTrue(TestParser.test(input,expect,404))
    
    def test_e(self):
        input = """
number a[3] <- b[1] + c
number b[3] <- (a+b+c)[3]
"""
        expect = """Error on line 3 col 22: ["""
        # expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,405))
    
    def test_f(self):
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
        expect = """successful"""
        # expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,406))

    def test_1001(self):
        """test 1001 Source code 1"""
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,1001))

    def test_1002(self):
        """test 1002 Source code 2"""
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,1002))

    def test_1003(self):
        """test 1003"""
        input = """
            

\n\n\n
\\n

                """
        expect = "Error on line 10 col 16: <EOF>"
        self.assertTrue(TestParser.test(input,expect,1003))

    def test_1004(self):
        """test 1004"""
        input = """
for i until i > x / 2 by 1
begin

end

                """
        expect = "Error on line 2 col 0: for"
        self.assertTrue(TestParser.test(input,expect,1004))

    def test_1005(self):
        """test 1005"""
        input = """
            func isPrime(number x)

            func main()
                begin \\t
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
                return true   \\n             end
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,1005))

    def test_1006(self):
        """test 1006"""
        input = """string s <- writeString("Hello this is a '"test'"") \\n"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,1006))

    def test_1007(self):
        """test 1007"""
        input = """func foo(number arr[1,2,3])
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,1007))

    def test_1008(self):
        """test 1008"""
        input = """
func foo()
    begin
        number arr[3, foo(5)*4,6]
    end
        """
        expect = "Error on line 4 col 22: foo"
        self.assertTrue(TestParser.test(input,expect,1008))

    def test_1009(self):
        """test 1009"""
        input = """
func foo()
    begin
        number arr[3, 3,1] <- [b[9,20][0][c[25]] + 5, foo(6), "abc"]
    end
        """
        expect = "Error on line 4 col 38: ["
        self.assertTrue(TestParser.test(input,expect,1009))

    def test_1010(self):
        """test 1010"""
        input = """
func foo()
    begin
        func foo2(number a)
    end
        """
        expect = "Error on line 4 col 8: func"
        self.assertTrue(TestParser.test(input,expect,1010))

    def test_1011(self):
        """test 1011"""
        input = """
func foo()
    begin
        number __abc[2]
        var bca <- 81[3] + ag[2]
    end
        """
        expect = "Error on line 5 col 21: ["
        self.assertTrue(TestParser.test(input,expect,1011))
    
    def test_1012(self):
        """test 1012"""
        input = """
func foo()
    begin
        if (a < b) if (c < d) bool e
    end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,1012))
    
    def test_1013(self):
        """test 1013"""
        input = """func foo()
        begin
        string c <- "\\???mmp"
        end
        """
        expect = '\\?'
        self.assertTrue(TestParser.test(input,expect,1013))

    def test_1014(self):
        """test 1014"""
        input = """
func foo()
    begin
        number a[5] <- [1, 2, 3, 4, 5, "__abc", _ksdjaksjd]
        number b[2, 3] <- [[1, 2, 3], [4, 5, 6, abcxyz, _lololol, UsjdOewu721_3hjsA], false, 812jsdjak_sj]
    end
        """
        expect = "Error on line 5 col 96: jsdjak_sj"
        self.assertTrue(TestParser.test(input,expect,1014))

    def test_1015(self):
        """test 1015"""
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,1015))

    def test_1016(self):
        """test 1016"""
        input = """
        var a <- [abc,xyz]
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,1016))

    def test_1017(self):
        """test 1017"""
        input = """
var a
        """
        expect = "Error on line 2 col 5: \n"
        self.assertTrue(TestParser.test(input,expect,1017))

    def test_1018(self):
        """test 1018"""
        input = """
string a <- expr()[2] + [1,"kfc",E][1,4,[]]
        """
        expect = "Error on line 2 col 35: ["
        self.assertTrue(TestParser.test(input,expect,1018))

    def test_1019(self):
        """test 1019"""
        input = """
func fooooooo ()


	return "fool'"'"'"fool"


dynamic a1

var a2

"""
        expect = """Error on line 10 col 6: 
"""
        self.assertTrue(TestParser.test(input, expect, 1019))
    
    def test_1020(self):
        """test 1020"""
        input = """\n
        """
        expect = """Error on line 3 col 8: <EOF>"""
        self.assertTrue(TestParser.test(input, expect, 1020))

    def test_1021(self):
        """test 1021"""
        input = "        \\n  "
        expect = """Error on line 1 col 12: <EOF>"""
        self.assertTrue(TestParser.test(input, expect, 1021))

    def test_1022(self):
        """test 1022"""
        input = """##number a\nnumber a\n##\\n var b\n"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 1022))

    def test_1023(self):
        """test 1023"""
        input = """

"""
        expect = """Error on line 3 col 0: <EOF>"""
        self.assertTrue(TestParser.test(input, expect, 1023))

    def test_1024(self):
        """test 1024"""
        input = """

func foo()
begin
askdjas <- 123.e-3
if (abc) 
number foo() <- 8910
end
"""
        expect = """Error on line 7 col 10: ("""
        self.assertTrue(TestParser.test(input, expect, 1024))

    def test_1025(self):
        """test 1025"""
        input = """
            var engineergaming123
"""
        expect = """Error on line 2 col 33: 
"""
        self.assertTrue(TestParser.test(input, expect, 1025))
    
    def test_1026(self):
        """test 1026"""
        input = """
            var _123engineergaming123
"""
        expect = """Error on line 2 col 37: 
"""
        self.assertTrue(TestParser.test(input, expect, 1026))
    
    def test_1027(self):
        """test 1027"""
        input = """
            var engineergaming123 <- 123e2xyz
"""
        expect = """Error on line 2 col 42: xyz"""
        self.assertTrue(TestParser.test(input, expect, 1027))
    
    def test_1028(self):
        """test 1028"""
        input = """
            var engineergaming123<-e2xyz
            func foo() begin\nend
"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 1028))
    
    def test_1029(self):
        """test 1029"""
        input = """
            var engineergaming123<-e2xyz
            func foo() begin\n\n\n\n\r\n\r\r\rend
"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 1029))
    
    def test_1030(self):
        """test 1030"""
        input = """
            var engineergaming123<-e2xyz
            func foo() begin\n\n\n\n

    \t\r\\rend
"""
        expect = """Error on line 9 col 6: \\r"""
        self.assertTrue(TestParser.test(input, expect, 1030))

    def test_1031(self):
        """test 1031"""
        input = """
        begin
        end
        """
        expect = "Error on line 2 col 8: begin"
        self.assertTrue(TestParser.test(input,expect,1031))
    
    def test_1032(self):
        """test 1032"""
        input = """
        func ##dkkj239090 
        isPrime(number x)
        ##abc dkfjkl9292&23u56^&&i-p;sw;]
        ##83kIW*921o [ ID))@_} ]

        """
        expect = "Error on line 2 col 26: \n"
        self.assertTrue(TestParser.test(input,expect,1032))
    
    def test_1033(self):
        """test 1033"""
        input = """

        ##abc dkfjkl9292&23u56^&&i-p;sw;]
        ##83kIW*921o [ ID))@_} ]
        

        """
        expect = "Error on line 7 col 8: <EOF>"
        self.assertTrue(TestParser.test(input,expect,1033))
    
    def test_1034(self):
        """test 1034"""
        input = """

        ##abc dkfjkl9292&23u56^&&i-p;sw;]
        ##83kIW*921o [ ID))@_} ]
        ##uuuuuuuuuuuu"""
        expect = "Error on line 5 col 22: <EOF>"
        self.assertTrue(TestParser.test(input,expect,1034))
    
    def test_1035(self):
        """test 1035"""
        input = """

        ##abc dkfjkl9292&23u56^&&i-p;sw;]
        ##83kIW*921o [ ID))@_} ]
        #uuuuuuuuuuuu"""
        expect = "#"
        self.assertTrue(TestParser.test(input,expect,1035))
    
    def test_1036(self):
        """test 1036"""
        input = """"""
        expect = "Error on line 1 col 0: <EOF>"
        self.assertTrue(TestParser.test(input,expect,1036))
    
    def test_1037(self):
        """test 1037"""
        input = """##"""
        expect = "Error on line 1 col 2: <EOF>"
        self.assertTrue(TestParser.test(input,expect,1037))
    
    def test_1038(self):
        """test 1038"""
        input = """
func main()
        begin   \\n  var i <- 0\nfoo()[3 + foo(2)] <- a[b[2, 3]] + 4
    end\\n"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,1038))
    
    def test_1039(self):
        """test 1039"""
        input = """
func main()      \n  """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,1039))

    def test_1040(self):
        """test 1040 Simple program: int main() {} """
        input = """func main () return 1
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,1040))
    
    def test_1041(self):
        """test 1041"""
        input = """func main () return (expr1 * expr2 == abc..."xyz"..."mno")
        """
        expect = "Error on line 1 col 49: ..."
        self.assertTrue(TestParser.test(input,expect,1041))
    
    def test_1042(self):
        """test 1042"""
        input = """func main ()
        number x1 = 5
        """
        # expect = "Error on line 2 col 8: number"
        expect = "Error on line 2 col 18: ="
        self.assertTrue(TestParser.test(input,expect,1042))
    
    def test_1043(self):
        """test 1043"""
        input = """func main ()    begin
        number x1 = 5 \n   end
        """
        expect = "Error on line 2 col 18: ="
        self.assertTrue(TestParser.test(input,expect,1043))
    
    def test_1044(self):
        """test 1044"""
        input = """func main ()    begin
        number x1<-5 \r\n dynamic x2 = foo(0)  
        end
        """
        expect = "Error on line 3 col 12: ="
        self.assertTrue(TestParser.test(input,expect,1044))
    
    def test_1045(self):
        """test 1045"""
        input = """
func main(string a) 
    begin 
        break ## 12345678
    end
func main(dynamic a) 
        """
        expect = "Error on line 6 col 10: dynamic"
        self.assertTrue(TestParser.test(input,expect,1045))
    
    def test_1046(self):
        """test 1046"""
        input = """
func main(string a <- "abc") 
    begin 
        break ## 12345678
    end
func main(number a) 
        """
        expect = "Error on line 2 col 19: <-"
        self.assertTrue(TestParser.test(input,expect,1046))
    
    def test_1047(self):
        """test 1047"""
        input = """
func main(string a) 
    begin 
        break x ## 12345678
    end
func main(number a) 
        """
        expect = "Error on line 4 col 14: x"
        self.assertTrue(TestParser.test(input,expect,1047))
    
    def test_1048(self):
        """test 1048"""
        input = """
func main(string a) 
    foo(3,5)
func main(number a) 
        """
        expect = "Error on line 3 col 4: foo"
        self.assertTrue(TestParser.test(input,expect,1048))
    
    def test_1049(self):
        """test 1049"""
        input = """
number a <- "kdoqqw123" + 42E24
bool b <- true and false or not not s[20]
string c <- [r,t,x[3]]
var d <- [3,4,[5,6,7],[8,9,0]] + [[23]]
dynamic e
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,1049))
    
    def test_1050(self):
        """test 1050"""
        input = """
number a <- "kdoqqw123" + 42E24
bool b <- true and false or not (not s[20] and 7E3)
string c <- ([r,t,x[3]])
dynamic e <- abc
var d <- [3,4,[5,6,7],[8,9,0]] + [foo[23],_foo(string)[1]]
        """
        expect = "Error on line 6 col 47: string"
        self.assertTrue(TestParser.test(input,expect,1050))
    
    def test_1051(self):
        """test 1051"""
        input = """
number a <- "kdoqqw123" + 42E24
bool b <- true and false or not (not s[20] and 7E3)
string c <- ([r,t,x[3]])
dynamic e <- abc
var d <- [3,4,[5,6,7],[8,9,0]] + [foo[23],_foo(str)[foo()]]
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,1051))
    
    def test_1052(self):
        """test 1052"""
        input = """
number a <- "kdoqqw123" + +42E+24
bool b <- true and false or not (not s[20] and 7E3)
string c <- ([r,t,x[3]])
dynamic e <- abc
var d <- [3,4,[5,6,7],[8,9,0]] + [foo[23],_foo(str)[foo()]]
        """
        expect = "Error on line 2 col 26: +"
        self.assertTrue(TestParser.test(input,expect,1052))
    
    def test_1053(self):
        """test 1053"""
        input = """
func foo()
    begin
        if (not x)
            return ---(--1)
    end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,1053))
    
    def test_1054(self):
        """test 1054"""
        input = """
func foo()
    begin
        if ((x <= (y > z) ... "abc") ... ["xyz"...foo()])
            return ---(--1)
    end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,1054))
    
    def test_1055(self):
        """test 1055"""
        input = """
func foo()
    begin
        if ((x <= (y > z) ... "abc") ... ["xyz"...foo([[1,23,4],[2,"abc'"abc"]])])
            return ---(--1)
    end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,1055))
    
    def test_1056(self):
        """test 1056"""
        input = """
func foo()
    begin
        number x <- foo(,)
    end
        """
        expect = "Error on line 4 col 24: ,"
        self.assertTrue(TestParser.test(input,expect,1056))
    
    def test_1057(self):
        """test 1057"""
        input = """
func foo()
    begin
        number x <- foo(abc,)
    end
        """
        expect = "Error on line 4 col 28: )"
        self.assertTrue(TestParser.test(input,expect,1057))
    
    def test_1058(self):
        """test 1058"""
        input = """
func foo()
    begin
        number x <- foo(abc,[,])
    end
        """
        expect = "Error on line 4 col 29: ,"
        self.assertTrue(TestParser.test(input,expect,1058))
    
    def test_1059(self):
        """test 1059"""
        input = """
func foo()
    begin
        number x <- foo(abc,[E3,_21,])
    end
        """
        expect = "Error on line 4 col 36: ]"
        self.assertTrue(TestParser.test(input,expect,1059))
    
    def test_1060(self):
        """test 1060 ver. 1.0.0"""
        input = """
func foo()
    begin
        aPI <- 3.14
        value <- x%[foo(5)]
        l[3] <- value * aPi
    end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,1060))
    
    def test_1061(self):
        """test 1061 ver. 1.0.0"""
        input = """
func foo()
    begin
        aPI <- 3.14
        value \\n<- x%[foo(5)]
        l[3] <- value * aPi
    end
        """
        expect = "Error on line 5 col 14: \\n"
        self.assertTrue(TestParser.test(input,expect,1061))
    
    def test_1062(self):
        """test 1062 ver. 1.0.0"""
        input = """
func foo()
    begin
        aPI <- 3.14\\nvalue \\n<- x%[foo(5)]
        l[3] <- value * aPi
    end
        """
        expect = "Error on line 4 col 27: \\n"
        self.assertTrue(TestParser.test(input,expect,1062))
    
    def test_1063(self):
        """test 1063 ver. 1.0.0"""
        input = """
func foo()
    begin
        aPI <- 3.14\\rvalue \\n<- x%[foo(5)]
        l[3] <- value * aPi
    end
        """
        expect = "Error on line 4 col 19: \\r"
        self.assertTrue(TestParser.test(input,expect,1063))
    
    def test_1064(self):
        """test 1064 ver. 1.0.0"""
        input = """
func foo(number a[5], string b)
begin
var i <- 0
for i until (((i)) >= 5) by (1))
begin
a[i] <- i * i + 5
end
return -1
end
        """
        expect = "Error on line 5 col 31: )"
        self.assertTrue(TestParser.test(input,expect,1064))
    
    def test_1065(self):
        """test 1065 ver. 1.0.0"""
        input = """
func foo(number a[5], string b)
begin
var i <- 0
for i until (i) >= 5) by (1)
begin
a[i] <- i * i + 5
end
return -1
end
        """
        expect = "Error on line 5 col 20: )"
        self.assertTrue(TestParser.test(input,expect,1065))
    
    def test_1066(self):
        """test 1066 ver. 1.0.0"""
        input = """
func foo(number a[5], string b)
begin
var i <- 0
for i until ((i) >= 5 by (1))
begin
a[i] <- i * i + 5
end
return -1
end
        """
        expect = "Error on line 5 col 22: by"
        self.assertTrue(TestParser.test(input,expect,1066))
    
    def test_1067(self):
        """test 1067 ver. 1.2.2"""
        input = """
func foo()
begin
var i <- 0
for i until i >= 10 by 1
writeNumbe(i)
end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,1067))
    
    def test_1068(self):
        """test 1068 ver. 1.2.2"""
        input = """
func foo()
begin
number i[[1,2],3] <- 0
for i until i >= 10 by 1
writeNumbe(i)
end
        """
        expect = "Error on line 4 col 9: ["
        self.assertTrue(TestParser.test(input,expect,1068))
    
    def test_1069(self):
        """test 1069 ver. 1.2.2"""
        input = """
func foo()
begin
number i[1,2,3] <- [[1,2],3]
for i until i >= 10 by 1
writeNumbe(i)
end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,1069))
    
    def test_1070(self):
        """test 1070 ver. 1.2.2"""
        input = """
func foo()
begin
number i[5abc] <- [abc]
for i until i >= 10 by 1
writeNumbe(i)
end
        """
        expect = "Error on line 4 col 10: abc"
        self.assertTrue(TestParser.test(input,expect,1070))
    
    def test_1071(self):
        """test 1071 ver. 1.2.2"""
        input = """
func foo()
begin
number i[-5e-4] <- [abc]
for i until i >= 10 by 1
writeNumbe(i)
end
        """
        expect = "Error on line 4 col 9: -"
        self.assertTrue(TestParser.test(input,expect,1071))
    
    def test_1072(self):
        """test 1072 ver. 1.2.2"""
        input = """
func foo()
begin
number i[5e-4] <- ["a"[abc]]
for i until i >= 10 by 1
writeNumbe(i)
end
        """
        expect = "Error on line 4 col 22: ["
        self.assertTrue(TestParser.test(input,expect,1072))
    
    def test_1073(self):
        """test 1073 ver. 1.2.2"""
        input = """
func foo()
begin
number i[5e-4] <- [[foo()[abc]]
for i until i >= 10 by 1
writeNumbe(i)
end
        """
        expect = "Error on line 4 col 31: \n"
        self.assertTrue(TestParser.test(input,expect,1073))
    
    def test_1074(self):
        """test 1074 ver. 1.2.2"""
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,1074))
    
    def test_1075(self):
        """test 1075 ver. 1.2.2"""
        input = """
func foo()
    begin
        number r,s,t,foo2
        number s
        r <- 2.0
        number a[5]
        number b[5]
        s <- r * r * 3.14
        a[0] <- s
    end
        """
        expect = "Error on line 4 col 16: ,"
        self.assertTrue(TestParser.test(input,expect,1075))
    
    def test_1076(self):
        """test 1076 ver. 1.2.2"""
        input = """
func foo()
    begin
        number r()
        number s
        r <- 2.0
        number a[5]
        number b[5]
        s <- r * r * 3.14
        a[0] <- s
    end
        """
        expect = "Error on line 4 col 16: ("
        self.assertTrue(TestParser.test(input,expect,1076))
    
    def test_1077(self):
        """test 1077 ver. 1.2.2"""
        input = """
func foo()
    begin
        number "abcdef"
        number s
        r <- 2.0
        number a[5]
        number b[5]
        s <- r * r * 3.14
        a[0] <- s
    end
        """
        expect = "Error on line 4 col 15: abcdef"
        self.assertTrue(TestParser.test(input,expect,1077))
    
    def test_1078(self):
        """test 1078 ver. 1.2.2"""
        input = """
func foo()
    begin
        number __"abc"
        number s
        r <- 2.0
        number a[5]
        number b[5]
        s <- r * r * 3.14
        a[0] <- s
    end
        """
        expect = "Error on line 4 col 17: abc"
        self.assertTrue(TestParser.test(input,expect,1078))
    
    def test_1079(self):
        """test 1079 ver. 1.2.2"""
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,1079))
    
    def test_1080(self):
        """test 1080 ver. 1.2.2"""
        input = """
func foo()
    begin
        number _##"abc"^^^\n
        number \nstring
        r <- 2.0
        number a[5]
        number b[5]
        s <- r * r * 3.14
        a[0] <- s
    end
        """
        expect = "Error on line 6 col 15: \n"
        self.assertTrue(TestParser.test(input,expect,1080))
    
    def test_1081(self):
        """test 1081"""
        input = """
dynamic r <- a - b * a/b
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,1081))
    
    def test_1082(self):
        """test 1082"""
        input = """
dynamic r <- (a - (b * a/b))
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,1082))
    
    def test_1083(self):
        """test 1083"""
        input = """
dynamic r <- ((a - b) * (a/b))...(a%b) + (a - (b + c) * 3)
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,1083))
    
    def test_1084(self):
        """test 1084"""
        input = """
dynamic r <- not((a - b) * (a/b))...(a%b) == (a or (b + c) and 3)
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,1084))
    
    def test_1085(self):
        """test 1085"""
        input = """
dynamic r <- not((a - b) * (a/b))...(a%b) == (a ... (b <= c) and 3 and a[(a+(b/c)),foo([a,b,c])])
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,1085))
    
    def test_1086(self):
        """test 1086"""
        input = """
dynamic r <- not(((-a - -b) * (a/b)) = (-a%b) == (a ... (b <= c) and 3 >= a[(a != (b/c)),foo([a,b,c])])) < (a > [b,c()[d[e]]])
        """
        expect = "Error on line 2 col 46: =="
        self.assertTrue(TestParser.test(input,expect,1086))
    
    def test_1087(self):
        """test 1087"""
        input = """
dynamic r <- not(((-a - -b) * (a/b)) = ((-a%b) == (a ... (b <= c) and 3 >= a[(a != (b/c)),foo([a,b,c])])) < (a > [b,c()[d[e]]]))
        """
        expect = "Error on line 2 col 106: <"
        self.assertTrue(TestParser.test(input,expect,1087))
    
    def test_1088(self):
        """test 1088"""
        input = """
dynamic r <- not(((-a - -b) * (a/b)) = (((-a%b) == (a ... (b <= c) and 3 >= a[(a != (b/c)),foo([a,b,c])]))) < (a > [b,c()[d[e]]]))
        """
        expect = "Error on line 2 col 108: <"
        self.assertTrue(TestParser.test(input,expect,1088))
    
    def test_1089(self):
        """test 1089"""
        input = """
dynamic r <- not(((-a - -b) * (a/b)) = ((((-a%b) == (a ... (b <= c) and 3 >= a[(a != (b/c)),foo([a,b,c])]))) < (a > [b,c()[d[e]...(a >= b)...-c]])))
        """
        expect = "Error on line 2 col 138: ..."
        self.assertTrue(TestParser.test(input,expect,1089))
    
    def test_1090(self):
        """test 1090"""
        input = """
dynamic r <- not(((-a - -b) * (a/b)) = ((((-a%b) == (a ... (b <= c) and 3 >= a[(a != (b/c)),foo([a,b,c])]))) < (a > [b,c()[d[e]...((a >= b)...-c)]])))
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,1090))
    
    def test_1091(self):
        """test 1091 ver. 1.0.0"""
        input = """
func areDivisors(number num1, number num2)
    return (num1 % num2 = 0 or num2 % num1 = 0)

func main()
    begin
        var num1 <- readNumber()
        var num2 <- readNumber()
        if areDivisors(num1, num2) printString("Yes")
        else printString("No")
    end
        """
        expect = "Error on line 3 col 43: ="
        self.assertTrue(TestParser.test(input,expect,1091))
    
    def test_1092(self):
        """test 1092 ver. 1.0.0"""
        input = """
func isPrime(number x)

func main()
    begin
        number x <- readNumber()
        if isPrime(x) printString("Yes")
        else printString("No")
    end

func isPrime(number x)
    begin
        if x <= 1 return false
        var i <- 2
        for i until i > x / 2 by 1
        begin
            if x % i = 0 return false
        end
        return true
    end
        """
        expect = "Error on line 7 col 11: isPrime"
        self.assertTrue(TestParser.test(input,expect,1092))
    
    def test_1093(self):
        """test 1093"""
        input = """func main()\nbegin\nend\n"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,1093))
    
    def test_1094(self):
        """test 1094"""
        input = """
func goo (number a, b)
    return 1 - foo(1, a, b)
"""
        expect = "Error on line 2 col 20: b"
        self.assertTrue(TestParser.test(input,expect,1094))
    
    def test_1095(self):
        """test 1095"""
        input = """
func goo (number a, number b)
    return 1 - foo(1, a, b)
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,1095))
    
    def test_1096(self):
        """test 1096 ver. 1.0.0"""
        input = """
func foo()
    begin
        aPI <- 3.14
        value <- x.foo(5)
        l[3] <- value * aPi
    end
        """
        expect = "."
        self.assertTrue(TestParser.test(input,expect,1096))
    
    def test_1097(self):
        """test 1097"""
        input = """
func goo (number a, number b)
    return"""
        expect = "Error on line 3 col 10: <EOF>"
        self.assertTrue(TestParser.test(input,expect,1097))
    
    def test_1098(self):
        """test 1098"""
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,1098))
    
    def test_1099(self):
        """test 1099"""
        input = """
func Second_to_Last(string str)
    return str(04-02-2024)
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,1099))
    
    def test_1100(self):
        """test 1100"""
        input = """
func Last(string str)
    begin
        str <- "HAPPY NEW YEAR!"    ## happy new year 2024
    end
## FIN"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,1100))