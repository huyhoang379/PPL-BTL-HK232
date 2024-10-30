import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    def testcase_00(self): # test case 200 -> 209
        """test"""
        input =""" var a[2]
        """
        expect = "Error on line 1 col 6: ["
        self.assertTrue(TestParser.test(input,expect,200))
    def testcase_01(self):
        """test"""
        input =""" number a[1,2,3]<-[]  
                    dynamic a[2,3] <- [[1,2]]
                    """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))
    def testcase_02(self):
        """test"""
        input =""" bool a[0] <- [[2,3],[4,5],1+2]  
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,202))
    def testcase_03(self):
        """test"""
        input =""" string a[0,0,0] <-  [2,3+1,"string"]
                    number a[1,2] <- []
        number a[1+2,3,a>3] <- [1,2,3]
        """
        expect = """Error on line 3 col 18: +"""
        self.assertTrue(TestParser.test(input,expect,203))
    def testcase_04(self):
        """test"""
        input =""" number diem[1111] <- [1,2,3
        """
        expect = """Error on line 1 col 28: \n\n"""
        self.assertTrue(TestParser.test(input,expect,204))
    def testcase_05(self):
        """test"""
        input =""" bool hello <- [123] 
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,205))
    def testcase_06(self):
        """test"""
        input =""" number a[0] <- [[1,2,3],[4,5,6],"string"] 
                    bool a[1,2,3] <- a+2
                    string a[2][3]
                    """
        expect = "Error on line 3 col 31: ["
        self.assertTrue(TestParser.test(input,expect,206))
    def testcase_07(self):
        """test"""
        input ="""func main() 
                    begin 
                        a[3 + foo(2)] <- a[b[2, 3]] + 4
                    end
                bool a[3 + foo(2)] <- a[b[2, 3]] + 4
                """
        expect = "Error on line 5 col 25: +"
        self.assertTrue(TestParser.test(input,expect,207))
    def testcase_08(self):
        """test"""
        input =""" bool a[1,2,3] <- [[true, false, true],["true","false",true]]
         """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,208))
    def testcase_09(self):
        """test"""
        input =""" string diem[2,4] <- [[10,10,10,1],2,[2,3],4,[5,6]]
                    number nullptr[3] <- [[[1,2,3],true,[2,3]],[2,3],3]
                    """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,209))
    def testcase_10(self):
        """test normal expression"""
        input =""" func main()
                    begin
                        a[1] <- 1+3-4%6 and a > "Lunar new year" or -a < 3
                    end
                    
        """
        expect = "Error on line 3 col 71: <"
        self.assertTrue(TestParser.test(input,expect,210))
    def testcase_11(self):
        """test index_op"""
        input =""" func main()
                    begin
                        a <- main()[1+2,3] / a[2,3,4,5,6,7] + func_call(func_call[1,2])[1,2]
                    end
                    """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,211))
    def testcase_12(self):
        """test"""
        input ="""func main()
                    begin
                        a <- not - main()[1+2,3]  + - not a[3]
                    end   
        """
        expect = "Error on line 3 col 54: not"
        self.assertTrue(TestParser.test(input,expect,212))
    def testcase_13(self):
        """test"""
        input =""" func main()
                    begin
                        a[2,3] <- 2<a ... b > 2
                    end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,213))
    def testcase_14(self):
        """test"""
        input ="""func main()
                    begin
                        a <- function()[2,3] ... "PPL" + 2 > b ... a[1+2,4/2]
                    end
        """
        expect = "Error on line 3 col 63: ..."
        self.assertTrue(TestParser.test(input,expect,214))
    def testcase_15(self):
        """test"""
        input ="""func main()
                    begin
                        a <- function()[2,3] ... a +2 > true - a[1+2,4/2][2]
                    end 
        """
        expect = "Error on line 3 col 73: ["
        self.assertTrue(TestParser.test(input,expect,215))
    def testcase_16(self):
        """test"""
        input =""" func main()
                    begin
                        a <- a > b >= c == d
                    end
                    """
        expect = "Error on line 3 col 35: >="
        self.assertTrue(TestParser.test(input,expect,216))
    def testcase_17(self):
        """test"""
        input =""" func main()
                    begin
                        a <- (function()[2,3] ... true) + 2 > (123 ... a[1+2,4/2])
                    end
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,217))
    def testcase_18(self):
        """test"""
        input ="""func main()
                    begin
                        a <- ( "hello" > 3 ) - (a <= 2) - (true == 3)
                        a[3] <- ( "hello" > 3 ) - (a <= 2 - true == 3)
                    end
         """
        expect = "Error on line 4 col 65: =="
        self.assertTrue(TestParser.test(input,expect,218))
    def testcase_19(self):
        """test"""
        input ="""
                    func main()
                    begin
                        a <- ( "hello" > 3 ) - (a <= 2) - (true == 3)
                        a[3] <- hehe[1,2] + - "happy" + not true 
                        var a <- [1,2,3] + - [a+1,3>2] - [[1-2%3,a > a], [true, false]]
                    end 
                    """
        expect = "Error on line 6 col 41: +"
        self.assertTrue(TestParser.test(input,expect,219))
    def testcase_20(self):
        """test function call + sub problem"""
        input =""" func main()
                    begin
                        isTrue(isTrue())
                        a[1] <- 1+3-4%6 and a > "Lunar new year" or -a < 3
                    end
                    isTrue()
                    
        """
        expect = "Error on line 4 col 71: <"
        self.assertTrue(TestParser.test(input,expect,220))
    def testcase_21(self):
        """test index_op"""
        input =""" func main()
                    begin
                        a[2]<- isOdd(a,true,1)
                    end
                    """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,221))
    def testcase_22(self):
        """test"""
        input ="""func main()
                    begin
                         a[2]<- isOdd(a,true,isEven())
                    end   
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,222))
    def testcase_23(self):
        """test"""
        input =""" 
        func main()
                    begin
                        a[2,3] <- 2<a ... b > 2
                    end
        func isOdd() func hello()
        
        """
        expect = """Error on line 6 col 21: func"""
        self.assertTrue(TestParser.test(input,expect,223))
    def testcase_24(self):
        """test"""
        input ="""func main()
                    begin
                        a <- function()[2,3] ... "PPL" + - function("string", true, 123,a) > not function(a,b,c) ... a[1+2,4/2]
                    end
                    func call_function(number a [1+2,3,a<3])
        """
        expect = "Error on line 3 col 113: ..."
        self.assertTrue(TestParser.test(input,expect,224))
    def testcase_25(self):
        """test"""
        input ="""func main()
                    begin
                        call_function(2,3) <- function()[2,3] ... a +2 > true - a[1+2,4/2][2]
                    end 
                    
        """
        expect = "Error on line 3 col 43: <-"
        self.assertTrue(TestParser.test(input,expect,225))
    def testcase_26(self):
        """test"""
        input =""" func main()
                    begin
                        a <- a > b >= c == d
                    end
                    func abs()
                    return main()
                    func checkTrue()
                    """
        expect = "Error on line 3 col 35: >="
        self.assertTrue(TestParser.test(input,expect,226))
    def testcase_27(self):
        """test"""
        input =""" func abs()
                    func ABS()
                    func dfs(number a,number d) return true
                    func main()
                    begin
                        a <- (function()[2,3] ... true) + 2 > (123 ... a[1+2,4/2])
                        return dfs()
                    end
                    func function (number a bool b)
                """
        expect = "Error on line 9 col 44: bool"
        self.assertTrue(TestParser.test(input,expect,227))
    def testcase_28(self):
        """test"""
        input =""" function( number a , bool b, number a[1,2,3])
                func main()
                    begin
                        a <- ( "hello" > 3 ) - (a <= 2) - (true == 3)
                        a[3] <- ( "hello" > 3 ) - (a <= 2 - true == 3)
                    end
         """
        expect = "Error on line 1 col 1: function"
        self.assertTrue(TestParser.test(input,expect,228))
    def testcase_29(self):
        """test"""
        input ="""
                    func oddOneOut(number a[2], bool d) return "happy birthday"
                    func main()
                    begin
                        a <- odd() + even() % even()[oddOneOut(odd(),even())[odd(),even()]]
                    end 
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,229))
    def testcase_30(self):
        """test declaration + assignment"""
        input =""" func main()
                    begin
                        var a
                    end
                    isTrue()
                    
        """
        expect = """Error on line 3 col 29: \n\n"""
        self.assertTrue(TestParser.test(input,expect,230))
    def testcase_31(self):
        """test index_op"""
        input =""" func main()
                    return dynamic a
                    """
        expect = "Error on line 2 col 27: dynamic"
        self.assertTrue(TestParser.test(input,expect,231))
    def testcase_32(self):
        """test"""
        input ="""func isDivisor()
                    begin
                         dynamic a <- [1,2,3] + [1+2, 3 % 6,a >3]
                         var ID <- []
                    end   
        """
        expect = "Error on line 3 col 46: +"
        self.assertTrue(TestParser.test(input,expect,232))
    def testcase_33(self):
        """test"""
        input =""" 
        func main()
                    begin
                        number a <- function (1,2)
                    end
        func isOdd() return func hello()
        
        """
        expect = """Error on line 6 col 28: func"""
        self.assertTrue(TestParser.test(input,expect,233))
    def testcase_34(self):
        """test"""
        input ="""
                var a <- a
                dynamic a
                bool b
                func main()
                    return var a
        """
        expect = "Error on line 6 col 27: var"
        self.assertTrue(TestParser.test(input,expect,234))
    def testcase_35(self):
        """test"""
        input ="""
                number a <- a() + 1 / 2 * 3 <= 3 ... "true" >= 2
            string b <- a(1,2)[3,4,5 ... 6] + false + false
            bool c <- a(x,y[1,2,"3"] ... 4)[true]
            dynamic d <- (a ... z) ... b and (a >= b) < b[1, b[2]]
            var e <-  ["tr", 2, 3, 4, 5] + [[1, 2 + 2 * 2 / 3, 3], [4, 5, 6]]
            number doanhle <- a(x,array[2])[2,3+2,true,false]
                        
        """
        expect = "Error on line 6 col 41: +"
        self.assertTrue(TestParser.test(input,expect,235))
    def testcase_36(self):
        """test"""
        input =""" func main()
                    begin
                        a <- [1,2,3] - [[3%4,2],2,false]
                    end
                    var a <- number a
                    """
        expect = "Error on line 3 col 37: -"
        self.assertTrue(TestParser.test(input,expect,236))
    def testcase_37(self):
        """test"""
        input =""" var assignment <- a()
            var assignment <- a(1,2)
            dynamic b <- [a,a<3,3]
            var assignment <- a(x,b[2])[2]
            var assignment <- a(x,y[3] ... z)[1,2]
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,237))
    def testcase_38(self):
        """test"""
        input =""" var a <- a[1] + 1
            
            var c <- array[1,(1)...2,array[ar[(1*2) or 1]],array[2]]
            var d <- a[1] + fun()[1,fun()] 
            var b <- array[1,2+3,4+5][0][2,3]
            
         """
        expect = "Error on line 5 col 37: ["
        self.assertTrue(TestParser.test(input,expect,238))
    def testcase_39(self):
        """test"""
        input ="""
                    var HCMUT <- -1 * not 1
                     var BKU <- not not not----K
                    var e <- 1[1]
        """
        expect = "Error on line 4 col 30: ["
        self.assertTrue(TestParser.test(input,expect,239))
    def testcase_40(self):
        input =""" var i <- 0
                    for i until i >= 10 by 1
                    writeNumber(i)
                    
        """
        expect = "Error on line 2 col 20: for"
        self.assertTrue(TestParser.test(input,expect,240))
    def testcase_41(self):
        """test index_op"""
        input =""" begin
                    number r
                    number s
                    r <- 2.0
                    number a[5]
                    number b[5]
                    s <- r * r * 3.14
                    a[0] <- s
                    end
                    """
        expect = "Error on line 1 col 1: begin"
        self.assertTrue(TestParser.test(input,expect,241))
    def testcase_42(self):
        """test"""
        input ="""func areDivisors(number num1, number num2)
 return ((num1 % num2 = 0) or (num2 % num1 = 0))
 func main()
 begin
 var num1 <- readNumber()
 var num2 <- readNumber()
 if (areDivisors(num1, num2)) writeString("Yes")
 else writeString("No")
 end  
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,242))
    def testcase_43(self):
        """test"""
        input =""" 
        func isPrime(number x)
 func main()
 begin
 number x <- readNumber()
 if (isPrime(x)) writeString("Yes")
 else writeString("No")
 end
        
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,243))
    def testcase_44(self):
        """test"""
        input ="""
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
        self.assertTrue(TestParser.test(input,expect,244))
    def testcase_45(self):
        """test"""
        input ="""
                func isPrime()
 begin
 if (x <= 1) return false
 var i <- 2
 for i until (i > x / 2) by 1
 begin
 if (x % i = 0) return false
 end
 return true
 end
                        
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,245))
    def testcase_46(self):
        """test"""
        input =""" func isPrime(number x)
 begin
 if (x <= 1) return false
 var i <- 2
 for arr[0] until i > x / 2 by 1
 begin
 if (x % i = 0) return false
 end
 return true
 end
                    """
        expect = "Error on line 5 col 8: ["
        
        
        
        self.assertTrue(TestParser.test(input,expect,246))
    def testcase_47(self):
        """test"""
        input =""" func isPalindrome() begin
        end
        func main(number a)
        begin
            for i until i > 10 by i % a
                var count <- array[1,2,3][1,2]
                break
                ##comment
        end
        func isPrime(number x)
 begin
 if (x <= 1) return false
 var i <- 2
 for x until (i > x / 2) by 1
 begin
 if (x % i = 0) return false
 end
 return true
 end
                """
        expect = "Error on line 6 col 41: ["
        self.assertTrue(TestParser.test(input,expect,247))
    def testcase_48(self):
        """test"""
        input =""" func foo(number a[5], string b)
 begin
 var i <- 0
 for i until i >= 5 by 1
 begin
 a[i] <- i * i + 5
 end
 return-1
 end
            
         """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,248))
    def testcase_49(self):
        """test"""
        input ="""
                   func main()
        begin
            var i <- foo(2+5)
            begin
                continue
                begin
                    break
                    begin
                        for a until a >= i by 1 + 1
                            if (a > i * i) return true
                            else return false
                    end
                end
            end
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,249))
    def testcase_50(self):
        input =""" func main()
begin
dynamic a <- readNumber()
if ((a>0) and (a<10))
	a<-a*2
else if ((a>10) and (a<20) )
a<-a*3
else a <- a*4
return
end
                    """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,250))
    def testcase_51(self):
        """test index_op"""
        input =""" func main() begin
        
        if (a>3) a <- a-1
        elif (a-1==2) return 0
        elif (a==1) begin
        if(1-2==3) return true
        else return false
        end
        return false
        
                    """
        expect = "Error on line 11 col 20: <EOF>"
        self.assertTrue(TestParser.test(input,expect,251))
    def testcase_52(self):
        """test"""
        input ="""func main()
begin
var a<-3
var b<-4
if (a<b) a<-b+a
if (b<a) 
	if (a=3) b<-b-a
	elif (b=4)
		if (a=7)
			b<-a%b
		else b<-b%a
	else b<-b-a
else
b <- 3

end  
        """
        expect = """Error on line 13 col 4: \n\n"""
        self.assertTrue(TestParser.test(input,expect,252))
    def testcase_53(self):
        """test"""
        input =""" 
        dynamic a
var b<-2
func main()
	begin
if (b=2)
	a <- b
elif (b=3)
	a <- b*2 + 1
else a <- -1
return
end
        
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,253))
    def testcase_54(self):
        """test"""
        input ="""
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
        self.assertTrue(TestParser.test(input,expect,254))
    def testcase_55(self):
        """test"""
        input ="""
                func isPrime()
 begin
 if (x <= 1) return false
 var i <- 2
 for i until (i > x / 2) by 1
 begin
 if (x % i = 0) return false
 end
 return true
 end
 if (a==3) return false
                        
        """
        expect = "Error on line 12 col 1: if"
        self.assertTrue(TestParser.test(input,expect,255))
    def testcase_56(self):
        """test"""
        input =""" func isPrime(number x)
 begin
 if (x <= 1) return false
 var i <- 2
 for arr[0] until i > x / 2 by 1
 begin
 if (x % i = 0) return false
 end
 return true
 end
                    """
        expect = "Error on line 5 col 8: ["
        
        
        
        self.assertTrue(TestParser.test(input,expect,256))
    def testcase_57(self):
        """test"""
        input =""" 
        func main()
        begin
        return
        end
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,257))
    def testcase_58(self):
        """test"""
        input =""" 
            func main()
        begin
        return (false)
        end
         """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,258))
    def testcase_59(self):
        """test"""
        input ="""
                   func main()
        begin
            begin
                begin
                    return "I <3 PPL"
                end
            end
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,259))
    def testcase_60(self):
        input ="""
        var a<- 3.14
            func main()
                    begin
                    a <- [1,2,3]
                    if (a==1) 
                    else a=1
                    end
                    """
        expect = "Error on line 7 col 20: else"
        self.assertTrue(TestParser.test(input,expect,260))
    def testcase_61(self):
        """test index_op"""
        input ="""  var _globalVar <- -1e-9
number pi <- 3.1415926535897
dynamic e <- 2.71828182846
func exp(number n)
begin
var ans <- 1
var i<-0
for i until i=n by 1
ans*=e
return ans
end
func main()
begin
	var a<-exp(10)
end
        
                    """
        expect = "Error on line 9 col 3: *"
        self.assertTrue(TestParser.test(input,expect,261))
    def testcase_62(self):
        """test"""
        input ="""func main()
            func main(number f1)
            func main(number a[5],bool x[5,2,3], bool a[5,2,3], string b, bool c)
            func main(number num1, number num2)
                var MinhDiem <- 1
            func main(number f1 <- c)
        """
        expect = "Error on line 6 col 32: <-"
        self.assertTrue(TestParser.test(input,expect,262))
    def testcase_63(self):
        """test"""
        input =""" 
        func main()
            begin   
                if(1+1) api <- 1
                ## comment0
                
                if(1+1) 
                    ## comment1
                    
                    api <- 1
                    ## comment2
                else api <- 1
                ## comment3
                
                if 1 api <- 1
                elif 1 ... 2
                    ## comment1
                    
                    api <- 1
                    ## comment2
                elif 1 api <- 1
                
                if 1 api <- 1
                elif 1 ... 2 api <- 1
                elif 1 api <- 1
                else api <- 1   
            end
        
        """
        expect = """Error on line 15 col 19: 1"""
        self.assertTrue(TestParser.test(input,expect,263))
    def testcase_64(self):
        """test"""
        input ="""
                func main()
        begin 
            return ([1,2,3]) + 1
            return main()
            main(1,2)
            fun()
            main([1,2,3], 1+2, a, c ... e)
        end
        """
        expect = "Error on line 4 col 20: ["
        self.assertTrue(TestParser.test(input,expect,264))
    def testcase_65(self):
        """test"""
        input ="""
                func main()
            begin
                begin
                    begin
                        x <- 1
                    end
                    
                    begin
                        return true
                    end
                    
                    return false
                end
                
                begin
                end
                return true
            end
            return (HCMUT)
                        
        """
        expect = "Error on line 20 col 12: return"
        self.assertTrue(TestParser.test(input,expect,265))
    def testcase_66(self):
        """test"""
        input =""" func isPrime(number x)
 begin
 if (x <= 1) return false
 var i <- 2
 for arr[0] until i > x / 2 by 1
 begin
 if (x % i = 0) return false
 end
 return true
 end
                    """
        expect = "Error on line 5 col 8: ["
        
        
        
        self.assertTrue(TestParser.test(input,expect,266))
    def testcase_67(self):
        """test"""
        input =""" 
        func main()
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,267))
    def testcase_68(self):
        """test"""
        input =""""""
        expect = "Error on line 1 col 0: <EOF>"
        self.assertTrue(TestParser.test(input,expect,268))
    def testcase_69(self):
        """test"""
        input ="""
        
        """
        expect = "Error on line 3 col 8: <EOF>"
        self.assertTrue(TestParser.test(input,expect,269))
    def testcase_70(self):
        input ="""
        var a<- 3.14
            func main()
                    begin
                    a <- [1,2,3]
                    if (a==1) 
                    else a=1
                    end
                    """
        expect = "Error on line 7 col 20: else"
        self.assertTrue(TestParser.test(input,expect,270))
    def testcase_71(self):
        """test index_op"""
        input ="""  var _globalVar <- -1e-9
