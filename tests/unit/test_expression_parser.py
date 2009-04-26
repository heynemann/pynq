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

parser = ExpressionParser()
operations_to_test = {
    BinaryExpression.Add : (("1+2", "1", "2"), ("1 + 2", "1", "2")),
    BinaryExpression.Subtract : (("1-2", "1", "2"), ("1 - 2", "1", "2")),
    BinaryExpression.Multiply : (("1*2", "1", "2"), ("1 * 2", "1", "2")),
    BinaryExpression.Divide : (("1/2", "1", "2"), ("1 / 2", "1", "2")),
    BinaryExpression.Power : (("1**2", "1", "2"), ("1 ** 2", "1", "2")),
    BinaryExpression.Modulo : (("1%2", "1", "2"), ("1 % 2", "1", "2")),
}

def test_for_null():
    for operation in operations_to_test.keys():
        for combination in operations_to_test[operation]:
            program, lhs, rhs = combination
            yield assert_not_null, program, operation, lhs, rhs

def test_for_type_of_expression():
    for operation in operations_to_test.keys():
        for combination in operations_to_test[operation]:
            program, lhs, rhs = combination
            yield assert_is_binary_expression, program, operation, lhs, rhs

def test_for_type_of_expression():
    for operation in operations_to_test.keys():
        for combination in operations_to_test[operation]:
            program, lhs, rhs = combination
            yield assert_is_constant_expression_on_both_sides, program, operation, lhs, rhs

def test_for_values():
    for operation in operations_to_test.keys():
        for combination in operations_to_test[operation]:
            program, lhs, rhs = combination
            yield assert_values_on_both_sides, program, operation, lhs, rhs

def test_for_node_type():
    for operation in operations_to_test.keys():
        for combination in operations_to_test[operation]:
            program, lhs, rhs = combination
            yield assert_node_type, program, operation, lhs, rhs

#Asserts
def assert_not_null(program, node_type, lhs, rhs):
    tree = parser.parse(program)
    assert tree is not None, "The tree cannot be null after parsing for operation %s" % node_type

def assert_is_binary_expression(program, node_type, lhs, rhs):
    tree = parser.parse(program)
    assert isinstance(tree, BinaryExpression), "The tree for this operation (%s) should return a BinaryExpression" % node_type

def assert_is_constant_expression_on_both_sides(program, node_type, lhs, rhs):
    tree = parser.parse(program)
    assert isinstance(tree.lhs, ConstantExpression), "The lhs for this operation (%s) should be a ConstantExpression" % node_type
    assert isinstance(tree.rhs, ConstantExpression), "The rhs for this operation (%s) should be a ConstantExpression" % node_type

def assert_values_on_both_sides(program, node_type, lhs, rhs):
    tree = parser.parse(program)
    assert tree.lhs.value == lhs, "The value for the lhs when the operation is %s should be %s and was %s" % (node_type, lhs, tree.lhs.value)
    assert tree.rhs.value == rhs, "The value for the lhs when the operation is %s should be %s and was %s" % (node_type, rhs, tree.rhs.value)

def assert_node_type(program, node_type, lhs, rhs):
    tree = parser.parse(program)
    assert tree.node_type == node_type, "The tree node type should be %s and was %s" % (node_type, tree.node_type)

if __name__ == '__main__':
    import nose
    nose.main()
