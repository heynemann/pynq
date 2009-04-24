#!/usr/bin/env python
#-*- coding:utf-8 -*-

# Licensed under the Open Software License ("OSL") v. 3.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.opensource.org/licenses/osl-3.0.php

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest
import re
import sys
from os.path import dirname, abspath, join
root_path = abspath(join(dirname(__file__), "../../"))
sys.path.insert(0, root_path)

from pynq.expressions import Expression, ConstantExpression, BinaryExpression
from base import BaseUnitTest

class TestBinaryBooleanExpressions(BaseUnitTest):

#Equals
    def test_expression_equal_of_two_constants(self):
        a = ConstantExpression(True)
        b = ConstantExpression(False)
        node_type = BinaryExpression.Equal
        expr = BinaryExpression(node_type, a, b)

        self.assertEquals(expr.node_type, node_type)
        self.assertEquals(expr.lhs, a)
        self.assertEquals(expr.rhs, b)

    def test_expression_equal_of_two_constants_representation(self):
        a = ConstantExpression(True)
        b = ConstantExpression(False)
        node_type = BinaryExpression.Equal
        expr = BinaryExpression(node_type, a, b)
        
        self.assertEquals("(True == False)", str(expr))

    def test_nested_equal_expression(self):
        a = ConstantExpression(True)
        b = ConstantExpression(False)
        c = ConstantExpression(None)
        node_type = BinaryExpression.Equal

        expr = BinaryExpression(node_type, BinaryExpression(node_type, a, b), c)

        self.assertEquals(expr.node_type, node_type)
        self.failUnless(isinstance(expr.lhs, BinaryExpression), "The left-hand side of the binary expression should be a binary expression as well, but is %s" % expr.lhs.__class__)
        self.assertEquals(expr.lhs.node_type, node_type)
        self.assertEquals(expr.lhs.lhs, a)
        self.assertEquals(expr.lhs.rhs, b)
        self.assertEquals(expr.rhs, c)
    
    def test_nested_equal_expression_representation(self):
        a = ConstantExpression(True)
        b = ConstantExpression(False)
        c = ConstantExpression(None)
        node_type = BinaryExpression.Equal

        expr = BinaryExpression(node_type, BinaryExpression(node_type, a, b), c)

        self.assertEquals("((True == False) == None)", str(expr))

#Not Equal
    def test_expression_not_equal_of_two_constants(self):
        a = ConstantExpression(True)
        b = ConstantExpression(False)
        node_type = BinaryExpression.NotEqual
        expr = BinaryExpression(node_type, a, b)

        self.assertEquals(expr.node_type, node_type)
        self.assertEquals(expr.lhs, a)
        self.assertEquals(expr.rhs, b)

    def test_expression_not_equal_of_two_constants_representation(self):
        a = ConstantExpression(True)
        b = ConstantExpression(False)
        node_type = BinaryExpression.NotEqual
        expr = BinaryExpression(node_type, a, b)
        
        self.assertEquals("(True != False)", str(expr))

    def test_nested_not_equal_expression(self):
        a = ConstantExpression(True)
        b = ConstantExpression(False)
        c = ConstantExpression(None)
        node_type = BinaryExpression.NotEqual

        expr = BinaryExpression(node_type, BinaryExpression(node_type, a, b), c)

        self.assertEquals(expr.node_type, node_type)
        self.failUnless(isinstance(expr.lhs, BinaryExpression), "The left-hand side of the binary expression should be a binary expression as well, but is %s" % expr.lhs.__class__)
        self.assertEquals(expr.lhs.node_type, node_type)
        self.assertEquals(expr.lhs.lhs, a)
        self.assertEquals(expr.lhs.rhs, b)
        self.assertEquals(expr.rhs, c)
    
    def test_nested_not_equal_expression_representation(self):
        a = ConstantExpression(True)
        b = ConstantExpression(False)
        c = ConstantExpression(None)
        node_type = BinaryExpression.NotEqual

        expr = BinaryExpression(node_type, BinaryExpression(node_type, a, b), c)

        self.assertEquals("((True != False) != None)", str(expr))

#Greater Than
    def test_expression_greater_than_of_two_constants(self):
        a = ConstantExpression(True)
        b = ConstantExpression(False)
        node_type = BinaryExpression.GreaterThan
        expr = BinaryExpression(node_type, a, b)

        self.assertEquals(expr.node_type, node_type)
        self.assertEquals(expr.lhs, a)
        self.assertEquals(expr.rhs, b)

    def test_expression_greater_than_of_two_constants_representation(self):
        a = ConstantExpression(True)
        b = ConstantExpression(False)
        node_type = BinaryExpression.GreaterThan
        expr = BinaryExpression(node_type, a, b)
        
        self.assertEquals("(True > False)", str(expr))

    def test_nested_greater_than_expression(self):
        a = ConstantExpression(True)
        b = ConstantExpression(False)
        c = ConstantExpression(None)
        node_type = BinaryExpression.GreaterThan

        expr = BinaryExpression(node_type, BinaryExpression(node_type, a, b), c)

        self.assertEquals(expr.node_type, node_type)
        self.failUnless(isinstance(expr.lhs, BinaryExpression), "The left-hand side of the binary expression should be a binary expression as well, but is %s" % expr.lhs.__class__)
        self.assertEquals(expr.lhs.node_type, node_type)
        self.assertEquals(expr.lhs.lhs, a)
        self.assertEquals(expr.lhs.rhs, b)
        self.assertEquals(expr.rhs, c)
    
    def test_nested_greater_than_expression_representation(self):
        a = ConstantExpression(True)
        b = ConstantExpression(False)
        c = ConstantExpression(None)
        node_type = BinaryExpression.GreaterThan

        expr = BinaryExpression(node_type, BinaryExpression(node_type, a, b), c)

        self.assertEquals("((True > False) > None)", str(expr))