number pi <- 3.1415926535897
dynamic e <- 2.71828182846
func exp(number n)
begin
var ans <- 1
var i<-0
for i until i=n by 1
return ans
end
func main()
begin
	var a<-exp(10)
end
        
                    """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,271))
    def testcase_72(self):
        """test"""
        input ="""func main()
            func main(number f1)
            func main(number a[5],bool x[2+1,2,3], bool a[5,2,3], string b, bool c)
            func main(number num1, number num2)
                var MinhDiem <- 1
            func main(number f1 )
            begin
                main(main()[2,3],arr[2+1,3])
            end
        """
        expect = "Error on line 3 col 42: +"
        self.assertTrue(TestParser.test(input,expect,272))
    def testcase_73(self):
        """test"""
        input =""" 
        func main()
begin
var i<-0
var j<-0
var k<-0
number x<-readNumber()
for i until i<x by 5
for j until j<x by a
for k until k<x by 1 
x <- x + 1
end
        
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,273))
    def testcase_74(self):
        """test"""
        input ="""
                func main()
        begin 
            bool a <- not not - - (a[a[a[a[a[a[0]]]]]])
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,274))
    def testcase_75(self):
        """test"""
        input ="""
                ## quin cha na, quin cha na
                        
        """
        expect = "Error on line 4 col 8: <EOF>"
        self.assertTrue(TestParser.test(input,expect,275))
    def testcase_76(self):
        """test"""
        input =""" var a = "abcd"
                func main()
                begin
                    for a[23] until a <2 by 1 return true
                end
                    """
        expect = "Error on line 1 col 7: ="
        
        
        
        self.assertTrue(TestParser.test(input,expect,276))
    def testcase_77(self):
        """test"""
        input =""" 
        var a,b,c <-2
        func main()
                """
        expect = "Error on line 2 col 13: ,"
        self.assertTrue(TestParser.test(input,expect,277))
    def testcase_78(self):
        """test"""
        input ="""func foo(a,b) return true"""
        expect = "Error on line 1 col 9: a"
        self.assertTrue(TestParser.test(input,expect,278))
    def testcase_79(self):
        """test"""
        input ="""
        func main() begin
