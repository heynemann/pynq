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
from pynq.expressions import UnaryExpression, ConstantExpression

parser = ExpressionParser()
operations_to_test = {
    UnaryExpression.Negate : (("-1", "1"),),
    UnaryExpression.Not : (("not 1", "1"),),
}

def test_for_null_for_unary_expressions():
    for operation in operations_to_test.keys():
        for combination in operations_to_test[operation]:
            program, rhs = combination
            yield assert_not_null, program, operation, rhs

def test_for_type_of_expression_for_unary_expressions():
    for operation in operations_to_test.keys():
        for combination in operations_to_test[operation]:
            program, rhs = combination
            yield assert_is_binary_expression, program, operation, rhs

def test_for_type_of_expression_for_unary_expressions():
    for operation in operations_to_test.keys():
        for combination in operations_to_test[operation]:
            program, rhs = combination
            yield assert_is_constant_expression_on_both_sides, program, operation, rhs

def test_for_value_for_unary_expressions():
    for operation in operations_to_test.keys():
        for combination in operations_to_test[operation]:
            program, rhs = combination
            yield assert_value, program, operation, rhs

def test_for_node_type_for_unary_expressions():
    for operation in operations_to_test.keys():
        for combination in operations_to_test[operation]:
            program, rhs = combination
            yield assert_node_type, program, operation, rhs

#Asserts
def assert_not_null(program, node_type, rhs):
    tree = parser.parse(program)
    assert tree is not None, "The tree cannot be null after parsing for operation %s" % node_type

def assert_is_unary_expression(program, node_type, rhs):
    tree = parser.parse(program)
    assert isinstance(tree, UnaryExpression), "The tree for this operation (%s) should return a UnaryExpression" % node_type

def assert_is_constant_expression_on_both_sides(program, node_type, rhs):
    tree = parser.parse(program)
    assert isinstance(tree.rhs, ConstantExpression), "The rhs for this operation (%s) should be a ConstantExpression" % node_type

def assert_value(program, node_type, rhs):
    tree = parser.parse(program)
    assert tree.rhs.value == rhs, "The value for the rhs when the operation is %s should be %s and was %s" % (node_type, rhs, tree.rhs.value)

def assert_node_type(program, node_type, rhs):
    tree = parser.parse(program)
    assert tree.node_type == node_type, "The tree node type should be %s and was %s" % (node_type, tree.node_type)

if __name__ == '__main__':
    import nose
    nose.main()
