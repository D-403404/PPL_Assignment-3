import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    def test_1(self):
        """test 1"""
        input = "the_quick_brown_fox\b\f\n\n\n#"
        expect = "the_quick_brown_fox,\n,\n,\n,Error Token #"
        self.assertTrue(TestLexer.test(input,expect,1))

    def test_2(self):
        """test 2"""
        input = "the_quick_brown_fox\b\fJumPS___ovEr\a\n_THE_laz__y_doG\n\n\t123"
        expect = "the_quick_brown_fox,JumPS___ovEr,Error Token \a"
        self.assertTrue(TestLexer.test(input,expect,2))

    def test_3(self):
        """test 3"""
        input = """\r\n\\N"""
        expect = """
,
,Error Token \\"""
        self.assertTrue(TestLexer.test(input,expect,3))

    def test_4(self):
        """test 4"""
        input = """\r\n\\r\\n_ABCXYZ123 __aAaAA_-Aaa?__"""
        expect = """
,
,\\r,\\n,_ABCXYZ123,__aAaAA_,-,Aaa,Error Token ?"""
        self.assertTrue(TestLexer.test(input,expect,4))

    def test_5(self):
        """test 5"""
        input = """
hello _world    , i'm sick
\n\a

"""
        expect = """
,hello,_world,,,i,Error Token '"""
        self.assertTrue(TestLexer.test(input,expect,5))

    def test_6(self):
        """test 6"""
        input = """
hello _world  ##what jgfghhjghhhg  , i'm sick
\n\a

"""
        expect = """
,hello,_world,
,
,Error Token \a"""
        self.assertTrue(TestLexer.test(input,expect,6))

    def test_7(self):
        """test 7"""
        input = """
##mumumumumu
##nananananana
##lololololololo
##
89ue.2"""
        expect = """
,
,
,
,
,89,ue,Error Token ."""
        self.assertTrue(TestLexer.test(input,expect,7))

    def test_8(self):
        """test 8"""
        input = """abcxyz 123_xnh@"""
        expect = """abcxyz,123,_xnh,Error Token @"""
        self.assertTrue(TestLexer.test(input,expect,8))

    def test_9(self):
        """test 9"""
        input = """0ab_12"\n;\\x"""
        expect = """Error Token 0"""
        expect = """0,ab_12,Unclosed String: """
        self.assertTrue(TestLexer.test(input,expect,9))
    
    def test_10(self):
        """test 10"""
        input = """0X12 abc%/-_xyz mn$op"""
        expect = """0,X12,abc,%,/,-,_xyz,mn,Error Token $"""
        self.assertTrue(TestLexer.test(input,expect,10))

    def test_11(self):
        """test 11"""
        input = "002.0000600r2\\n\\t\\?"
        expect = "002.0000600,r2,\\n,Error Token \\"
        self.assertTrue(TestLexer.test(input,expect,11))
    
    def test_12(self):
        """test 12"""
        input = "23.1231eE23e1^2"
        expect = "23.1231,eE23e1,Error Token ^"
        self.assertTrue(TestLexer.test(input,expect,12))
    
    def test_13(self):
        """test 13"""
        input = "23.e13 45.1223E-1 672.12Ee-3 2^3"
        expect = "23.e13,45.1223E-1,672.12,Ee,-,3,2,Error Token ^"
        self.assertTrue(TestLexer.test(input,expect,13))
    
    def test_14(self):
        """test 14"""
        input = "23.e13 45.1223E-1 672.12Ee-3 2*3 e2 a? 12"
        expect = "23.e13,45.1223E-1,672.12,Ee,-,3,2,*,3,e2,a,Error Token ?"
        self.assertTrue(TestLexer.test(input,expect,14))
    
    def test_15(self):
        """test 15"""
        input = "0 1 23 00 000 -0 -2 0e2 0.2 0.2e+ 23.e\n13 45\n.1223E-1"
        expect = "0,1,23,00,000,-,0,-,2,0e2,0.2,0.2,e,+,23.,e,\n,13,45,\n,Error Token ."
        self.assertTrue(TestLexer.test(input,expect,15))
    
    def test_16(self):
        """test 16"""
        input = "-312.e11 21E+41 5E--2 23..t3"
        expect = "-,312.e11,21E+41,5,E,-,-,2,23.,Error Token ."
        self.assertTrue(TestLexer.test(input,expect,16))
    
    def test_17(self):
        """test 17"""
        input = "-312.e11 21E+41 5E--2 23..t3"
        expect = "-,312.e11,21E+41,5,E,-,-,2,23.,Error Token ."
        self.assertTrue(TestLexer.test(input,expect,17))
    
    def test_18(self):
        """test 18"""
        input = "12. 0.311e-2 31 ...47e-0'0.01'"
        expect = "12.,0.311e-2,31,...,47e-0,Error Token '"
        self.assertTrue(TestLexer.test(input,expect,18))
    
    def test_19(self):
        """test 19"""
        input = "+12. 3eeee2 0.311e-2 31\r 47e+2e2.2 "
        expect = "+,12.,3,eeee2,0.311e-2,31,\n,47e+2,e2,Error Token ."
        self.assertTrue(TestLexer.test(input,expect,19))
    
    def test_20(self):
        """test 20"""
        input = "+12.  3e5eee 4e_ 2.... 5..."
        expect = "+,12.,3e5,eee,4,e_,2.,...,5.,Error Token ."
        self.assertTrue(TestLexer.test(input,expect,20))
    
    def test_21(self):
        """test 21"""
        input = "......\r.....\r\n"
        expect = "...,...,\n,...,Error Token ."
        self.assertTrue(TestLexer.test(input,expect,21))
    
    def test_22(self):
        """test 22"""
        input = """true false number bool string
return var dynamic func
for until by break continue
if else elif begin end
not and or math !"""
        expect = """true,false,number,bool,string,
,return,var,dynamic,func,
,for,until,by,break,continue,
,if,else,elif,begin,end,
,not,and,or,math,Error Token !"""
        self.assertTrue(TestLexer.test(input,expect,22))
    
    def test_23(self):
        """test 23"""
        input = """true false number bool string
return var dynamic func
for until by break continue
if else elif begin end
not and or math !""".upper()
        expect = """TRUE,FALSE,NUMBER,BOOL,STRING,
,RETURN,VAR,DYNAMIC,FUNC,
,FOR,UNTIL,BY,BREAK,CONTINUE,
,IF,ELSE,ELIF,BEGIN,END,
,NOT,AND,OR,MATH,Error Token !"""
        self.assertTrue(TestLexer.test(input,expect,23))
    
    def test_24(self):
        """test 24"""
        input = """true false number bool string
return var dynamic func
for until by break continue
if else elif begin end
not and or math !""".upper()
        expect = """TRUE,FALSE,NUMBER,BOOL,STRING,
,RETURN,VAR,DYNAMIC,FUNC,
,FOR,UNTIL,BY,BREAK,CONTINUE,
,IF,ELSE,ELIF,BEGIN,END,
,NOT,AND,OR,MATH,Error Token !"""
        self.assertTrue(TestLexer.test(input,expect,24))
    
    def test_25(self):
        """test 25"""
        input = """true false number bool string
return var dynamic func
for until by break continue
if else elif begin end
not and or math :::""".upper()
        expect = """TRUE,FALSE,NUMBER,BOOL,STRING,
,RETURN,VAR,DYNAMIC,FUNC,
,FOR,UNTIL,BY,BREAK,CONTINUE,
,IF,ELSE,ELIF,BEGIN,END,
,NOT,AND,OR,MATH,Error Token :"""
        self.assertTrue(TestLexer.test(input,expect,25))
    
    def test_26(self):
        """test 26"""
        input = """+ - * / %
not and or = <-
!= < <= > >=
... == AND oR NoT &&"""
        expect = """+,-,*,/,%,
,not,and,or,=,<-,
,!=,<,<=,>,>=,
,...,==,AND,oR,NoT,Error Token &"""
        self.assertTrue(TestLexer.test(input,expect,26))
    
    def test_27(self):
        """test 27"""
        input = """+ - * / %
not and or = <-
!= < <= > >=
... == AND oR NoT ||"""
        expect = """+,-,*,/,%,
,not,and,or,=,<-,
,!=,<,<=,>,>=,
,...,==,AND,oR,NoT,Error Token |"""
        self.assertTrue(TestLexer.test(input,expect,27))
    
    def test_28(self):
        """test 28"""
        input = """ \\ """
        expect = """Error Token \\"""
        self.assertTrue(TestLexer.test(input,expect,28))
    
    def test_29(self):
        """test 29"""
        input = """ () [] {} """
        expect = """(,),[,],Error Token {"""
        self.assertTrue(TestLexer.test(input,expect,29))
    
    def test_30(self):
        """test 30"""
        input = """ () [] ##{}#{}\n#{} """
        expect = """(,),[,],\n,Error Token #"""
        self.assertTrue(TestLexer.test(input,expect,30))

    def test_31(self):
        """test 31 simple string"""
        self.assertTrue(TestLexer.test("\"'Yanxi Palace - 2018'\"","Unclosed String: 'Yanxi Palace - 2018'\"",31))

    def test_32(self):
        """test 32 complex string"""
        self.assertTrue(TestLexer.test("\"'isn''t'\"","Unclosed String: 'isn''t'\"",32))

    def test_33(self):
        """test 33"""
        input = """ "He asked me: \\'"Where is John?\\'"" """
        expect = "He asked me: \\',Where,is,John,Error Token ?"
        self.assertTrue(TestLexer.test(input,expect,33))
    
    def test_34(self):
        """test 34"""
        input = """ "ab\'"c\\n def" """
        expect = """Unclosed String: ab'"c"""
        self.assertTrue(TestLexer.test(input,expect,34))
    
    def test_35(self):
        """test 35"""
        input = """ "jsjfajsfkhjakjkakfwe90o9i288r_==+:;sd;'"S:kdlau\\###$%^\t ebv " """
        expect = """Illegal Escape In String: jsjfajsfkhjakjkakfwe90o9i288r_==+:;sd;'"S:kdlau\\#"""
        self.assertTrue(TestLexer.test(input,expect,35))
    
    def test_36(self):
        """test 36"""
        input = """ "Escape sequence in string: \n \b \f \n" """
        expect = """Unclosed String: Escape sequence in string: """
        self.assertTrue(TestLexer.test(input,expect,36))
    
    def test_37(self):
        """test 37"""
        input = """ "This is a string containing tab \t\r\n" """
        expect = """Unclosed String: This is a string containing tab \t"""
        self.assertTrue(TestLexer.test(input,expect,37))
    
    def test_38(self):
        """test 38"""
        input = """ "This is a string containing tab \\t\\r\\n" """
        expect = """Unclosed String: This is a string containing tab \\t\\r"""
        self.assertTrue(TestLexer.test(input,expect,38))
    
    def test_39(self):
        """test 39"""
        input = """ "Backslash in string \\x" """
        expect = """Illegal Escape In String: Backslash in string \\x"""
        self.assertTrue(TestLexer.test(input,expect,39))
    
    def test_40(self):
        """test 40"""
        input = """ "Backslash in string \\\\x" """
        expect = """Backslash in string \\\\x,<EOF>"""
        self.assertTrue(TestLexer.test(input,expect,40))

    def test_41(self):
        """test 41"""
        input = """ "It's \\t meeee! 1.0e-12 .5" " """
        expect = "It's \\t meeee! 1.0e-12 .5,Unclosed String:  "
        self.assertTrue(TestLexer.test(input,expect,41))

    def test_42(self):
        """test 42"""
        input = """ "It's \\n meeee!" """
        expect = "Unclosed String: It's "
        self.assertTrue(TestLexer.test(input,expect,42))

    def test_43(self):
        """test 43"""
        input = """ "\b\f\t\b\f\ra\n" """
        expect = "Unclosed String: \b\f\t\b\f"
        self.assertTrue(TestLexer.test(input,expect,43))

    def test_44(self):
        """test 44"""
        input = """ "It's \t\\z\b meeee!" """
        expect = "Illegal Escape In String: It's \t\\z"
        self.assertTrue(TestLexer.test(input,expect,44))

    def test_45(self):
        """test 45"""
        input = """ "It's 'meeee!'" """
        expect = "Unclosed String: It's 'meeee!'\" "
        self.assertTrue(TestLexer.test(input,expect,45))

    def test_46(self):
        """test 46"""
        input = """ "It's \n meeee!" """
        expect = "Unclosed String: It's "
        self.assertTrue(TestLexer.test(input,expect,46))

    def test_47(self):
        """test 47"""
        input = """ "'" "\'" "\\'" """
        expect = "'\" ,Error Token '"
        self.assertTrue(TestLexer.test(input,expect,47))

    def test_48(self):
        """test 48"""
        input = """ "\\'" "\'" """
        expect = "\\',Unclosed String: '\" "
        self.assertTrue(TestLexer.test(input,expect,48))

    def test_49(self):
        """test 49"""
        input = """ "HELLLLLLLLLLO \\ " """
        expect = "Illegal Escape In String: HELLLLLLLLLLO \\ "
        self.assertTrue(TestLexer.test(input,expect,49))

    def test_50(self):
        """test 50"""
        input = """ "\a" """
        expect = "\a,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,50))

    def test_51(self):
        """test 51"""
        input = """ "xyz\\'"fu" """
        expect = """xyz\\',fu,Unclosed String:  """
        self.assertTrue(TestLexer.test(input,expect,51))

    def test_52(self):
        """test 52"""
        input = """ "\\'"\\b\n" """
        expect = """\\',\n,Unclosed String:  """
        self.assertTrue(TestLexer.test(input,expect,52))
    
    def test_53(self):
        """test 53"""
        input = """ "\\'"\\b\\n"\'" """
        expect = """\\',\\n,Unclosed String: '" """
        self.assertTrue(TestLexer.test(input,expect,53))
    
    def test_54(self):
        """test 54"""
        input = """ \\'"\\b\\n"\' """
        expect = """Error Token \\"""
        self.assertTrue(TestLexer.test(input,expect,54))

    def test_55(self):
        """test 55"""
        input = """ string "... '' ........... \\'", """
        expect = "string,... '' ........... \\',,,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,55))

    def test_56(self):
        """test 56"""
        input = """ string "... '' ........... '", """
        expect = "string,Unclosed String: ... '' ........... '\", "
        self.assertTrue(TestLexer.test(input,expect,56))

    def test_57(self):
        """test 57"""
        input = """ ##This is a comment \n\\ """
        expect = "\n,Error Token \\"
        self.assertTrue(TestLexer.test(input,expect,57))

    def test_58(self):
        """test 58"""
        input = """ string 1.3 \r\f\t\b\n\a """
        expect = "string,1.3,\n,\n,Error Token \a"
        self.assertTrue(TestLexer.test(input,expect,58))

    def test_59(self):
        """test 59"""
        input = """0ab_12'"\n;x"""
        expect = """0,ab_12,Error Token '"""
        self.assertTrue(TestLexer.test(input,expect,59))

    def test_60(self):
        """test 60"""
        input = """0ab_12""\n\\r"\\x\""""
        expect = """0,ab_12,,
,\\r,Illegal Escape In String: \\x"""
        self.assertTrue(TestLexer.test(input,expect,60))

    def test_61(self):
        """test 61"""
        input = """0ab_12"\\n;x"""
        expect = """0,ab_12,Unclosed String: """
        self.assertTrue(TestLexer.test(input,expect,61))

    def test_62(self):
        """test 62"""
        input = """0ab_12"\n;x"""
        expect = """0,ab_12,Unclosed String: """
        self.assertTrue(TestLexer.test(input,expect,62))
    
    def test_63(self):
        """test 63"""
        input = """0ab_12";x"""
        expect = """0,ab_12,Unclosed String: ;x"""
        self.assertTrue(TestLexer.test(input,expect,63))
    
    def test_64(self):
        """test 64"""
        input = """ a\r\n##1\nb\r"\r\n" """
        expect = """a,
,
,
,b,
,Unclosed String: """
        self.assertTrue(TestLexer.test(input,expect,64))

    def test_65(self):
        """test 65"""
        input = """ \t\b\f\r\n\a """
        expect = """\n,\n,Error Token \a"""
        self.assertTrue(TestLexer.test(input,expect,65))

    def test_66(self):
        """test 66"""
        input = """ \t\b\f
\a """
        expect = """\n,Error Token \a"""
        self.assertTrue(TestLexer.test(input,expect,66))

    def test_67(self):
        """test 67"""
        input = """\r\n\\r\\n_ABCXYZ123 __/\50\46\109 \123"""
        expect = """
,
,\\r,\\n,_ABCXYZ123,__,/,(,Error Token &"""
        self.assertTrue(TestLexer.test(input,expect,67))
    
    def test_68(self):
        """test 68"""
        input = """\r\n\\r\\n_ABCXYZ123 __/\50\50\129 \\123"""
        expect = """
,
,\\r,\\n,_ABCXYZ123,__,/,(,(,
,9,Error Token \\"""
        self.assertTrue(TestLexer.test(input,expect,68))
    
    def test_69(self):
        """test 69"""
        input = """\r\n\\r\\n_ABCXYZ123 __/\63\56\114 \\123"""
        expect = """
,
,\\r,\\n,_ABCXYZ123,__,/,3.,L,Error Token \\"""
        self.assertTrue(TestLexer.test(input,expect,69))
    
    def test_70(self):
        """test 70"""
        input = """a quick brown fox jumps over a lazy dog, 
        (actually this is just a random sentence\\b\\f\\n\\r [1n_order _t0 tEsT "s0me_Lexer RULE$$$__$$$"])
        "go away!"##the dog \\n\\r says (this is a comment like above ^^^^)\r\abc """
        expect = """a,quick,brown,fox,jumps,over,a,lazy,dog,,,
,(,actually,this,is,just,a,random,sentence,\\n,\\r,[,1,n_order,_t0,tEsT,s0me_Lexer RULE$$$__$$$,],),
,go away!,\n,Error Token \a"""
        self.assertTrue(TestLexer.test(input,expect,70))
    
    def test_71(self):
        """test 71"""
        input = """"^"a%^"""
        expect = """^,a,%,Error Token ^"""
        self.assertTrue(TestLexer.test(input,expect,71))
    
    def test_72(self):
        """test 72"""
        input = """15.Efdss__1abc*<>><=="*-+++$##><>"{// " \\ """
        expect = """15.,Efdss__1abc,*,<,>,>,<=,=,*-+++$##><>,Error Token {"""
        self.assertTrue(TestLexer.test(input,expect,72))
    
    def test_73(self):
        """test 73"""
        input = """ "test1" \ninput\\m##\\h\\m "test2" """
        expect = """test1,\n,input,Error Token \\"""
        self.assertTrue(TestLexer.test(input,expect,73))
    
    def test_74(self):
        """test 74"""
        input = """ 
##This is comment
abc
//This isn"t comment 
abc"""
        expect = """
,
,abc,
,/,/,This,isn,Unclosed String: t comment """
        self.assertTrue(TestLexer.test(input,expect,74))
    
    def test_75(self):
        """test 75"""
        input = """ ##3e1.kwi12.0"test\\u" #\\r$ \r#"""
        expect = """\n,Error Token #"""
        self.assertTrue(TestLexer.test(input,expect,75))
    
    def test_76(self):
        """test 76"""
        input = """====== === -> skip;"""
        expect = """==,==,==,==,=,-,>,skip,Error Token ;"""
        self.assertTrue(TestLexer.test(input,expect,76))
    
    def test_77(self):
        """test 77"""
        input = """int a[6] = [1,2,3];"""
        expect = """int,a,[,6,],=,[,1,,,2,,,3,],Error Token ;"""
        self.assertTrue(TestLexer.test(input,expect,77))
    
    def test_78(self):
        """test 78"""
        input = """func foo() {begin \nvar a <- 5 \nend}"""
        expect = """func,foo,(,),Error Token {"""
        self.assertTrue(TestLexer.test(input,expect,78))
    
    def test_79(self):
        """test 79"""
        input = """func foo() begin \nvar a <- 5 \nend\v"""
        expect = """func,foo,(,),begin,\n,var,a,<-,5,\n,end,Error Token \v"""
        self.assertTrue(TestLexer.test(input,expect,79))
    
    def test_80(self):
        """test 80"""
        input = """ if (x <= 1) return "falsestmt\\n" """
        expect = """if,(,x,<=,1,),return,Unclosed String: falsestmt"""
        self.assertTrue(TestLexer.test(input,expect,80))
    
    def test_81(self):
        """test 81"""
        input = """ if (x <= 1) return ["false##stmt",[3,4]]["s] """
        expect = """if,(,x,<=,1,),return,[,false##stmt,,,[,3,,,4,],],[,Unclosed String: s] """
        self.assertTrue(TestLexer.test(input,expect,81))
    
    def test_82(self):
        """test 82"""
        input = """((num1 % num2 = 0) or (num2 % num1 = 0) and !true)"""
        expect = """(,(,num1,%,num2,=,0,),or,(,num2,%,num1,=,0,),and,Error Token !"""
        self.assertTrue(TestLexer.test(input,expect,82))
    
    def test_83(self):
        """test 83"""
        input = """func main() return ((a+b)**2) > foo(abc,xyz)[3,1]\a"""
        expect = """func,main,(,),return,(,(,a,+,b,),*,*,2,),>,foo,(,abc,,,xyz,),[,3,,,1,],Error Token \a"""
        self.assertTrue(TestLexer.test(input,expect,83))
    
    def test_84(self):
        """test 84"""
        input = """for(int i=0, i != 4, i++) print("hello World);"""
        expect = """for,(,int,i,=,0,,,i,!=,4,,,i,+,+,),print,(,Unclosed String: hello World);"""
        self.assertTrue(TestLexer.test(input,expect,84))
    
    def test_85(self):
        """test 85"""
        input = """fetch(data)
        if(not data) cout << '404 NOT FOUND' """
        expect = """fetch,(,data,),
,if,(,not,data,),cout,<,<,Error Token '"""
        self.assertTrue(TestLexer.test(input,expect,85))
    
    def test_86(self):
        """test 86"""
        input = """lexerr::header"""
        expect = """lexerr,Error Token :"""
        self.assertTrue(TestLexer.test(input,expect,86))
    
    def test_87(self):
        """test 87"""
        input = """unnamed-horse@gmail.com"""
        expect = """unnamed,-,horse,Error Token @"""
        self.assertTrue(TestLexer.test(input,expect,87))
    
    def test_88(self):
        """test 88"""
        input = """ERROR_CHAR: . {raise ErrorToken(self.text)};"""
        expect = """ERROR_CHAR,Error Token :"""
        self.assertTrue(TestLexer.test(input,expect,88))
    
    def test_89(self):
        """test 89"""
        input = """ERROR_CHAR##: . {raise \nErrorToken(self.text)};"""
        expect = """ERROR_CHAR,\n,ErrorToken,(,self,Error Token ."""
        self.assertTrue(TestLexer.test(input,expect,89))
    
    def test_90(self):
        """test 90"""
        input = """<EOF>\v"""
        expect = """<,EOF,>,Error Token \v"""
        self.assertTrue(TestLexer.test(input,expect,90))
    
    def test_91(self):
        """test 91"""
        input = """177031.69E+215.14E16"""
        expect = """177031.69E+215,Error Token ."""
        self.assertTrue(TestLexer.test(input,expect,91))
    
    def test_92(self):
        """test 92"""
        input = """t1ck_t0ck <- < - <-- a([/\\])"""
        expect = """t1ck_t0ck,<-,<,-,<-,-,a,(,[,/,Error Token \\"""
        self.assertTrue(TestLexer.test(input,expect,92))
    
    def test_93(self):
        """test 93"""
        input = """if(a==b and not 6) do stmt_1 elif(a) do stmt_2 else $"""
        expect = """if,(,a,==,b,and,not,6,),do,stmt_1,elif,(,a,),do,stmt_2,else,Error Token $"""
        self.assertTrue(TestLexer.test(input,expect,93))
    
    def test_94(self):
        """test 94"""
        input = """if(a==b and not 6)\r\n do stmt_1 elif(a)\r\n do stmt_2 else $"""
        expect = """if,(,a,==,b,and,not,6,),\n,\n,do,stmt_1,elif,(,a,),\n,\n,do,stmt_2,else,Error Token $"""
        self.assertTrue(TestLexer.test(input,expect,94))
    
    def test_95(self):
        """test 95"""
        input = """if(a==b and not 6)\r do stmt_1 elif(a)\n do stmt_2 else $"""
        expect = """if,(,a,==,b,and,not,6,),\n,do,stmt_1,elif,(,a,),\n,do,stmt_2,else,Error Token $"""
        self.assertTrue(TestLexer.test(input,expect,95))
    
    def test_96(self):
        """test 96"""
        input = """u_have_been HIT_by, u_ve been struck_BY, AAAAA sm0000th, cr1m1nal!!!"""
        expect = """u_have_been,HIT_by,,,u_ve,been,struck_BY,,,AAAAA,sm0000th,,,cr1m1nal,Error Token !"""
        self.assertTrue(TestLexer.test(input,expect,96))
    
    def test_97(self):
        """test 97"""
        input = """if(MIchael) say('HEE HEE')"""
        expect = """if,(,MIchael,),say,(,Error Token '"""
        self.assertTrue(TestLexer.test(input,expect,97))
    
    def test_98(self):
        """test 98"""
        input = """
begin
    do nothing
end\r\n
\\"""
        expect = """\n,begin,\n,do,nothing,\n,end,\n,\n,\n,Error Token \\"""
        self.assertTrue(TestLexer.test(input,expect,98))
    
    def test_99(self):
        """test 99"""
        input = """s <- r * r * 3\r.14"""
        expect = """s,<-,r,*,r,*,3,\n,Error Token ."""
        self.assertTrue(TestLexer.test(input,expect,99))
    
    def test_100(self):
        """test 100"""
        input = """ENDING for the LEXERRRR test, just wanna make sure no error in this testcase :)"""
        expect = """ENDING,for,the,LEXERRRR,test,,,just,wanna,make,sure,no,error,in,this,testcase,Error Token :"""
        self.assertTrue(TestLexer.test(input,expect,100))
    