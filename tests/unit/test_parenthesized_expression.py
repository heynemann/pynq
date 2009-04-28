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
import sys
from os.path import dirname, abspath, join
root_path = abspath(join(dirname(__file__), "../../"))
sys.path.insert(0, root_path)

from pynq.parser import ExpressionParser
from pynq.expressions import BinaryExpression, ConstantExpression

class TestParenthesizedExpression(unittest.TestCase):

    def test_basic_parenthesized_expression_returns_something(self):
        expression = "1 + (2 + 3)"
        parser = ExpressionParser()
        tree = parser.parse(expression)
        assert tree is not None, "The tree cannot be null after parsing"

    def test_basic_parenthesized_expression_returns_binary_expression(self):
        expression = "1 + (2 + 3)"
        parser = ExpressionParser()
        tree = parser.parse(expression)
        assert isinstance(tree, BinaryExpression), "The tree needs to be a binary expression"

    def test_basic_parenthesized_expression_returns_constant_expression_in_lhs(self):
        expression = "1 + (2 + 3)"
        parser = ExpressionParser()
        tree = parser.parse(expression)
        assert tree.lhs is not None, "The lhs for the tree cannot be null"
        assert isinstance(tree.lhs, ConstantExpression), "The lhs should be a constant expression"

    def test_basic_parenthesized_expression_returns_proper_value_in_lhs(self):
        expression = "1 + (2 + 3)"
        parser = ExpressionParser()
        tree = parser.parse(expression)
        assert tree.lhs.value == "1", "The lhs should contain the '1' value"

    def test_basic_parenthesized_expression_returns_binary_expression_in_rhs(self):
        expression = "1 + (2 + 3)"
        parser = ExpressionParser()
        tree = parser.parse(expression)
        assert isinstance(tree.rhs, BinaryExpression), "The rhs should be a BinaryExpression"

    def test_basic_parenthesized_expression_returns_not_null_expressions_inside_rhs(self):
        expression = "1 + (2 + 3)"
        parser = ExpressionParser()
        tree = parser.parse(expression)
        assert tree.rhs.lhs is not None, "The lhs of the rhs cannot be null"        
        assert tree.rhs.rhs is not None, "The rhs of the rhs cannot be null"

    def test_basic_parenthesized_expression_returns_constant_expressions_inside_rhs(self):
        expression = "1 + (2 + 3)"
        parser = ExpressionParser()
        tree = parser.parse(expression)
        assert isinstance(tree.rhs.lhs, ConstantExpression), "The lhs of the rhs should be a ConstantExpression"        
        assert isinstance(tree.rhs.rhs, ConstantExpression), "The rhs of the rhs should be a ConstantExpression"        

    def test_basic_parenthesized_expression_returns_proper_values_inside_rhs(self):
        expression = "1 + (2 + 3)"
        parser = ExpressionParser()
        tree = parser.parse(expression)
        assert tree.rhs.lhs.value == "2", "The lhs of the rhs should be 2 but was %s" % tree.rhs.lhs.value
        assert tree.rhs.rhs.value == "3", "The rhs of the rhs should be 3 but was %s" % tree.rhs.rhs.value

    def test_advanced_parenthesized_expression(self):
        expression = "(1 + 2 + 3) + ((2+3) + 1)"
        parser = ExpressionParser()
        tree = parser.parse(expression)

        assert str(tree) == "(((1 + 2) + 3) + ((2 + 3) + 1))", "The expression was not parsed correctly"
    
    def test_advanced_parenthesized_expression(self):
        expression = "(1 + (2 + 3)) + ((2+3) + 1)"
        parser = ExpressionParser()
        tree = parser.parse(expression)
        
        expected = "((1 + (2 + 3)) + ((2 + 3) + 1))"
        assert str(tree) == expected, "The expression was not parsed correctly. Expecting %s, Found %s" % (expected, str(tree))
    
if __name__ == '__main__':
    unittest.main()
