import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        input = """
            func foo(number a) return "1"
            func main() 
            begin
                dynamic x
                var a <- foo([x, x]) ... x
            end
        """
        expect = """Program([FuncDecl(Id(main), [], Block([VarDecl(Id(a), None, dynamic, None), VarDecl(Id(b), None, dynamic, None), VarDecl(Id(arr), ArrayType([2.0, 2.0], NumberType), None, ArrayLit(ArrayLit(Id(a), Id(b)))), VarDecl(Id(c), ArrayType([2.0, 2.0], NumberType), None, Id(arr))]))])"""
        self.assertTrue(TestAST.test(input, expect, 300))
