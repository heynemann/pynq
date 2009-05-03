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
from pynq.providers import CollectionProvider
from base import BaseUnitTest

class TestPynqFactory(BaseUnitTest):

    def __test_from_returns_query(self):
        query = From([])
        assert isinstance(query, Query)
    
    def __test_from_with_empty_provider_raises(self):
        error = "The provider cannot be None. If you meant to use the CollectionProvider pass in a tuple or list"
        self.assertRaisesEx(ValueError, From, None, exc_pattern=re.compile(error))        
    
    def __test_passing_tuple_returns_collection_provider(self):
        query = From(tuple([]))
        assert isinstance(query.provider, CollectionProvider)
        
    def __test_passing_list_returns_collection_provider(self):
        query = From([])
        assert isinstance(query.provider, CollectionProvider)
    
    def __test_specifying_provider_keeps_provider_in_the_tree(self):
        query = From("provider")
        assert query.provider == "provider"
        
    def __test_where_binary_equals_returns_tree(self):
        col = []
        tree = From(col).where("some.other.property == 'Bernardo'")
        
        assert tree is not None, "The From method needs to return something"
        assert isinstance(tree, Query), "The lambda should have resolved to a LambdaExpression"

    def __test_where_binary_equals_returns_binary_expression(self):
        col = []
        tree = From(col).where("some.other.property == 'Bernardo'")        

        assert len(tree.expressions) == 1, "There should be one where expression"
        assert isinstance(tree.expressions[0], BinaryExpression), \
                "The first expression of the tree should be a BinaryExpression"

    def __test_where_binary_equals_returns_get_attribute_expression_on_lhs(self):
        col = []
        tree = From(col).where("some.other.property == 'Bernardo'")
        error = "Lhs should be GetAttributeExpression but was %s"
        class_name = tree.expressions[0].__class__.__name__
        assert isinstance(tree.expressions[0].lhs, GetAttributeExpression), \
                            error % class_name

    def __test_where_binary_equals_returns_tree_name_expressions_as_attributes_on_lhs(self):
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
    
    def __test_where_binary_equals_returns_the_proper_node_type(self):
        col = []
        tree = From(col).where("some.other.property == 'Bernardo'")

        assert tree.expressions[0].node_type == BinaryExpression.Equal

    def __test_where_binary_equals_returns_a_constant_expression_on_the_rhs(self):
        col = []
        tree = From(col).where("some.other.property == 'Bernardo'")

        assert isinstance(tree.expressions[0].rhs, ConstantExpression)

    def __test_where_binary_equals_returns_the_right_value_on_the_rhs(self):
        col = []
        tree = From(col).where("some.other.property == 'Bernardo'")

        assert tree.expressions[0].rhs.value == "'Bernardo'"
        
    def __test_select_many_returns_proper_results_for_numbers(self):
        items = From([1,2,3,4,5]).where("item > 2 and item < 4").select_many()
        assert items == [3], "Only item 3 should be in the resulting collection but it was %s." % ",".join(items)

    def __test_select_many_returns_proper_results_for_sub_property(self):
        class SomeElement(object):
            def __init__(self, value):
                self.value = value
            def __str__(self):
                return str(self.value)
        
        col = [SomeElement(1), SomeElement(2), SomeElement(3), SomeElement(4), SomeElement(5)]
        
        items = From(col).where("item.value > 2 and item.value < 4").select_many()
        
        assert len(items) == 1, "Only item 3 should be in the resulting collection, but it has length of %d" % len(items)
        assert items[0].value == 3, "Only item 3 should be in the resulting collection but it was %s." % items[0].value

    class TwoValues(object):
        def __init__(self, value, value2):
            self.value = value
            self.value2 = value2

    def __test_where_add_returns_proper_results(self):
        
        col = [self.TwoValues(1, 2), self.TwoValues(2, 3), self.TwoValues(3, 4), self.TwoValues(4, 5), self.TwoValues(5, 6)]
        
        items = From(col).where("item.value + item.value2 > 8").select_many()
        
        assert len(items) == 2, "Only items 4 and 5 should be in the resulting collection, but it has length of %d" % len(items)
        assert items[0].value == 4, "Item 4 should be in the resulting collection but it was %s." % items[0].value
        assert items[1].value == 5, "Item 5 should be in the resulting collection but it was %s." % items[1].value

    def test_where_power_returns_proper_results(self):
        col = [self.TwoValues(1, 2), self.TwoValues(2, 3), self.TwoValues(3, 4), self.TwoValues(4, 5), self.TwoValues(5, 6)]
        
        items = From(col).where("item.value ** item.value2 > 90").select_many()
        
        assert len(items) == 2, "Only items 4 and 5 should be in the resulting collection, but it has length of %d" % len(items)
        assert items[0].value == 4, "Item 4 should be in the resulting collection but it was %s." % items[0].value
        assert items[1].value == 5, "Item 5 should be in the resulting collection but it was %s." % items[1].value

    def test_where_not_returns_proper_results(self):
        col = [self.TwoValues(1, 2), self.TwoValues(2, 3), self.TwoValues(3, 4), self.TwoValues(4, 5), self.TwoValues(5, 6)]
        
        items = From(col).where("not (item.value < 4)").select_many()
        
        assert len(items) == 2, "Only items 4 and 5 should be in the resulting collection, but it has length of %d" % len(items)
        assert items[0].value == 4, "Item 4 should be in the resulting collection but it was %s." % items[0].value
        assert items[1].value == 5, "Item 5 should be in the resulting collection but it was %s." % items[1].value        
    
    def test_where_or_returns_proper_results(self):
        col = [self.TwoValues(1, 2), self.TwoValues(2, 3), self.TwoValues(3, 4), self.TwoValues(4, 5), self.TwoValues(5, 6)]
        
        items = From(col).where("item.value == 4 or item.value == 5").select_many()
        
        assert len(items) == 2, "Only items 4 and 5 should be in the resulting collection, but it has length of %d" % len(items)
        assert items[0].value == 4, "Item 4 should be in the resulting collection but it was %s." % items[0].value
        assert items[1].value == 5, "Item 5 should be in the resulting collection but it was %s." % items[1].value
        
    def test_where_and_returns_proper_results(self):
        col = [self.TwoValues(1, 2), self.TwoValues(2, 3), self.TwoValues(3, 4), self.TwoValues(4, 5), self.TwoValues(5, 6)]
        
        items = From(col).where("item.value > 2 and item.value2 < 6 ").select_many()
        
        assert len(items) == 2, "Only items 3 and 4 should be in the resulting collection, but it has length of %d" % len(items)
        assert items[0].value == 3, "Item 3 should be in the resulting collection but it was %s." % items[0].value
        assert items[1].value == 4, "Item 4 should be in the resulting collection but it was %s." % items[1].value

if __name__ == '__main__':
    unittest.main()