#Greater Than or Equal
    def test_expression_greater_than_or_equal_of_two_constants(self):
        a = ConstantExpression(True)
        b = ConstantExpression(False)
        node_type = BinaryExpression.GreaterThanOrEqual
        expr = BinaryExpression(node_type, a, b)

        self.assertEquals(expr.node_type, node_type)
        self.assertEquals(expr.lhs, a)
        self.assertEquals(expr.rhs, b)

    def test_expression_greater_than_or_equal_of_two_constants_representation(self):
        a = ConstantExpression(True)
        b = ConstantExpression(False)
        node_type = BinaryExpression.GreaterThanOrEqual
        expr = BinaryExpression(node_type, a, b)
        
        self.assertEquals("(True >= False)", str(expr))

    def test_nested_greater_than_or_equal_expression(self):
        a = ConstantExpression(True)
        b = ConstantExpression(False)
        c = ConstantExpression(None)
        node_type = BinaryExpression.GreaterThanOrEqual

        expr = BinaryExpression(node_type, BinaryExpression(node_type, a, b), c)

        self.assertEquals(expr.node_type, node_type)
        self.failUnless(isinstance(expr.lhs, BinaryExpression), "The left-hand side of the binary expression should be a binary expression as well, but is %s" % expr.lhs.__class__)
        self.assertEquals(expr.lhs.node_type, node_type)
        self.assertEquals(expr.lhs.lhs, a)
        self.assertEquals(expr.lhs.rhs, b)
        self.assertEquals(expr.rhs, c)
    
    def test_nested_greater_than_or_equal_expression_representation(self):
        a = ConstantExpression(True)
        b = ConstantExpression(False)
        c = ConstantExpression(None)
        node_type = BinaryExpression.GreaterThanOrEqual

        expr = BinaryExpression(node_type, BinaryExpression(node_type, a, b), c)

        self.assertEquals("((True >= False) >= None)", str(expr))

#Less Than
    def test_expression_less_than_of_two_constants(self):
        a = ConstantExpression(True)
        b = ConstantExpression(False)
        node_type = BinaryExpression.LessThan
        expr = BinaryExpression(node_type, a, b)

        self.assertEquals(expr.node_type, node_type)
        self.assertEquals(expr.lhs, a)
        self.assertEquals(expr.rhs, b)

    def test_expression_less_than_of_two_constants_representation(self):
        a = ConstantExpression(True)
        b = ConstantExpression(False)
        node_type = BinaryExpression.LessThan
        expr = BinaryExpression(node_type, a, b)
        
        self.assertEquals("(True < False)", str(expr))

    def test_nested_less_than_expression(self):
        a = ConstantExpression(True)
        b = ConstantExpression(False)
        c = ConstantExpression(None)
        node_type = BinaryExpression.LessThan

        expr = BinaryExpression(node_type, BinaryExpression(node_type, a, b), c)

        self.assertEquals(expr.node_type, node_type)
        self.failUnless(isinstance(expr.lhs, BinaryExpression), "The left-hand side of the binary expression should be a binary expression as well, but is %s" % expr.lhs.__class__)
        self.assertEquals(expr.lhs.node_type, node_type)
        self.assertEquals(expr.lhs.lhs, a)
        self.assertEquals(expr.lhs.rhs, b)
        self.assertEquals(expr.rhs, c)
    
    def test_nested_less_than_expression_representation(self):
        a = ConstantExpression(True)
        b = ConstantExpression(False)
        c = ConstantExpression(None)
        node_type = BinaryExpression.LessThan

        expr = BinaryExpression(node_type, BinaryExpression(node_type, a, b), c)

        self.assertEquals("((True < False) < None)", str(expr))

#Less Than or Equal
    def test_expression_less_than_or_equal_of_two_constants(self):
        a = ConstantExpression(True)
        b = ConstantExpression(False)
        node_type = BinaryExpression.LessThanOrEqual
        expr = BinaryExpression(node_type, a, b)

        self.assertEquals(expr.node_type, node_type)
        self.assertEquals(expr.lhs, a)
        self.assertEquals(expr.rhs, b)

    def test_expression_less_than_or_equal_of_two_constants_representation(self):
        a = ConstantExpression(True)
        b = ConstantExpression(False)
        node_type = BinaryExpression.LessThanOrEqual
        expr = BinaryExpression(node_type, a, b)
        
        self.assertEquals("(True <= False)", str(expr))

    def test_nested_less_than_or_equal_expression(self):
        a = ConstantExpression(True)
        b = ConstantExpression(False)
        c = ConstantExpression(None)
        node_type = BinaryExpression.LessThanOrEqual

        expr = BinaryExpression(node_type, BinaryExpression(node_type, a, b), c)

        self.assertEquals(expr.node_type, node_type)
        self.failUnless(isinstance(expr.lhs, BinaryExpression), "The left-hand side of the binary expression should be a binary expression as well, but is %s" % expr.lhs.__class__)
        self.assertEquals(expr.lhs.node_type, node_type)
        self.assertEquals(expr.lhs.lhs, a)
        self.assertEquals(expr.lhs.rhs, b)
        self.assertEquals(expr.rhs, c)
    
    def test_nested_less_than_or_equal_expression_representation(self):
        a = ConstantExpression(True)
        b = ConstantExpression(False)
        c = ConstantExpression(None)
        node_type = BinaryExpression.LessThanOrEqual

        expr = BinaryExpression(node_type, BinaryExpression(node_type, a, b), c)

        self.assertEquals("((True <= False) <= None)", str(expr))

if __name__ == '__main__':
    unittest.main()
