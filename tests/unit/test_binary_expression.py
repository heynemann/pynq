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

class TestBinaryExpression(BaseUnitTest):

    def test_binary_expression_only_accepts_expressions_for_arguments(self):
        a = 10
        a_expr = ConstantExpression(10)
        b = "20"
        b_expr = ConstantExpression(20)
        node_type = BinaryExpression.Add
        
        self.assertRaisesEx(ValueError, BinaryExpression, node_type, a, b_expr, exc_pattern=re.compile("Lhs must be an expression \(an instance of a class that inherits from pynq.Expression\)"))
        self.assertRaisesEx(ValueError, BinaryExpression, node_type, a_expr, b, exc_pattern=re.compile("Rhs must be an expression \(an instance of a class that inherits from pynq.Expression\)"))
        self.assertRaisesEx(ValueError, BinaryExpression, None, a_expr, b_expr, exc_pattern=re.compile("The BinaryExpression node type is required"))

    def test_expression_for_addition_of_two_constants(self):
        a = ConstantExpression(10)
        b = ConstantExpression(20)
        node_type = BinaryExpression.Add
        expr = BinaryExpression(node_type, a, b)

        self.assertEquals(expr.node_type, node_type)
        self.assertEquals(expr.lhs, a)
        self.assertEquals(expr.rhs, b)

    def test_expression_for_addition_of_two_constants_representation(self):
        a = ConstantExpression(10)
        b = ConstantExpression(20)
        node_type = BinaryExpression.Add
        expr = BinaryExpression(node_type, a, b)
        
        self.assertEquals("(10 + 20)", str(expr))

    def test_nested_addition_expression(self):
        a = ConstantExpression(10)
        b = ConstantExpression(20)
        c = ConstantExpression(30)
        add_node = BinaryExpression.Add

        expr = BinaryExpression(add_node, BinaryExpression(add_node, a, b), c)

        self.assertEquals(expr.node_type, add_node)
        self.failUnless(isinstance(expr.lhs, BinaryExpression), "The left-hand side of the binary expression should be a binary expression as well, but is %s" % expr.lhs.__class__)
        self.assertEquals(expr.lhs.node_type, add_node)
        self.assertEquals(expr.lhs.lhs, a)
        self.assertEquals(expr.lhs.rhs, b)
        self.assertEquals(expr.rhs, c)
    
    def test_nested_addition_expression_representation(self):
        a = ConstantExpression(10)
        b = ConstantExpression(20)
        c = ConstantExpression(30)
        add_node = BinaryExpression.Add

        expr = BinaryExpression(add_node, BinaryExpression(add_node, a, b), c)

        self.assertEquals("((10 + 20) + 30)", str(expr))

if __name__ == '__main__':
    unittest.main()
