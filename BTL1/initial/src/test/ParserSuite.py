import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_00(self):
        input = """func main () return 1
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,200))
        
    def test_01(self):
        input = """func main() begin
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))
        
    def test_02(self):
        input = """func main() 
        begin
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,202))
    
    def test_03(self):
        input = """
            var HuyHoang <- false and "false" or 2 
            var HuyHoang <- 2 and 3 and 4 or 5 or 6
            var HuyHoang <- 2 + 3 - 3 + 4 and 4
            var HuyHoang <- 2 / 3 * 4 % 5
            var HuyHoang <- 2 / 3 / 3 * 4 % 5
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 203)) 

    def test_04(self): 
        input = """ 
            number HuyHoang
            
            ## Huy Hoang
            number HuyHoang <- 1
            bool b[1,1]
            bool b[1,1] <- 12 + 12 / 23 * 34
            string b[34]
            ## 12 
            
            string b[34] <- 23 ... " stress"
            var j <- 1
            dynamic j
            dynamic j <- 1
            ## Huy Hoang
             
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 204))
        
    def test_05(self):    
        input = """ 
            var HuyHoang
        """
        expect = "Error on line 2 col 24: \n"
        self.assertTrue(TestParser.test(input, expect, 205))   
        
    def test_06(self): 
        input = """ 
            dynamic HuyHoang[6] <- 4
        """
        expect = "Error on line 2 col 28: ["
        self.assertTrue(TestParser.test(input, expect, 206))         
        
    def test_07(self): 
        input = """ 
            bool b["stress"]
            bool c[[2,3]]
            bool d[2+2]
        """
        expect = "Error on line 2 col 19: stress"
        self.assertTrue(TestParser.test(input, expect, 207))   
        
    def test_08(self): 
        input = """ 
            bool b[2,]
        """
        expect = "Error on line 2 col 21: ]"
        self.assertTrue(TestParser.test(input, expect, 208)) 
        
    def test_09(self): 
        input = """ 
            var b[2]
        """
        expect = "Error on line 2 col 17: ["
        self.assertTrue(TestParser.test(input, expect, 209))  
        
    def test_10(self): 
        input = """ 
            func main()
            func main(number n1, number n2)
                var HuyHoang <- 2
            func main(number s1 <- d)
        """
        expect = "Error on line 5 col 32: <-"
        self.assertTrue(TestParser.test(input, expect, 210))       
        
    def test_11(self): 
        input = """ 
            func TT()
            ## Huy Hoang
            func TT() func TT(dynamic b) ## Huy Hoang
        """
        expect = "Error on line 4 col 22: func"
        self.assertTrue(TestParser.test(input, expect, 211))  
        
    def test_12(self): 
        input = """ 
            func cole(var b)
        """
        expect = "Error on line 2 col 22: var"
        self.assertTrue(TestParser.test(input, expect, 212))                 

    def test_13(self): 
        input = """ 
            ##12
            ##12
            
            func muoi(number b) var d <- 2
        """
        expect = "Error on line 5 col 32: var"
        self.assertTrue(TestParser.test(input, expect, 213))  
        
    def test_14(self):         
        input = """ 
            func hotd(string b) 
                begin 
                    continue ## 12
                end
            func hotd(dynamic b) 
        """
        expect = "Error on line 6 col 22: dynamic"
        self.assertTrue(TestParser.test(input, expect, 214))    
        
    def test_15(self): 
        input = """ 
            func duch(number b[2,3,4]) ##12
                break
        """
        expect = "Error on line 3 col 16: break"
        self.assertTrue(TestParser.test(input, expect, 215))    
        
    def test_16(self):         
        input = """
            ##12
            func huhu(number b) 
                ##12
                
                begin 
                    break
                end
                
                ##12
                ##12
            func huhu(number b)
            ##12        
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 216)) 
        
    def test_17(self):
        input = """ 
            ## so tired
            
            var b <- 2 ## 12
            ## 12
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 217))   
        
    def test_18(self): 
        input = """var b <- 2"""
        expect = "Error on line 1 col 10: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 218))
        
    def test_19(self):
        input = """func huhu(number b) """
        expect = "Error on line 1 col 20: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 219))  
                                   
    def test_20(self):
        input = """ var HuyHoang <- "Huy" ... "Hoang" 
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 220))
        
    def test_21(self):
        input = """ var HuyHoang <- "Huy" ... 1 ... "Hoang" 
        """
        expect = "Error on line 1 col 29: ..."
        self.assertTrue(TestParser.test(input, expect, 221))
        
    def test_22(self): 
        input = """ 
            var HuyHoang <- true > "true" 
            var HuyHoang <- true >= "true"
            var HuyHoang <- true = "true"
            var HuyHoang <- true == "true"
            var HuyHoang <- true < "true"
            var HuyHoang <- true <= "true"
            var HuyHoang <- true >= "true" ... 1 > 2
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 222))
        
    def test_23(self): 
        input = """ var HuyHoang <- true > a >= b 
        """
        expect = "Error on line 1 col 26: >="
        self.assertTrue(TestParser.test(input, expect, 223))
        
    def test_24(self): 
        input = """ 
            var HuyHoang <- true and "true" or 1 
            var HuyHoang <- 1 and 2 and 3 or 4 or 4
            var HuyHoang <- 1 + 2 - 2 + 3 and 3
            var HuyHoang <- 1 / 2 * 3 % 4
            var HuyHoang <- 1 / 2 / 2 * 3 % 4
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 224))
        
    def test_25(self): 
        input = """var HuyHoang <- true <= "true" and 1 > 2
        """
        expect = "Error on line 1 col 37: >"
        self.assertTrue(TestParser.test(input, expect, 225)) 
        
    def test_26(self):   
        input = """ 
            var HuyHoang <- -1 * not 1
            var HuyHoang <- not not not----D
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 226)) 
    
    def test_27(self):     
        input = """var HuyHoang <- - not 2
        """
        expect = "Error on line 1 col 18: not"
        self.assertTrue(TestParser.test(input, expect, 227)) 
        
    def test_28(self): 
        input = """ 
            var HuyHoang <- b[2] + 2
            var HuyHoang <- array[2,3+2][4][2,3]
            var HuyHoang <- array[2,(3)...6,array[ar[(5*2) and 7]],array[2]]
            var HuyHoang <- b[8] + fun()[9,fun()] 
            var HuyHoang <- 1[8]
        """
        expect = "Error on line 3 col 40: ["
        self.assertTrue(TestParser.test(input, expect, 228))
        
    def test_29(self): 
        input = """var HuyHoang <- b[]
        """
        expect = "Error on line 1 col 18: ]"
        self.assertTrue(TestParser.test(input, expect, 229)) 
        
    def test_30(self): 
        input = """ 
            var HuyHoang <- b()
            var HuyHoang <- b(1,2)
            var HuyHoang <- b(x,array[2])[2]
            var HuyHoang <- b(z,k[3] ... 2)[1,2]
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 230))    
    
    def test_31(self):     
        input = """var HuyHoang <- b()()
        """
        expect = "Error on line 1 col 19: ("
        self.assertTrue(TestParser.test(input, expect, 231))  
        
    def test_32(self): 
        input = """ 
            var HuyHoang <- b() + ++1 / 2 *3 <= 3 ... "v" >= 2
            var HuyHoang <- b(1,2)[1,2,3 ... 2] + false + true
            var HuyHoang <- b(z,k[2,3,"2"] ... 2)[true]
            var HuyHoang <- (a ... 3) ... b and (a >= b) < b[1, b[1]]
            var HuyHoang <-  ["tr", 2, 3, 4, 5] + [[1, 2 + 2 * 2 / 3, 3], [4, 5, 6]]
            var HuyHoang <- b(x,array[2])[2,3+2,true,false]
        """
        expect = "Error on line 2 col 34: +"
        self.assertTrue(TestParser.test(input, expect, 232))  

    def test_33(self): 
        input = """var HuyHoang <- b[1]()
        """
        expect = "Error on line 1 col 20: ("
        self.assertTrue(TestParser.test(input, expect, 233))         
        
    def test_34(self): 
        input = """
        ## comment
        func huhu()

            ## comment
            begin
            aPI <- 3.1416
            end
            ## comment
            
        ## comment
        
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 234))
    
    def test_35(self):     
        input = """
        func huhu() begin 
        end
        func huhu() 
            begin 
                ## comment0
            end
        func huhu()
            ## comment1
            begin
                ## comment2
                
                ## comment3
                HuyHoang <- 1 + 2 + sad()
                HuyHoang[1+a] <- 1
                
                ## comment4
                HuyHoang[3+4,2,4] <- 3
                
                ## comment5
            end
            ## comment
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 235)) 
    
    def test_36(self):     
        input = """
        func huhu()
            begin
            aPI + 2 <- 5.14
            end
        """
        expect = "Error on line 4 col 16: +"
        self.assertTrue(TestParser.test(input, expect, 236))
    
    def test_37(self):     
        input = """
        func huhu()
            begin
            aPI()<- 4.14 - 1
            end
        """
        expect = "Error on line 4 col 17: <-"
        self.assertTrue(TestParser.test(input, expect, 237))
    
    def test_38(self):     
        input = """
        func huhu()
            begin
            (aPI)[5]<- 3.1416
            end
        """
        expect = "Error on line 4 col 12: ("
        self.assertTrue(TestParser.test(input, expect, 238))
                
    def test_39(self):  
        input = """
        func huhu()
            begin   
                if(1+1) api <- 3.14
                ## comment0
                
                if(1+1) 
                    ## comment1
                    
                    api <- 3.14
                    ## comment2
                else api <- 3.14
                ## comment3
                
                if (1) api <- 3.14
                elif (1 ... 2)
                    ## comment1
                    
                    api <- 3.14
                    ## comment2
                elif (1) api <- 3.14
                
                if (1) api <- 3.14
                elif (1 ... 2) api <- 3.14
                elif (1) api <- 3.14
                else api <- 3.14  
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 239))  
    
    def test_40(self):     
        input = """
        func huhu()
            begin   
                if (api <- 3.14)
            end
        """
        expect = "Error on line 4 col 24: <-"
        self.assertTrue(TestParser.test(input, expect, 240))   
        
    def testcase_41(self):
        input =""" begin
                    end
                    """
        expect = "Error on line 1 col 1: begin"
        self.assertTrue(TestParser.test(input,expect,241))     
        
    def test_42(self): 
        input = """
        func huhu()
            begin
            for j until j >= 11 by 2 + 2
                ## comment
                
                y <- 2
            ## comment
            end
            
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 242))    
    
    def test_43(self):     
        input = """
        func huhu()
            begin
            for j[2] until j >= 10 by 2 + 2
                y <- 2
            end
        """
        expect = "Error on line 4 col 17: ["
        self.assertTrue(TestParser.test(input, expect, 243))    

    def test_44(self): 
        input = """
        func huhu()
            begin
            for j+2 until h >= 22 by 2 + 2
                c <- 2
            end
        """
        expect = "Error on line 4 col 17: +"
        self.assertTrue(TestParser.test(input, expect, 244)) 
    
    def test_45(self):     
        input = """
        func huhu()
        begin 
            break
            continue
            for j until j >= 10 by 2 + 2 ... 4 / 5
                begin
                    break
                    continue
                end
                
            for j until j >= 10 by 2 print(2)
            for h until h >= 10 by 2 
                print(2)
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 245))  
    
    def test_46(self):     
        input = """
        func huhu()
            begin
            for j until k >= 11 by 2 + 2
            end
        """
        expect = "Error on line 5 col 12: end"
        self.assertTrue(TestParser.test(input, expect, 246))  
        
    def test_47(self): 
        input = """
        func huhu()
            return 2 + 2
        """    
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 247))

    def test_48(self): 
        input = """
        func huhu()
            begin
            huhu()
            end
        """    
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 248))
    
    def test_49(self): 
        input = """
        func huhu()
        begin 
            return ([3,2,3]) + 2
            return huhu()
            huhu(3,2)
            sad()
            huhu([3,2,3], 3+2, b, d ... e)
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 249))  
    
    def test_50(self): 
        input = """
        func huhu()
            return func()
        """
        expect = "Error on line 3 col 19: func"
        self.assertTrue(TestParser.test(input, expect, 250))      
    
    def test_51(self):     
        input = """
        func huhu()
            return break
        """
        expect = "Error on line 3 col 19: break"
        self.assertTrue(TestParser.test(input, expect, 251)) 
        
    def test_52(self): 
        input = """
        func huhu()
            begin
                begin
                    begin
                        y <- 1
                    end
                    
                    begin
                        return false
                    end
                    
                    return true
                end
                
                begin
                end
                return false
            end
        """    
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 252))
     
    def test_53(self):
        input = """var aPI <- 3.1416"""
        expect = "Error on line 1 col 17: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 253))          
  
    def test_54(self):
        input = """
        func areDivisors(number num1, number num2)
            return (num1 % num2 = 0 ... num2 % num1 = 0)
        func huhu()
            begin
                var num1 <- readNumber()
                var num2 <- readNumber()
                if (areDivisors(num1, num2)) printString("Yes")
                else printString("No")
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 254))   
        
    def test_55(self): 
        input = """
            func isPrime(number x)
            func huhu()
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
            
            
            for i until i > x / 2 by 1 + 1 var c <- 1
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 255))
        
    def test_56(self):
        input =""" func t56()
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,256))
        
    def test_57(self):
        input =""" 
        func t57()
        begin
        return
        end
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,257))
        
    def test_58(self):
        input =""" 
            func t58()
        begin
        return (true)
        end
         """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,258))
        
    def test_59(self):
        input ="""
                   func xl()
        begin
            begin
                begin
                    return "!I <3 PPL!"
                end
            end
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,259))
        
    def test_60(self):
        input ="""
        var p<- 3.1416
            func main()
                    begin
                    p <- [2,3,4]
                    if (p==2) 
                    else p=2
                    end
                    """
        expect = "Error on line 7 col 20: else"
        self.assertTrue(TestParser.test(input,expect,260))
        
    def test_61(self):
        input =""" stop
        """
        expect = "Error on line 1 col 1: stop"
        self.assertTrue(TestParser.test(input,expect,261))
        
    def test_62(self):
        input ="""var
        """
        expect = "Error on line 1 col 3: \n"
        self.assertTrue(TestParser.test(input,expect,262))
        
    def test_63(self):
        input =""" 
        func main()
            begin   
                if(2+2) api <- 2
                ## comment0
                
                if(2+2) 
                    ## comment1
                    
                    api <- 2
                    ## comment2
                else api <- 2
                ## comment3
                
                if 2 api <- 2
                elif 3 ... 3
                    ## comment1
                    
                    api <- 2
                    ## comment2
                elif 2 api <- 2
                
                if 2 api <- 2
                elif 2 ... 3 api <- 2
                elif 2 api <- 2
                else api <- 2   
            end
        
        """
        expect = """Error on line 15 col 19: 2"""
        self.assertTrue(TestParser.test(input,expect,263))
        
    def test_64(self):
        input ="""
                func main()
        begin 
            return ([2,3,4]) + 2
            return main()
            main(2,3)
            fun()
            main([2,3,4], 2+3, b, d ... f)
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,264))
        
    def test_65(self):
        input ="""
                func main()
            begin
                begin
                    begin
                        x <- 1
                    end
                    
                    begin
                        return false
                    end
                    
                    return true
                end
                
                begin
                end
                return false
            end
            return (NhieuQua)
                        
        """
        expect = "Error on line 20 col 12: return"
        self.assertTrue(TestParser.test(input,expect,265))
        
    def test_66(self):
        input =""" func ohmygod(number y)
 begin
 if (y <= 2) return true
 var j <- 3
 for arr[1] until j > y / 3 by 2
 begin
 if (y % j = 1) return true
 end
 return false
 end
                    """
        expect = "Error on line 5 col 8: ["
        self.assertTrue(TestParser.test(input,expect,266))
        
    def test_67(self):
        input =""" 
        func cuutui()
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,267))
        
    def test_68(self):
        input =""""""
        expect = "Error on line 1 col 0: <EOF>"
        self.assertTrue(TestParser.test(input,expect,268))
        
    def test_69(self):
        input ="""
        
        """
        expect = "Error on line 3 col 8: <EOF>"
        self.assertTrue(TestParser.test(input,expect,269))
        
    def test_70(self):
        input ="""
        var b<- 3.1416
            func main()
                    begin
                    b <- [2,3,4]
                    if (b==2) 
                    else b=2
                    end
                    """
        expect = "Error on line 7 col 20: else"
        self.assertTrue(TestParser.test(input,expect,270))
        
    def test_71(self):
        input ="""  var im_so_sad <- -2e-8
