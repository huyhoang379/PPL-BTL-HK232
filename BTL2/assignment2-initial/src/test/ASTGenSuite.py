import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test_00(self):
        input = """number a
        """
        expect = str(Program([VarDecl(Id("a"), NumberType())]))
        self.assertTrue(TestAST.test(input, expect, 300))
        
    def test_01(self):
        input = """var str <- "Hello world!"
        """
        expect = """Program([VarDecl(Id(str), None, var, StringLit(Hello world!))])"""
        self.assertTrue(TestAST.test(input, expect, 301))
        
    def test_02(self):
        input = """func main() return 1
        """
        expect = """Program([FuncDecl(Id(main), [], Return(NumLit(1.0)))])"""
        self.assertTrue(TestAST.test(input, expect, 302))
        
    def test_03(self):
        input = """func inc(number a) return a + 1
        func main() begin
        var a <- 1
        inc(a)
        writeNumber(a)
        end
        """
        expect = """Program([FuncDecl(Id(inc), [VarDecl(Id(a), NumberType, None, None)], Return(BinaryOp(+, Id(a), NumLit(1.0)))), FuncDecl(Id(main), [], Block([VarDecl(Id(a), None, var, NumLit(1.0)), CallStmt(Id(inc), [Id(a)]), CallStmt(Id(writeNumber), [Id(a)])]))])"""
        self.assertTrue(TestAST.test(input, expect, 303))

    def test_04(self):
        input = """func main() begin
        number a
        if (5 < 2) a <- 1
        elif (not true) a <- 2
        elif ("h" == "6") a <- 3
        end
        """
        expect = """Program([FuncDecl(Id(main), [], Block([VarDecl(Id(a), NumberType, None, None), If((BinaryOp(<, NumLit(5.0), NumLit(2.0)), AssignStmt(Id(a), NumLit(1.0))), [(UnaryOp(not, BooleanLit(True)), AssignStmt(Id(a), NumLit(2.0))), (BinaryOp(==, StringLit(h), StringLit(6)), AssignStmt(Id(a), NumLit(3.0)))], None)]))])"""
        self.assertTrue(TestAST.test(input, expect, 304))
        
    def test_05(self):
        input = """func main() begin
        if (1) writeString("1")
        elif (2) if(3) writeString("1")
        elif (4) writeString("1")
        else writeString("1")
        end
        """
        expect = """Program([FuncDecl(Id(main), [], Block([If((NumLit(1.0), CallStmt(Id(writeString), [StringLit(1)])), [(NumLit(2.0), If((NumLit(3.0), CallStmt(Id(writeString), [StringLit(1)])), [(NumLit(4.0), CallStmt(Id(writeString), [StringLit(1)]))], CallStmt(Id(writeString), [StringLit(1)])))], None)]))])"""
        self.assertTrue(TestAST.test(input, expect, 305))
        
    def test_06(self):
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
        expect = """Program([FuncDecl(Id(main), [], Block([VarDecl(Id(i), None, var, NumLit(0.0)), VarDecl(Id(j), NumberType, None, NumLit(0.0)), For(Id(i), BinaryOp(<=, Id(i), NumLit(10.0)), NumLit(2.0), Block([For(Id(j), BinaryOp(<=, Id(j), NumLit(20.0)), NumLit(4.0), CallStmt(Id(writeNumber), [BinaryOp(*, Id(i), Id(j))]))]))]))])"""
        self.assertTrue(TestAST.test(input, expect, 306))
        
    def test_07(self):
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
        expect = """Program([VarDecl(Id(a), NumberType, None, NumLit(100.0)), FuncDecl(Id(sum), [VarDecl(Id(n), NumberType, None, None)], Block([If((BinaryOp(=, Id(n), NumLit(0.0)), Return(NumLit(0.0))), [], None), Return(BinaryOp(+, Id(n), CallExpr(Id(sum), [BinaryOp(-, Id(n), NumLit(1.0))])))])), FuncDecl(Id(main), [], Block([CallStmt(Id(writeNumber), [CallExpr(Id(sum), [Id(a)])])]))])"""
        self.assertTrue(TestAST.test(input, expect, 307))
        
    def test_08(self):
        input = """number a
        """
        expect = str(Program([VarDecl(Id("a"), NumberType())]))
        self.assertTrue(TestAST.test(input, expect, 308))
        
    def test_09(self):
        input = """var str <- "Hello world!"
        """
        expect = """Program([VarDecl(Id(str), None, var, StringLit(Hello world!))])"""
        self.assertTrue(TestAST.test(input, expect, 309))
        
    def test_10(self):
        input = """func main() return 1
        """
        expect = """Program([FuncDecl(Id(main), [], Return(NumLit(1.0)))])"""
        self.assertTrue(TestAST.test(input, expect, 310))
        
    def test_11(self):
        input = """func inc(number a) return a + 1
        func main() begin
        var a <- 1
        inc(a)
        writeNumber(a)
        end
        """
        expect = """Program([FuncDecl(Id(inc), [VarDecl(Id(a), NumberType, None, None)], Return(BinaryOp(+, Id(a), NumLit(1.0)))), FuncDecl(Id(main), [], Block([VarDecl(Id(a), None, var, NumLit(1.0)), CallStmt(Id(inc), [Id(a)]), CallStmt(Id(writeNumber), [Id(a)])]))])"""
        self.assertTrue(TestAST.test(input, expect, 311))

    def test_12(self):
        input = """func main() begin
        number a
        if (5 < 2) a <- 1
        elif (not true) a <- 2
        elif ("h" == "6") a <- 3
        end
        """
        expect = """Program([FuncDecl(Id(main), [], Block([VarDecl(Id(a), NumberType, None, None), If((BinaryOp(<, NumLit(5.0), NumLit(2.0)), AssignStmt(Id(a), NumLit(1.0))), [(UnaryOp(not, BooleanLit(True)), AssignStmt(Id(a), NumLit(2.0))), (BinaryOp(==, StringLit(h), StringLit(6)), AssignStmt(Id(a), NumLit(3.0)))], None)]))])"""
        self.assertTrue(TestAST.test(input, expect, 312))
        
    def test_13(self):
        input = """func main() begin
        if (1) writeString("1")
        elif (2) if(3) writeString("1")
        elif (4) writeString("1")
        else writeString("1")
        end
        """
        expect = """Program([FuncDecl(Id(main), [], Block([If((NumLit(1.0), CallStmt(Id(writeString), [StringLit(1)])), [(NumLit(2.0), If((NumLit(3.0), CallStmt(Id(writeString), [StringLit(1)])), [(NumLit(4.0), CallStmt(Id(writeString), [StringLit(1)]))], CallStmt(Id(writeString), [StringLit(1)])))], None)]))])"""
        self.assertTrue(TestAST.test(input, expect, 313))
        
    def test_14(self):
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
        expect = """Program([FuncDecl(Id(main), [], Block([VarDecl(Id(i), None, var, NumLit(0.0)), VarDecl(Id(j), NumberType, None, NumLit(0.0)), For(Id(i), BinaryOp(<=, Id(i), NumLit(10.0)), NumLit(2.0), Block([For(Id(j), BinaryOp(<=, Id(j), NumLit(20.0)), NumLit(4.0), CallStmt(Id(writeNumber), [BinaryOp(*, Id(i), Id(j))]))]))]))])"""
        self.assertTrue(TestAST.test(input, expect, 314))
        
    def test_15(self):
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
        expect = """Program([VarDecl(Id(a), NumberType, None, NumLit(100.0)), FuncDecl(Id(sum), [VarDecl(Id(n), NumberType, None, None)], Block([If((BinaryOp(=, Id(n), NumLit(0.0)), Return(NumLit(0.0))), [], None), Return(BinaryOp(+, Id(n), CallExpr(Id(sum), [BinaryOp(-, Id(n), NumLit(1.0))])))])), FuncDecl(Id(main), [], Block([CallStmt(Id(writeNumber), [CallExpr(Id(sum), [Id(a)])])]))])"""
        self.assertTrue(TestAST.test(input, expect, 315))
        
    def test_16(self):
        input = """number a
        """
        expect = str(Program([VarDecl(Id("a"), NumberType())]))
        self.assertTrue(TestAST.test(input, expect, 316))
        
    def test_17(self):
        input = """var str <- "Hello world!"
        """
        expect = """Program([VarDecl(Id(str), None, var, StringLit(Hello world!))])"""
        self.assertTrue(TestAST.test(input, expect, 317))
        
    def test_18(self):
        input = """func main() return 1
        """
        expect = """Program([FuncDecl(Id(main), [], Return(NumLit(1.0)))])"""
        self.assertTrue(TestAST.test(input, expect, 318))
        
    def test_19(self):
        input = """func inc(number a) return a + 1
        func main() begin
        var a <- 1
        inc(a)
        writeNumber(a)
        end
        """
        expect = """Program([FuncDecl(Id(inc), [VarDecl(Id(a), NumberType, None, None)], Return(BinaryOp(+, Id(a), NumLit(1.0)))), FuncDecl(Id(main), [], Block([VarDecl(Id(a), None, var, NumLit(1.0)), CallStmt(Id(inc), [Id(a)]), CallStmt(Id(writeNumber), [Id(a)])]))])"""
        self.assertTrue(TestAST.test(input, expect, 319))

    def test_20(self):
        input = """func main() begin
        number a
        if (5 < 2) a <- 1
        elif (not true) a <- 2
        elif ("h" == "6") a <- 3
        end
        """
        expect = """Program([FuncDecl(Id(main), [], Block([VarDecl(Id(a), NumberType, None, None), If((BinaryOp(<, NumLit(5.0), NumLit(2.0)), AssignStmt(Id(a), NumLit(1.0))), [(UnaryOp(not, BooleanLit(True)), AssignStmt(Id(a), NumLit(2.0))), (BinaryOp(==, StringLit(h), StringLit(6)), AssignStmt(Id(a), NumLit(3.0)))], None)]))])"""
        self.assertTrue(TestAST.test(input, expect, 320))
        
    def test_21(self):
        input = """func main() begin
        if (1) writeString("1")
        elif (2) if(3) writeString("1")
        elif (4) writeString("1")
        else writeString("1")
        end
        """
        expect = """Program([FuncDecl(Id(main), [], Block([If((NumLit(1.0), CallStmt(Id(writeString), [StringLit(1)])), [(NumLit(2.0), If((NumLit(3.0), CallStmt(Id(writeString), [StringLit(1)])), [(NumLit(4.0), CallStmt(Id(writeString), [StringLit(1)]))], CallStmt(Id(writeString), [StringLit(1)])))], None)]))])"""
        self.assertTrue(TestAST.test(input, expect, 321))
        
    def test_22(self):
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
        expect = """Program([FuncDecl(Id(main), [], Block([VarDecl(Id(i), None, var, NumLit(0.0)), VarDecl(Id(j), NumberType, None, NumLit(0.0)), For(Id(i), BinaryOp(<=, Id(i), NumLit(10.0)), NumLit(2.0), Block([For(Id(j), BinaryOp(<=, Id(j), NumLit(20.0)), NumLit(4.0), CallStmt(Id(writeNumber), [BinaryOp(*, Id(i), Id(j))]))]))]))])"""
        self.assertTrue(TestAST.test(input, expect, 322))
        
    def test_23(self):
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
        expect = """Program([VarDecl(Id(a), NumberType, None, NumLit(100.0)), FuncDecl(Id(sum), [VarDecl(Id(n), NumberType, None, None)], Block([If((BinaryOp(=, Id(n), NumLit(0.0)), Return(NumLit(0.0))), [], None), Return(BinaryOp(+, Id(n), CallExpr(Id(sum), [BinaryOp(-, Id(n), NumLit(1.0))])))])), FuncDecl(Id(main), [], Block([CallStmt(Id(writeNumber), [CallExpr(Id(sum), [Id(a)])])]))])"""
        self.assertTrue(TestAST.test(input, expect, 323))
        
    def test_24(self):
        input = """number a
        """
        expect = str(Program([VarDecl(Id("a"), NumberType())]))
        self.assertTrue(TestAST.test(input, expect, 324))
        
    def test_25(self):
        input = """var str <- "Hello world!"
        """
        expect = """Program([VarDecl(Id(str), None, var, StringLit(Hello world!))])"""
        self.assertTrue(TestAST.test(input, expect, 325))
        
    def test_26(self):
        input = """func main() return 1
        """
        expect = """Program([FuncDecl(Id(main), [], Return(NumLit(1.0)))])"""
        self.assertTrue(TestAST.test(input, expect, 326))
        
    def test_27(self):
        input = """func inc(number a) return a + 1
        func main() begin
        var a <- 1
        inc(a)
        writeNumber(a)
        end
        """
        expect = """Program([FuncDecl(Id(inc), [VarDecl(Id(a), NumberType, None, None)], Return(BinaryOp(+, Id(a), NumLit(1.0)))), FuncDecl(Id(main), [], Block([VarDecl(Id(a), None, var, NumLit(1.0)), CallStmt(Id(inc), [Id(a)]), CallStmt(Id(writeNumber), [Id(a)])]))])"""
        self.assertTrue(TestAST.test(input, expect, 327))

    def test_28(self):
        input = """func main() begin
        number a
        if (5 < 2) a <- 1
        elif (not true) a <- 2
        elif ("h" == "6") a <- 3
        end
        """
        expect = """Program([FuncDecl(Id(main), [], Block([VarDecl(Id(a), NumberType, None, None), If((BinaryOp(<, NumLit(5.0), NumLit(2.0)), AssignStmt(Id(a), NumLit(1.0))), [(UnaryOp(not, BooleanLit(True)), AssignStmt(Id(a), NumLit(2.0))), (BinaryOp(==, StringLit(h), StringLit(6)), AssignStmt(Id(a), NumLit(3.0)))], None)]))])"""
        self.assertTrue(TestAST.test(input, expect, 328))
        
    def test_29(self):
        input = """func main() begin
        if (1) writeString("1")
        elif (2) if(3) writeString("1")
        elif (4) writeString("1")
        else writeString("1")
        end
        """
        expect = """Program([FuncDecl(Id(main), [], Block([If((NumLit(1.0), CallStmt(Id(writeString), [StringLit(1)])), [(NumLit(2.0), If((NumLit(3.0), CallStmt(Id(writeString), [StringLit(1)])), [(NumLit(4.0), CallStmt(Id(writeString), [StringLit(1)]))], CallStmt(Id(writeString), [StringLit(1)])))], None)]))])"""
        self.assertTrue(TestAST.test(input, expect, 329))
        
    def test_30(self):
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
        expect = """Program([FuncDecl(Id(main), [], Block([VarDecl(Id(i), None, var, NumLit(0.0)), VarDecl(Id(j), NumberType, None, NumLit(0.0)), For(Id(i), BinaryOp(<=, Id(i), NumLit(10.0)), NumLit(2.0), Block([For(Id(j), BinaryOp(<=, Id(j), NumLit(20.0)), NumLit(4.0), CallStmt(Id(writeNumber), [BinaryOp(*, Id(i), Id(j))]))]))]))])"""
        self.assertTrue(TestAST.test(input, expect, 330))
        
    def test_31(self):
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
        expect = """Program([VarDecl(Id(a), NumberType, None, NumLit(100.0)), FuncDecl(Id(sum), [VarDecl(Id(n), NumberType, None, None)], Block([If((BinaryOp(=, Id(n), NumLit(0.0)), Return(NumLit(0.0))), [], None), Return(BinaryOp(+, Id(n), CallExpr(Id(sum), [BinaryOp(-, Id(n), NumLit(1.0))])))])), FuncDecl(Id(main), [], Block([CallStmt(Id(writeNumber), [CallExpr(Id(sum), [Id(a)])])]))])"""
        self.assertTrue(TestAST.test(input, expect, 331))
        
    def test_32(self):
        input = """number a
        """
        expect = str(Program([VarDecl(Id("a"), NumberType())]))
        self.assertTrue(TestAST.test(input, expect, 331))
        
    def test_33(self):
        input = """var str <- "Hello world!"
        """
        expect = """Program([VarDecl(Id(str), None, var, StringLit(Hello world!))])"""
        self.assertTrue(TestAST.test(input, expect, 333))
        
    def test_34(self):
        input = """func main() return 1
        """
        expect = """Program([FuncDecl(Id(main), [], Return(NumLit(1.0)))])"""
        self.assertTrue(TestAST.test(input, expect, 334))
        
    def test_35(self):
        input = """func inc(number a) return a + 1
        func main() begin
        var a <- 1
        inc(a)
        writeNumber(a)
        end
        """
        expect = """Program([FuncDecl(Id(inc), [VarDecl(Id(a), NumberType, None, None)], Return(BinaryOp(+, Id(a), NumLit(1.0)))), FuncDecl(Id(main), [], Block([VarDecl(Id(a), None, var, NumLit(1.0)), CallStmt(Id(inc), [Id(a)]), CallStmt(Id(writeNumber), [Id(a)])]))])"""
        self.assertTrue(TestAST.test(input, expect, 335))

    def test_36(self):
        input = """func main() begin
        number a
        if (5 < 2) a <- 1
        elif (not true) a <- 2
        elif ("h" == "6") a <- 3
        end
        """
        expect = """Program([FuncDecl(Id(main), [], Block([VarDecl(Id(a), NumberType, None, None), If((BinaryOp(<, NumLit(5.0), NumLit(2.0)), AssignStmt(Id(a), NumLit(1.0))), [(UnaryOp(not, BooleanLit(True)), AssignStmt(Id(a), NumLit(2.0))), (BinaryOp(==, StringLit(h), StringLit(6)), AssignStmt(Id(a), NumLit(3.0)))], None)]))])"""
        self.assertTrue(TestAST.test(input, expect, 336))
        
    def test_37(self):
        input = """func main() begin
        if (1) writeString("1")
        elif (2) if(3) writeString("1")
        elif (4) writeString("1")
        else writeString("1")
        end
        """
        expect = """Program([FuncDecl(Id(main), [], Block([If((NumLit(1.0), CallStmt(Id(writeString), [StringLit(1)])), [(NumLit(2.0), If((NumLit(3.0), CallStmt(Id(writeString), [StringLit(1)])), [(NumLit(4.0), CallStmt(Id(writeString), [StringLit(1)]))], CallStmt(Id(writeString), [StringLit(1)])))], None)]))])"""
        self.assertTrue(TestAST.test(input, expect, 337))
        
    def test_38(self):
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
        expect = """Program([FuncDecl(Id(main), [], Block([VarDecl(Id(i), None, var, NumLit(0.0)), VarDecl(Id(j), NumberType, None, NumLit(0.0)), For(Id(i), BinaryOp(<=, Id(i), NumLit(10.0)), NumLit(2.0), Block([For(Id(j), BinaryOp(<=, Id(j), NumLit(20.0)), NumLit(4.0), CallStmt(Id(writeNumber), [BinaryOp(*, Id(i), Id(j))]))]))]))])"""
        self.assertTrue(TestAST.test(input, expect, 338))
        
    def test_39(self):
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
        expect = """Program([VarDecl(Id(a), NumberType, None, NumLit(100.0)), FuncDecl(Id(sum), [VarDecl(Id(n), NumberType, None, None)], Block([If((BinaryOp(=, Id(n), NumLit(0.0)), Return(NumLit(0.0))), [], None), Return(BinaryOp(+, Id(n), CallExpr(Id(sum), [BinaryOp(-, Id(n), NumLit(1.0))])))])), FuncDecl(Id(main), [], Block([CallStmt(Id(writeNumber), [CallExpr(Id(sum), [Id(a)])])]))])"""
        self.assertTrue(TestAST.test(input, expect, 339))
        
    def test_40(self):
        input = """number a
        """
        expect = str(Program([VarDecl(Id("a"), NumberType())]))
        self.assertTrue(TestAST.test(input, expect, 340))
        
    def test_41(self):
        input = """var str <- "Hello world!"
        """
        expect = """Program([VarDecl(Id(str), None, var, StringLit(Hello world!))])"""
        self.assertTrue(TestAST.test(input, expect, 341))
        
    def test_42(self):
        input = """func main() return 1
        """
        expect = """Program([FuncDecl(Id(main), [], Return(NumLit(1.0)))])"""
        self.assertTrue(TestAST.test(input, expect, 342))
        
    def test_43(self):
        input = """func inc(number a) return a + 1
        func main() begin
        var a <- 1
        inc(a)
        writeNumber(a)
        end
        """
        expect = """Program([FuncDecl(Id(inc), [VarDecl(Id(a), NumberType, None, None)], Return(BinaryOp(+, Id(a), NumLit(1.0)))), FuncDecl(Id(main), [], Block([VarDecl(Id(a), None, var, NumLit(1.0)), CallStmt(Id(inc), [Id(a)]), CallStmt(Id(writeNumber), [Id(a)])]))])"""
        self.assertTrue(TestAST.test(input, expect, 343))

    def test_44(self):
        input = """func main() begin
        number a
        if (5 < 2) a <- 1
        elif (not true) a <- 2
        elif ("h" == "6") a <- 3
        end
        """
        expect = """Program([FuncDecl(Id(main), [], Block([VarDecl(Id(a), NumberType, None, None), If((BinaryOp(<, NumLit(5.0), NumLit(2.0)), AssignStmt(Id(a), NumLit(1.0))), [(UnaryOp(not, BooleanLit(True)), AssignStmt(Id(a), NumLit(2.0))), (BinaryOp(==, StringLit(h), StringLit(6)), AssignStmt(Id(a), NumLit(3.0)))], None)]))])"""
        self.assertTrue(TestAST.test(input, expect, 344))
        
    def test_45(self):
        input = """func main() begin
        if (1) writeString("1")
        elif (2) if(3) writeString("1")
        elif (4) writeString("1")
        else writeString("1")
        end
        """
        expect = """Program([FuncDecl(Id(main), [], Block([If((NumLit(1.0), CallStmt(Id(writeString), [StringLit(1)])), [(NumLit(2.0), If((NumLit(3.0), CallStmt(Id(writeString), [StringLit(1)])), [(NumLit(4.0), CallStmt(Id(writeString), [StringLit(1)]))], CallStmt(Id(writeString), [StringLit(1)])))], None)]))])"""
        self.assertTrue(TestAST.test(input, expect, 345))
        
    def test_46(self):
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
        expect = """Program([FuncDecl(Id(main), [], Block([VarDecl(Id(i), None, var, NumLit(0.0)), VarDecl(Id(j), NumberType, None, NumLit(0.0)), For(Id(i), BinaryOp(<=, Id(i), NumLit(10.0)), NumLit(2.0), Block([For(Id(j), BinaryOp(<=, Id(j), NumLit(20.0)), NumLit(4.0), CallStmt(Id(writeNumber), [BinaryOp(*, Id(i), Id(j))]))]))]))])"""
        self.assertTrue(TestAST.test(input, expect, 346))
        
    def test_47(self):
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
        expect = """Program([VarDecl(Id(a), NumberType, None, NumLit(100.0)), FuncDecl(Id(sum), [VarDecl(Id(n), NumberType, None, None)], Block([If((BinaryOp(=, Id(n), NumLit(0.0)), Return(NumLit(0.0))), [], None), Return(BinaryOp(+, Id(n), CallExpr(Id(sum), [BinaryOp(-, Id(n), NumLit(1.0))])))])), FuncDecl(Id(main), [], Block([CallStmt(Id(writeNumber), [CallExpr(Id(sum), [Id(a)])])]))])"""
        self.assertTrue(TestAST.test(input, expect, 347))
        
    def test_48(self):
        input = """number a
        """
        expect = str(Program([VarDecl(Id("a"), NumberType())]))
        self.assertTrue(TestAST.test(input, expect, 348))
        
    def test_49(self):
        input = """var str <- "Hello world!"
        """
        expect = """Program([VarDecl(Id(str), None, var, StringLit(Hello world!))])"""
        self.assertTrue(TestAST.test(input, expect, 349))
        
    def test_50(self):
        input = """func main() return 1
        """
        expect = """Program([FuncDecl(Id(main), [], Return(NumLit(1.0)))])"""
        self.assertTrue(TestAST.test(input, expect, 350))
        
    def test_51(self):
        input = """func inc(number a) return a + 1
        func main() begin
        var a <- 1
        inc(a)
        writeNumber(a)
        end
        """
        expect = """Program([FuncDecl(Id(inc), [VarDecl(Id(a), NumberType, None, None)], Return(BinaryOp(+, Id(a), NumLit(1.0)))), FuncDecl(Id(main), [], Block([VarDecl(Id(a), None, var, NumLit(1.0)), CallStmt(Id(inc), [Id(a)]), CallStmt(Id(writeNumber), [Id(a)])]))])"""
        self.assertTrue(TestAST.test(input, expect, 351))

    def test_52(self):
        input = """func main() begin
        number a
        if (5 < 2) a <- 1
        elif (not true) a <- 2
        elif ("h" == "6") a <- 3
        end
        """
        expect = """Program([FuncDecl(Id(main), [], Block([VarDecl(Id(a), NumberType, None, None), If((BinaryOp(<, NumLit(5.0), NumLit(2.0)), AssignStmt(Id(a), NumLit(1.0))), [(UnaryOp(not, BooleanLit(True)), AssignStmt(Id(a), NumLit(2.0))), (BinaryOp(==, StringLit(h), StringLit(6)), AssignStmt(Id(a), NumLit(3.0)))], None)]))])"""
        self.assertTrue(TestAST.test(input, expect, 352))
        
    def test_53(self):
        input = """func main() begin
        if (1) writeString("1")
        elif (2) if(3) writeString("1")
        elif (4) writeString("1")
        else writeString("1")
        end
        """
        expect = """Program([FuncDecl(Id(main), [], Block([If((NumLit(1.0), CallStmt(Id(writeString), [StringLit(1)])), [(NumLit(2.0), If((NumLit(3.0), CallStmt(Id(writeString), [StringLit(1)])), [(NumLit(4.0), CallStmt(Id(writeString), [StringLit(1)]))], CallStmt(Id(writeString), [StringLit(1)])))], None)]))])"""
        self.assertTrue(TestAST.test(input, expect, 353))
        
    def test_54(self):
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
        expect = """Program([FuncDecl(Id(main), [], Block([VarDecl(Id(i), None, var, NumLit(0.0)), VarDecl(Id(j), NumberType, None, NumLit(0.0)), For(Id(i), BinaryOp(<=, Id(i), NumLit(10.0)), NumLit(2.0), Block([For(Id(j), BinaryOp(<=, Id(j), NumLit(20.0)), NumLit(4.0), CallStmt(Id(writeNumber), [BinaryOp(*, Id(i), Id(j))]))]))]))])"""
        self.assertTrue(TestAST.test(input, expect, 354))
        
    def test_55(self):
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
        expect = """Program([VarDecl(Id(a), NumberType, None, NumLit(100.0)), FuncDecl(Id(sum), [VarDecl(Id(n), NumberType, None, None)], Block([If((BinaryOp(=, Id(n), NumLit(0.0)), Return(NumLit(0.0))), [], None), Return(BinaryOp(+, Id(n), CallExpr(Id(sum), [BinaryOp(-, Id(n), NumLit(1.0))])))])), FuncDecl(Id(main), [], Block([CallStmt(Id(writeNumber), [CallExpr(Id(sum), [Id(a)])])]))])"""
        self.assertTrue(TestAST.test(input, expect, 355))
        
    def test_56(self):
        input = """number a
        """
        expect = str(Program([VarDecl(Id("a"), NumberType())]))
        self.assertTrue(TestAST.test(input, expect, 356))
        
    def test_57(self):
        input = """var str <- "Hello world!"
        """
        expect = """Program([VarDecl(Id(str), None, var, StringLit(Hello world!))])"""
        self.assertTrue(TestAST.test(input, expect, 357))
        
    def test_58(self):
        input = """func main() return 1
        """
        expect = """Program([FuncDecl(Id(main), [], Return(NumLit(1.0)))])"""
        self.assertTrue(TestAST.test(input, expect, 358))
        
    def test_59(self):
        input = """func inc(number a) return a + 1
        func main() begin
        var a <- 1
        inc(a)
        writeNumber(a)
        end
        """
        expect = """Program([FuncDecl(Id(inc), [VarDecl(Id(a), NumberType, None, None)], Return(BinaryOp(+, Id(a), NumLit(1.0)))), FuncDecl(Id(main), [], Block([VarDecl(Id(a), None, var, NumLit(1.0)), CallStmt(Id(inc), [Id(a)]), CallStmt(Id(writeNumber), [Id(a)])]))])"""
        self.assertTrue(TestAST.test(input, expect, 359))

    def test_60(self):
        input = """func main() begin
        number a
        if (5 < 2) a <- 1
        elif (not true) a <- 2
        elif ("h" == "6") a <- 3
        end
        """
        expect = """Program([FuncDecl(Id(main), [], Block([VarDecl(Id(a), NumberType, None, None), If((BinaryOp(<, NumLit(5.0), NumLit(2.0)), AssignStmt(Id(a), NumLit(1.0))), [(UnaryOp(not, BooleanLit(True)), AssignStmt(Id(a), NumLit(2.0))), (BinaryOp(==, StringLit(h), StringLit(6)), AssignStmt(Id(a), NumLit(3.0)))], None)]))])"""
        self.assertTrue(TestAST.test(input, expect, 360))
        
    def test_61(self):
        input = """func main() begin
        if (1) writeString("1")
        elif (2) if(3) writeString("1")
        elif (4) writeString("1")
        else writeString("1")
        end
        """
        expect = """Program([FuncDecl(Id(main), [], Block([If((NumLit(1.0), CallStmt(Id(writeString), [StringLit(1)])), [(NumLit(2.0), If((NumLit(3.0), CallStmt(Id(writeString), [StringLit(1)])), [(NumLit(4.0), CallStmt(Id(writeString), [StringLit(1)]))], CallStmt(Id(writeString), [StringLit(1)])))], None)]))])"""
        self.assertTrue(TestAST.test(input, expect, 361))
        
    def test_62(self):
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
        expect = """Program([FuncDecl(Id(main), [], Block([VarDecl(Id(i), None, var, NumLit(0.0)), VarDecl(Id(j), NumberType, None, NumLit(0.0)), For(Id(i), BinaryOp(<=, Id(i), NumLit(10.0)), NumLit(2.0), Block([For(Id(j), BinaryOp(<=, Id(j), NumLit(20.0)), NumLit(4.0), CallStmt(Id(writeNumber), [BinaryOp(*, Id(i), Id(j))]))]))]))])"""
        self.assertTrue(TestAST.test(input, expect, 362))
        
    def test_63(self):
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
        expect = """Program([VarDecl(Id(a), NumberType, None, NumLit(100.0)), FuncDecl(Id(sum), [VarDecl(Id(n), NumberType, None, None)], Block([If((BinaryOp(=, Id(n), NumLit(0.0)), Return(NumLit(0.0))), [], None), Return(BinaryOp(+, Id(n), CallExpr(Id(sum), [BinaryOp(-, Id(n), NumLit(1.0))])))])), FuncDecl(Id(main), [], Block([CallStmt(Id(writeNumber), [CallExpr(Id(sum), [Id(a)])])]))])"""
        self.assertTrue(TestAST.test(input, expect, 363))
        
    def test_64(self):
        input = """number a
        """
        expect = str(Program([VarDecl(Id("a"), NumberType())]))
        self.assertTrue(TestAST.test(input, expect, 364))
        
    def test_65(self):
        input = """var str <- "Hello world!"
        """
        expect = """Program([VarDecl(Id(str), None, var, StringLit(Hello world!))])"""
        self.assertTrue(TestAST.test(input, expect, 365))
        
    def test_66(self):
        input = """func main() return 1
        """
        expect = """Program([FuncDecl(Id(main), [], Return(NumLit(1.0)))])"""
        self.assertTrue(TestAST.test(input, expect, 366))
        
    def test_67(self):
        input = """func inc(number a) return a + 1
        func main() begin
        var a <- 1
        inc(a)
        writeNumber(a)
        end
        """
        expect = """Program([FuncDecl(Id(inc), [VarDecl(Id(a), NumberType, None, None)], Return(BinaryOp(+, Id(a), NumLit(1.0)))), FuncDecl(Id(main), [], Block([VarDecl(Id(a), None, var, NumLit(1.0)), CallStmt(Id(inc), [Id(a)]), CallStmt(Id(writeNumber), [Id(a)])]))])"""
        self.assertTrue(TestAST.test(input, expect, 367))

    def test_68(self):
        input = """func main() begin
        number a
        if (5 < 2) a <- 1
        elif (not true) a <- 2
        elif ("h" == "6") a <- 3
        end
        """
        expect = """Program([FuncDecl(Id(main), [], Block([VarDecl(Id(a), NumberType, None, None), If((BinaryOp(<, NumLit(5.0), NumLit(2.0)), AssignStmt(Id(a), NumLit(1.0))), [(UnaryOp(not, BooleanLit(True)), AssignStmt(Id(a), NumLit(2.0))), (BinaryOp(==, StringLit(h), StringLit(6)), AssignStmt(Id(a), NumLit(3.0)))], None)]))])"""
        self.assertTrue(TestAST.test(input, expect, 368))
        
    def test_69(self):
        input = """func main() begin
        if (1) writeString("1")
        elif (2) if(3) writeString("1")
        elif (4) writeString("1")
        else writeString("1")
        end
        """
        expect = """Program([FuncDecl(Id(main), [], Block([If((NumLit(1.0), CallStmt(Id(writeString), [StringLit(1)])), [(NumLit(2.0), If((NumLit(3.0), CallStmt(Id(writeString), [StringLit(1)])), [(NumLit(4.0), CallStmt(Id(writeString), [StringLit(1)]))], CallStmt(Id(writeString), [StringLit(1)])))], None)]))])"""
        self.assertTrue(TestAST.test(input, expect, 369))
        
    def test_70(self):
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
        expect = """Program([FuncDecl(Id(main), [], Block([VarDecl(Id(i), None, var, NumLit(0.0)), VarDecl(Id(j), NumberType, None, NumLit(0.0)), For(Id(i), BinaryOp(<=, Id(i), NumLit(10.0)), NumLit(2.0), Block([For(Id(j), BinaryOp(<=, Id(j), NumLit(20.0)), NumLit(4.0), CallStmt(Id(writeNumber), [BinaryOp(*, Id(i), Id(j))]))]))]))])"""
        self.assertTrue(TestAST.test(input, expect, 370))
        
    def test_71(self):
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
        expect = """Program([VarDecl(Id(a), NumberType, None, NumLit(100.0)), FuncDecl(Id(sum), [VarDecl(Id(n), NumberType, None, None)], Block([If((BinaryOp(=, Id(n), NumLit(0.0)), Return(NumLit(0.0))), [], None), Return(BinaryOp(+, Id(n), CallExpr(Id(sum), [BinaryOp(-, Id(n), NumLit(1.0))])))])), FuncDecl(Id(main), [], Block([CallStmt(Id(writeNumber), [CallExpr(Id(sum), [Id(a)])])]))])"""
        self.assertTrue(TestAST.test(input, expect, 371))
        
    def test_72(self):
        input = """number a
        """
        expect = str(Program([VarDecl(Id("a"), NumberType())]))
        self.assertTrue(TestAST.test(input, expect, 372))
        
    def test_73(self):
        input = """var str <- "Hello world!"
        """
        expect = """Program([VarDecl(Id(str), None, var, StringLit(Hello world!))])"""
        self.assertTrue(TestAST.test(input, expect, 373))
        
    def test_74(self):
        input = """func main() return 1
        """
        expect = """Program([FuncDecl(Id(main), [], Return(NumLit(1.0)))])"""
        self.assertTrue(TestAST.test(input, expect, 374))
        
    def test_75(self):
        input = """func inc(number a) return a + 1
        func main() begin
        var a <- 1
        inc(a)
        writeNumber(a)
        end
        """
        expect = """Program([FuncDecl(Id(inc), [VarDecl(Id(a), NumberType, None, None)], Return(BinaryOp(+, Id(a), NumLit(1.0)))), FuncDecl(Id(main), [], Block([VarDecl(Id(a), None, var, NumLit(1.0)), CallStmt(Id(inc), [Id(a)]), CallStmt(Id(writeNumber), [Id(a)])]))])"""
        self.assertTrue(TestAST.test(input, expect, 375))

    def test_76(self):
        input = """func main() begin
        number a
        if (5 < 2) a <- 1
        elif (not true) a <- 2
        elif ("h" == "6") a <- 3
        end
        """
        expect = """Program([FuncDecl(Id(main), [], Block([VarDecl(Id(a), NumberType, None, None), If((BinaryOp(<, NumLit(5.0), NumLit(2.0)), AssignStmt(Id(a), NumLit(1.0))), [(UnaryOp(not, BooleanLit(True)), AssignStmt(Id(a), NumLit(2.0))), (BinaryOp(==, StringLit(h), StringLit(6)), AssignStmt(Id(a), NumLit(3.0)))], None)]))])"""
        self.assertTrue(TestAST.test(input, expect, 376))
        
    def test_77(self):
        input = """func main() begin
        if (1) writeString("1")
        elif (2) if(3) writeString("1")
        elif (4) writeString("1")
        else writeString("1")
        end
        """
        expect = """Program([FuncDecl(Id(main), [], Block([If((NumLit(1.0), CallStmt(Id(writeString), [StringLit(1)])), [(NumLit(2.0), If((NumLit(3.0), CallStmt(Id(writeString), [StringLit(1)])), [(NumLit(4.0), CallStmt(Id(writeString), [StringLit(1)]))], CallStmt(Id(writeString), [StringLit(1)])))], None)]))])"""
        self.assertTrue(TestAST.test(input, expect, 377))
        
    def test_78(self):
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
        expect = """Program([FuncDecl(Id(main), [], Block([VarDecl(Id(i), None, var, NumLit(0.0)), VarDecl(Id(j), NumberType, None, NumLit(0.0)), For(Id(i), BinaryOp(<=, Id(i), NumLit(10.0)), NumLit(2.0), Block([For(Id(j), BinaryOp(<=, Id(j), NumLit(20.0)), NumLit(4.0), CallStmt(Id(writeNumber), [BinaryOp(*, Id(i), Id(j))]))]))]))])"""
        self.assertTrue(TestAST.test(input, expect, 378))
        
    def test_79(self):
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
        expect = """Program([VarDecl(Id(a), NumberType, None, NumLit(100.0)), FuncDecl(Id(sum), [VarDecl(Id(n), NumberType, None, None)], Block([If((BinaryOp(=, Id(n), NumLit(0.0)), Return(NumLit(0.0))), [], None), Return(BinaryOp(+, Id(n), CallExpr(Id(sum), [BinaryOp(-, Id(n), NumLit(1.0))])))])), FuncDecl(Id(main), [], Block([CallStmt(Id(writeNumber), [CallExpr(Id(sum), [Id(a)])])]))])"""
        self.assertTrue(TestAST.test(input, expect, 379))
        
    def test_80(self):
        input = """number a
        """
        expect = str(Program([VarDecl(Id("a"), NumberType())]))
        self.assertTrue(TestAST.test(input, expect, 380))
        
    def test_81(self):
        input = """var str <- "Hello world!"
        """
        expect = """Program([VarDecl(Id(str), None, var, StringLit(Hello world!))])"""
        self.assertTrue(TestAST.test(input, expect, 381))
        
    def test_82(self):
        input = """func main() return 1
        """
        expect = """Program([FuncDecl(Id(main), [], Return(NumLit(1.0)))])"""
        self.assertTrue(TestAST.test(input, expect, 382))
        
    def test_83(self):
        input = """func inc(number a) return a + 1
        func main() begin
        var a <- 1
        inc(a)
        writeNumber(a)
        end
        """
        expect = """Program([FuncDecl(Id(inc), [VarDecl(Id(a), NumberType, None, None)], Return(BinaryOp(+, Id(a), NumLit(1.0)))), FuncDecl(Id(main), [], Block([VarDecl(Id(a), None, var, NumLit(1.0)), CallStmt(Id(inc), [Id(a)]), CallStmt(Id(writeNumber), [Id(a)])]))])"""
        self.assertTrue(TestAST.test(input, expect, 383))

    def test_84(self):
        input = """func main() begin
        number a
        if (5 < 2) a <- 1
        elif (not true) a <- 2
        elif ("h" == "6") a <- 3
        end
        """
        expect = """Program([FuncDecl(Id(main), [], Block([VarDecl(Id(a), NumberType, None, None), If((BinaryOp(<, NumLit(5.0), NumLit(2.0)), AssignStmt(Id(a), NumLit(1.0))), [(UnaryOp(not, BooleanLit(True)), AssignStmt(Id(a), NumLit(2.0))), (BinaryOp(==, StringLit(h), StringLit(6)), AssignStmt(Id(a), NumLit(3.0)))], None)]))])"""
        self.assertTrue(TestAST.test(input, expect, 384))
        
    def test_85(self):
        input = """func main() begin
        if (1) writeString("1")
        elif (2) if(3) writeString("1")
        elif (4) writeString("1")
        else writeString("1")
        end
        """
        expect = """Program([FuncDecl(Id(main), [], Block([If((NumLit(1.0), CallStmt(Id(writeString), [StringLit(1)])), [(NumLit(2.0), If((NumLit(3.0), CallStmt(Id(writeString), [StringLit(1)])), [(NumLit(4.0), CallStmt(Id(writeString), [StringLit(1)]))], CallStmt(Id(writeString), [StringLit(1)])))], None)]))])"""
        self.assertTrue(TestAST.test(input, expect, 385))
        
    def test_86(self):
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
        expect = """Program([FuncDecl(Id(main), [], Block([VarDecl(Id(i), None, var, NumLit(0.0)), VarDecl(Id(j), NumberType, None, NumLit(0.0)), For(Id(i), BinaryOp(<=, Id(i), NumLit(10.0)), NumLit(2.0), Block([For(Id(j), BinaryOp(<=, Id(j), NumLit(20.0)), NumLit(4.0), CallStmt(Id(writeNumber), [BinaryOp(*, Id(i), Id(j))]))]))]))])"""
        self.assertTrue(TestAST.test(input, expect, 386))
        
    def test_87(self):
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
        expect = """Program([VarDecl(Id(a), NumberType, None, NumLit(100.0)), FuncDecl(Id(sum), [VarDecl(Id(n), NumberType, None, None)], Block([If((BinaryOp(=, Id(n), NumLit(0.0)), Return(NumLit(0.0))), [], None), Return(BinaryOp(+, Id(n), CallExpr(Id(sum), [BinaryOp(-, Id(n), NumLit(1.0))])))])), FuncDecl(Id(main), [], Block([CallStmt(Id(writeNumber), [CallExpr(Id(sum), [Id(a)])])]))])"""
        self.assertTrue(TestAST.test(input, expect, 387))
        
    def test_88(self):
        input = """number a
        """
        expect = str(Program([VarDecl(Id("a"), NumberType())]))
        self.assertTrue(TestAST.test(input, expect, 388))
        
    def test_89(self):
        input = """var str <- "Hello world!"
        """
        expect = """Program([VarDecl(Id(str), None, var, StringLit(Hello world!))])"""
        self.assertTrue(TestAST.test(input, expect, 389))
        
    def test_90(self):
        input = """func main() return 1
        """
        expect = """Program([FuncDecl(Id(main), [], Return(NumLit(1.0)))])"""
        self.assertTrue(TestAST.test(input, expect, 390))
        
    def test_91(self):
        input = """func inc(number a) return a + 1
        func main() begin
        var a <- 1
        inc(a)
        writeNumber(a)
        end
        """
        expect = """Program([FuncDecl(Id(inc), [VarDecl(Id(a), NumberType, None, None)], Return(BinaryOp(+, Id(a), NumLit(1.0)))), FuncDecl(Id(main), [], Block([VarDecl(Id(a), None, var, NumLit(1.0)), CallStmt(Id(inc), [Id(a)]), CallStmt(Id(writeNumber), [Id(a)])]))])"""
        self.assertTrue(TestAST.test(input, expect, 391))

    def test_92(self):
        input = """func main() begin
        number a
        if (5 < 2) a <- 1
        elif (not true) a <- 2
        elif ("h" == "6") a <- 3
        end
        """
        expect = """Program([FuncDecl(Id(main), [], Block([VarDecl(Id(a), NumberType, None, None), If((BinaryOp(<, NumLit(5.0), NumLit(2.0)), AssignStmt(Id(a), NumLit(1.0))), [(UnaryOp(not, BooleanLit(True)), AssignStmt(Id(a), NumLit(2.0))), (BinaryOp(==, StringLit(h), StringLit(6)), AssignStmt(Id(a), NumLit(3.0)))], None)]))])"""
        self.assertTrue(TestAST.test(input, expect, 392))
        
    def test_93(self):
        input = """func main() begin
        if (1) writeString("1")
        elif (2) if(3) writeString("1")
        elif (4) writeString("1")
        else writeString("1")
        end
        """
        expect = """Program([FuncDecl(Id(main), [], Block([If((NumLit(1.0), CallStmt(Id(writeString), [StringLit(1)])), [(NumLit(2.0), If((NumLit(3.0), CallStmt(Id(writeString), [StringLit(1)])), [(NumLit(4.0), CallStmt(Id(writeString), [StringLit(1)]))], CallStmt(Id(writeString), [StringLit(1)])))], None)]))])"""
        self.assertTrue(TestAST.test(input, expect, 393))
        
    def test_94(self):
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
        expect = """Program([FuncDecl(Id(main), [], Block([VarDecl(Id(i), None, var, NumLit(0.0)), VarDecl(Id(j), NumberType, None, NumLit(0.0)), For(Id(i), BinaryOp(<=, Id(i), NumLit(10.0)), NumLit(2.0), Block([For(Id(j), BinaryOp(<=, Id(j), NumLit(20.0)), NumLit(4.0), CallStmt(Id(writeNumber), [BinaryOp(*, Id(i), Id(j))]))]))]))])"""
        self.assertTrue(TestAST.test(input, expect, 394))
        
    def test_95(self):
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
        expect = """Program([VarDecl(Id(a), NumberType, None, NumLit(100.0)), FuncDecl(Id(sum), [VarDecl(Id(n), NumberType, None, None)], Block([If((BinaryOp(=, Id(n), NumLit(0.0)), Return(NumLit(0.0))), [], None), Return(BinaryOp(+, Id(n), CallExpr(Id(sum), [BinaryOp(-, Id(n), NumLit(1.0))])))])), FuncDecl(Id(main), [], Block([CallStmt(Id(writeNumber), [CallExpr(Id(sum), [Id(a)])])]))])"""
        self.assertTrue(TestAST.test(input, expect, 395))
        
    def test_96(self):
        input = """number a
        """
        expect = str(Program([VarDecl(Id("a"), NumberType())]))
        self.assertTrue(TestAST.test(input, expect, 396))
        
    def test_97(self):
        input = """var str <- "Hello world!"
        """
        expect = """Program([VarDecl(Id(str), None, var, StringLit(Hello world!))])"""
        self.assertTrue(TestAST.test(input, expect, 397))
        
    def test_98(self):
        input = """func main() return 1
        """
        expect = """Program([FuncDecl(Id(main), [], Return(NumLit(1.0)))])"""
        self.assertTrue(TestAST.test(input, expect, 398))
        
    def test_99(self):
        input = """func inc(number a) return a + 1
        func main() begin
        var a <- 1
        inc(a)
        writeNumber(a)
        end
        """
        expect = """Program([FuncDecl(Id(inc), [VarDecl(Id(a), NumberType, None, None)], Return(BinaryOp(+, Id(a), NumLit(1.0)))), FuncDecl(Id(main), [], Block([VarDecl(Id(a), None, var, NumLit(1.0)), CallStmt(Id(inc), [Id(a)]), CallStmt(Id(writeNumber), [Id(a)])]))])"""
        self.assertTrue(TestAST.test(input, expect, 399))