for _ until _ by _
if (_) break
__()
1
end
        """
        expect = "Error on line 6 col 0: 1"
        self.assertTrue(TestParser.test(input,expect,279))
    def testcase_80(self):
        input ="""
        dynamic a <- [[2+3,foo()[2],2],2,[3,4]]
        func main (number a, number b, bool arr[1,2,[2,3]])
                    """
        expect = "Error on line 3 col 52: ["
        self.assertTrue(TestParser.test(input,expect,280))
    def testcase_81(self):
        """test index_op"""
        input ="""  string a <- "Nguoi co con di qua tung goc pho"
        func main(bool a <- true)
        func isOdd()
                    """
        expect = "Error on line 2 col 25: <-"
        self.assertTrue(TestParser.test(input,expect,281))
    def testcase_82(self):
        """test"""
        input =""" 
        func interface()
        begin
            newline()
            newline()
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,282))
    def testcase_83(self):
        """test"""
        input =""" 
        func main()
begin
var i<-0
var j<-0
var k<-0
number x<-readNumber()
for i until i<x by 5
for j until j<x by a
for k until k<x by 1 var a <- "Dung noi hai chu '" Gia nhu '""
end
        
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,283))
    def testcase_84(self):
        """test"""
        input ="""
                func main()
        begin 
            bool a <- a[not not - - (a[a[a[a[a[a[0]]]]]]), 2+3/4,[1,2,3,4]]
        end
        var b <- a(1,2)[1,2,3 ... 2] + false + true
        """
        expect = "Error on line 4 col 65: ["
        self.assertTrue(TestParser.test(input,expect,284))
    def testcase_85(self):
        """test"""
        input ="""
            func main()
            begin
                for i until i<2 by a%2+5-4 
                    for j until i by a[5] 
                        for k until j by fun()[a] return
            end    
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,285))
    def testcase_86(self):
        """test"""
        input =""" func main(bool haha[2])
            begin
                
                return toYou
                return toMe
                return home
                bool haha[hihi]
            end
                    """
        expect = "Error on line 7 col 26: hihi"
        
        
        
        self.assertTrue(TestParser.test(input,expect,286))
    def testcase_87(self):
        """test"""
        input =""" 
        func a() ##HAPPY NEW YEAR
        begin
            a[_3 + foo(_2)] <- a[_b[_2, _3]] + _4 
        end
        
        
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,287))
    def testcase_88(self):
        """test"""
        input ="""
        begin
            if (c...x <= 1) return false else a<-1
        end
        func abcxyz(number x)
        """
        expect = "Error on line 2 col 8: begin"
        self.assertTrue(TestParser.test(input,expect,288))
    def testcase_89(self):
        """test"""
        input ="""
        func main() begin