number pi <- 3.1416
dynamic e <- 2.7183
func expe(number m)
begin
var ans <- 1
var j<-0
for j until j=m by 2
return ans
end
func main()
begin
	var b<-exp(9)
end
        
                    """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,271))
        
    def test_72(self):
        input ="""func main()
            func main(number s1)
            func main(number b[6],bool y[3+2,3,4], bool b[6,3,4], string c, bool d)
            func main(number huhu, number hichic)
                var HuyHoang <- 1
            func main(number s1 )
            begin
                main(main()[3,4],arr[3+2,4])
            end
        """
        expect = "Error on line 3 col 42: +"
        self.assertTrue(TestParser.test(input,expect,272))
        
    def test_73(self):
        input =""" 
        func main()
begin
var j<-1
number y<-rNumber()
for j until j<y by 6
y <- y + 2
end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,273))
        
    def test_74(self):
        input ="""
                func main()
        begin 
            bool b <- not not - - (b[b[b[b[b[b[1]]]]]])
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,274))
        
    def test_75(self):
        input ="""
                ## Bao gio thi het DL
                        
        """
        expect = "Error on line 4 col 8: <EOF>"
        self.assertTrue(TestParser.test(input,expect,275))
        
    def test_76(self):
        input =""" var b = "DL di ac qua di"
                func main()
                begin
                    for b[34] until b <3 by 2 return false
                end
                    """
        expect = "Error on line 1 col 7: ="
        self.assertTrue(TestParser.test(input,expect,276))
        
    def test_77(self):
        input =""" 
        var a,b,c <- "SOS"
        func main()
                """
        expect = "Error on line 2 col 13: ,"
        self.assertTrue(TestParser.test(input,expect,277))
        
    def test_78(self):
        input ="""func foo(a,b) return true"""
        expect = "Error on line 1 col 9: a"
        self.assertTrue(TestParser.test(input,expect,278))
        
    def test_79(self):
        input ="""
        func main() begin
