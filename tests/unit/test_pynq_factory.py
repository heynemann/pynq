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

from pynq import From, Query
from pynq.expressions import Expression, ConstantExpression, BinaryExpression, GetAttributeExpression, NameExpression
from base import BaseUnitTest

class TestPynqFactory(BaseUnitTest):

    def test_where_binary_equals_returns_tree(self):
        col = []
        tree = From(col).where("some.other.property == 'Bernardo'")
        
        assert tree is not None, "The From method needs to return something"
        assert isinstance(tree, Query), "The lambda should have resolved to a LambdaExpression"

    def test_where_binary_equals_returns_binary_expression(self):
        col = []
        tree = From(col).where("some.other.property == 'Bernardo'")        

        assert len(tree.expressions) == 1, "There should be one where expression"
        assert isinstance(tree.expressions[0], BinaryExpression), \
                "The first expression of the tree should be a BinaryExpression"

    def test_where_binary_equals_returns_get_attribute_expression_on_lhs(self):
        col = []
        tree = From(col).where("some.other.property == 'Bernardo'")
        error = "Lhs should be GetAttributeExpression but was %s"
        class_name = tree.expressions[0].__class__.__name__
        assert isinstance(tree.expressions[0].lhs, GetAttributeExpression), \
                            error % class_name

    def test_where_binary_equals_returns_tree_name_expressions_as_attributes_on_lhs(self):
        col = []
        tree = From(col).where("some.other.property == 'Bernardo'")
        error_message = "There should be three attributes "\
                        "('some','other','property') in the GetAttributeExpression, "\
                        "but there was %d"
        assert len(tree.expressions[0].lhs.attributes) == 3, \
                error_message % len(tree.expressions[0].lhs.attributes)
        for i in range(3):
            error = "The %d parameter should be a NameExpression but was %s"
            class_name = tree.expressions[0].lhs.attributes[i].__class__.__name__
            assert isinstance(tree.expressions[0].lhs.attributes[i], NameExpression), \
                                error % (i, class_name)
    
    def test_where_binary_equals_returns_the_proper_node_type(self):
        col = []
        tree = From(col).where("some.other.property == 'Bernardo'")

        assert tree.expressions[0].node_type == BinaryExpression.Equal

    def test_where_binary_equals_returns_a_constant_expression_on_the_rhs(self):
        col = []
        tree = From(col).where("some.other.property == 'Bernardo'")

        assert isinstance(tree.expressions[0].rhs, ConstantExpression)

    def test_where_binary_equals_returns_the_right_value_on_the_rhs(self):
        col = []
        tree = From(col).where("some.other.property == 'Bernardo'")

        assert tree.expressions[0].rhs.value == "Bernardo"
        
if __name__ == '__main__':
    unittest.main()
