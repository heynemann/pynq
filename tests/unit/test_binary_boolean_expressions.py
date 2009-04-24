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

#And Also
    def test_expression_and_also_of_two_constants(self):
        a = ConstantExpression(True)
        b = ConstantExpression(False)
        node_type = BinaryExpression.AndAlso
        expr = BinaryExpression(node_type, a, b)

        self.assertEquals(expr.node_type, node_type)
        self.assertEquals(expr.lhs, a)
        self.assertEquals(expr.rhs, b)

    def test_expression_and_also_of_two_constants_representation(self):
        a = ConstantExpression(True)
        b = ConstantExpression(False)
        node_type = BinaryExpression.AndAlso
        expr = BinaryExpression(node_type, a, b)
        
        self.assertEquals("(True and also False)", str(expr))

    def test_nested_and_also_expression(self):
        a = ConstantExpression(True)
        b = ConstantExpression(False)
        c = ConstantExpression(None)
        node_type = BinaryExpression.AndAlso

        expr = BinaryExpression(node_type, BinaryExpression(node_type, a, b), c)

        self.assertEquals(expr.node_type, node_type)
        self.failUnless(isinstance(expr.lhs, BinaryExpression), "The left-hand side of the binary expression should be a binary expression as well, but is %s" % expr.lhs.__class__)
        self.assertEquals(expr.lhs.node_type, node_type)
        self.assertEquals(expr.lhs.lhs, a)
        self.assertEquals(expr.lhs.rhs, b)
        self.assertEquals(expr.rhs, c)
    
    def test_nested_and_also_expression_representation(self):
        a = ConstantExpression(True)
        b = ConstantExpression(False)
        c = ConstantExpression(None)
        node_type = BinaryExpression.AndAlso

        expr = BinaryExpression(node_type, BinaryExpression(node_type, a, b), c)

        self.assertEquals("((True and also False) and also None)", str(expr))
        
#Or Else
    def test_expression_or_else_of_two_constants(self):
        a = ConstantExpression(True)
        b = ConstantExpression(False)
        node_type = BinaryExpression.OrElse
        expr = BinaryExpression(node_type, a, b)

        self.assertEquals(expr.node_type, node_type)
        self.assertEquals(expr.lhs, a)
        self.assertEquals(expr.rhs, b)

    def test_expression_or_else_of_two_constants_representation(self):
        a = ConstantExpression(True)
        b = ConstantExpression(False)
        node_type = BinaryExpression.OrElse
        expr = BinaryExpression(node_type, a, b)
        
        self.assertEquals("(True or else False)", str(expr))

    def test_nested_or_else_expression(self):
        a = ConstantExpression(True)
        b = ConstantExpression(False)
        c = ConstantExpression(None)
        node_type = BinaryExpression.OrElse

        expr = BinaryExpression(node_type, BinaryExpression(node_type, a, b), c)

        self.assertEquals(expr.node_type, node_type)
        self.failUnless(isinstance(expr.lhs, BinaryExpression), "The left-hand side of the binary expression should be a binary expression as well, but is %s" % expr.lhs.__class__)
        self.assertEquals(expr.lhs.node_type, node_type)
        self.assertEquals(expr.lhs.lhs, a)
        self.assertEquals(expr.lhs.rhs, b)
        self.assertEquals(expr.rhs, c)
    
    def test_nested_or_else_expression_representation(self):
        a = ConstantExpression(True)
        b = ConstantExpression(False)
        c = ConstantExpression(None)
        node_type = BinaryExpression.OrElse

        expr = BinaryExpression(node_type, BinaryExpression(node_type, a, b), c)

        self.assertEquals("((True or else False) or else None)", str(expr))

if __name__ == '__main__':
    unittest.main()