for a until a by a
if (a) break
aa()
2
end
        """
        expect = "Error on line 6 col 0: 2"
        self.assertTrue(TestParser.test(input,expect,279))
        
    def test_80(self):
        input ="""
        dynamic b <- [[3+4,f()[3],3],3,[4,5]]
        func main (number b, number c, bool arr[2,3,[3,4]])
                    """
        expect = "Error on line 3 col 52: ["
        self.assertTrue(TestParser.test(input,expect,280))
        
    def test_81(self):
        input ="""  string b <- "Cuoc song ma"
        func main(bool b <- false)
        func isEven()
                    """
        expect = "Error on line 2 col 25: <-"
        self.assertTrue(TestParser.test(input,expect,281))
        
    def test_82(self):
        input =""" 
        func face()
        begin
            newlive()
            newlive()
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,282))
        
    def test_83(self):
        input =""" 
        func main()
begin
var a<-0
var b<-0
var c<-0
number z<-readNumber()
for a until a<z by 5
for b until b<z by i
for c until c<z by 1 var i <- "Tinh dau kho phai"
end
        
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,283))
        
    def test_84(self):
        input ="""
                func main()
        begin 
            bool b <- b[not not - - (b[b[b[b[b[b[1]]]]]]), 3+4/5,[2,3,4,5]]
        end
        var c <- b(2,3)[2,3,4 ... 3] + false + true
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,284))
        
    def test_85(self):
        input ="""
            func main()
            begin
                for j until j<2 by b%3+6-5 
                    for k until j by b[6] 
                        for l until k by fun()[b] return
            end    
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,285))
        
    def test_86(self):
        input =""" func main(bool hehe[3])
            begin
                
                return TT
                return VV
                return AA
                bool hehe[hihi]
            end
                    """
        expect = "Error on line 7 col 26: hihi"
        self.assertTrue(TestParser.test(input,expect,286))
        
    def test_87(self):
        input =""" 
        func b() ##HAPPY BIRTHDAY
        begin
            b[_4 + f(_3)] <- b[_c[_3, _4]] + _5 
        end
        
        
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,287))
        
    def test_88(self):
        input ="""
        begin
            if (d...e <= 2) return false else b<-2
        end
        func abc(number x)
        """
        expect = "Error on line 2 col 8: begin"
        self.assertTrue(TestParser.test(input,expect,288))
        
    def test_89(self):
        input ="""
        func main() begin
for a until a by a
if (a) break up
aa()
2
end
        """
        expect = "Error on line 4 col 13: up"
        self.assertTrue(TestParser.test(input,expect,289))
        
    def test_90(self):
        input ="""
        func foo()
        begin      
            begin   
                if(2+2) a <- 2
                elif (3+3=6) a <- 3
                
                if(2+2) a <- 2
                else a <- 2
                ## comment
                
                if (2) a <- 2
                elif 2 ... 3
     
                    a <- 2
                elif (2) a <- 2
                
                if (2) a <- 2
                elif (2 ... 3) a <- 2
                elif 2 a <- 2
                else a <- 2   
            end
        end
                    """
        expect = "Error on line 13 col 21: 2"
        self.assertTrue(TestParser.test(input,expect,290))
        
    def test_91(self):
        input ="""  string a <- "u r my life"
        bool b <- false
        func main()
        func isEven()
                    """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,291))
        
    def test_92(self):
        input =""" 
        var tymm <- "<3"
        func interface(newlive())
        begin
            
            newlive()
        end
        """
        expect = "Error on line 3 col 23: newlive"
        self.assertTrue(TestParser.test(input,expect,292))
        
    def test_93(self):
        input =""" 
        func foo(number b[6], string c)
        begin
            var j <- 1
            for j until j >= 6 by 2
                begin
                    b[j] <- j * j + 6
                end
            return 0
        end
        
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,293))
        
    def test_94(self):
        input ="""
                func main() begin
        number a <- readNumber()
        var b <- 1.
        dynamic c
end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,294))
        
    def test_95(self):
        input ="""
            func main() begin
        bool _c[2] <- [true]
        number b[3,3] <- [[2,3],[4,5]]
        b[2,2] <- b[2,3]
end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,295))
        
    def test_96(self):
        input =""" func main(bool haha[3])
            begin
                bool LoveYou = - - - (not (-(not a[2+4%5,a<4,function(a+3)])))
                return honey
                bool hihi[hehe]
            end
                    """
        expect = "Error on line 3 col 29: ="
        self.assertTrue(TestParser.test(input,expect,296))
        
    def test_97(self):
        input =""" 
        func main()
        begin
            b[_4 + foo(_5)] <- b[_c[_6, _7]] + _8 
        end
        func b() ##HAPPY BIRTHDAY
        
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,297))
        
    def test_98(self):
        input ="""
        fu main()
        begin
            continue
        end
        break
        func abc(number x)
        """
        expect = "Error on line 2 col 8: fu"
        self.assertTrue(TestParser.test(input,expect,298))
        
    def test_99(self):
        input ="""
        func main() 
        begin 
            var test
        end
        """
        expect = """Error on line 4 col 20: \n"""
        self.assertTrue(TestParser.test(input,expect,299))