for _ until _ by _
if (_) break down
__()
1
end
        """
        expect = "Error on line 4 col 13: down"
        self.assertTrue(TestParser.test(input,expect,289))
    def testcase_90(self):
        input ="""
        func foo()
        begin      
            begin   
                if(1+1) a <- 1
                elif (2+2=4) a <- 2
                
                if(1+1) a <- 1
                else a <- 1
                ## comment
                
                if (1) a <- 1
                elif 1 ... 2
     
                    a <- 1
                elif (1) a <- 1
                
                if (1) a <- 1
                elif (1 ... 2) a <- 1
                elif 1 a <- 1
                else a <- 1   
            end
        end
                    """
        expect = "Error on line 13 col 21: 1"
        self.assertTrue(TestParser.test(input,expect,290))
    def testcase_91(self):
        """test index_op"""
        input ="""  string a <- "despacito"
        bool a <- true
        func main()
        func isOdd()
                    """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,291))
    def testcase_92(self):
        """test"""
        input =""" 
        var cham <- "<3"
        func interface(newline())
        begin
            
            newline()
        end
        """
        expect = "Error on line 3 col 23: newline"
        self.assertTrue(TestParser.test(input,expect,292))
    def testcase_93(self):
        """test"""
        input =""" 
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
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,293))
    def testcase_94(self):
        """test"""
        input ="""
                func main() begin
        number x <- readNumber()
        var y <- 0.
        dynamic z
end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,294))
    def testcase_95(self):
        """test"""
        input ="""
            func main() begin
        bool _b[1] <- [true]
        number a[2,2] <- [[1,2],[3,4]]
        a[1,1] <- a[1,2]
end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,295))
    def testcase_96(self):
        """test"""
        input =""" func main(bool haha[2])
            begin
                bool upToYou= - - - (not (-(not a[1+3%4,a<3,function(a+2)])))
                return toYou
                return toMe
                return home
                bool haha[hihi]
            end
                    """
        expect = "Error on line 3 col 28: ="
        self.assertTrue(TestParser.test(input,expect,296))
    def testcase_97(self):
        """test"""
        input =""" 
        func main()
        begin
            a[_3 + foo(_2)] <- a[_b[_2, _3]] + _4 
        end
        func a() ##HAPPY NEW YEAR
        
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,297))
    def testcase_98(self):
        """test"""
        input ="""
        fun main()
        begin
            break
        end
        continue
        func abcxyz(number x)
        """
        expect = "Error on line 2 col 8: fun"
        self.assertTrue(TestParser.test(input,expect,298))
    def testcase_99(self):
        """test"""
        input ="""
        func main() 
        begin 
            var final
        end
        """
        expect = """Error on line 4 col 21: \n\n"""
        self.assertTrue(TestParser.test(input,expect,299))