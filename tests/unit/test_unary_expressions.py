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

from pynq.expressions import Expression, ConstantExpression, UnaryExpression
from base import BaseUnitTest

class TestUnaryExpressions(BaseUnitTest):

#CollectionLength
    def test_expression_length_of_constant(self):
        a = ConstantExpression(["a","b"])
        node_type = UnaryExpression.CollectionLength
        expr = UnaryExpression(node_type, a)

        self.assertEquals(expr.node_type, node_type)
        self.assertEquals(expr.rhs, a)

    def test_expression_equal_of_two_constants_representation(self):
        a = ConstantExpression(["a","b"])
        node_type = UnaryExpression.CollectionLength
        expr = UnaryExpression(node_type, a)

        self.assertEquals("len(['a', 'b'])", str(expr))
    
    def test_expression_length_can_only_accept_constant_expression_of_list_types(self):
        a = ConstantExpression(["a","b"])
        b = ConstantExpression("b")
        node_type = UnaryExpression.CollectionLength

        expr = UnaryExpression(node_type, a)
        self.assertRaisesEx(ValueError, UnaryExpression, node_type, "some string", exc_pattern=re.compile("The CollectionLength unary expression can only take ConstantExpressions that hold tuples or lists as parameters."))
        self.assertRaisesEx(ValueError, UnaryExpression, node_type, b, exc_pattern=re.compile("The CollectionLength unary expression can only take ConstantExpressions that hold tuples or lists as parameters."))

#Negate
    def test_expression_negate_of_a_constant(self):
        a = ConstantExpression(10)
        node_type = UnaryExpression.Negate
        expr = UnaryExpression(node_type, a)

        self.assertEquals(expr.node_type, node_type)
        self.assertEquals(expr.rhs, a)

    def test_expression_negate_of_a_constant_representation(self):
        a = ConstantExpression(10)
        node_type = UnaryExpression.Negate
        expr = UnaryExpression(node_type, a)
        
        self.assertEquals("negate(10)", str(expr))

    def test_nested_negate_expression(self):
        a = ConstantExpression(10)
        node_type = UnaryExpression.Negate

        expr = UnaryExpression(node_type, UnaryExpression(node_type, a))

        self.assertEquals(expr.node_type, node_type)
        self.failUnless(isinstance(expr.rhs, UnaryExpression), "The right-hand side of the unary expression should be an unary expression as well, but is %s" % expr.rhs.__class__)
        self.assertEquals(expr.rhs.node_type, node_type)
        self.assertEquals(expr.rhs.rhs, a)
    
    def test_nested_negate_expression_representation(self):
        a = ConstantExpression(10)
        node_type = UnaryExpression.Negate

        expr = UnaryExpression(node_type, UnaryExpression(node_type, a))

        self.assertEquals("negate(negate(10))", str(expr))

if __name__ == '__main__':
    unittest.main()
