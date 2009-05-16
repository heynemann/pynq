#!/usr/bin/env python
# -*- coding:utf-8 -*-

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

from pynq import From
from pynq.expressions import NameExpression

class TestGroupBy(unittest.TestCase):

    class TestClass(object):
        def __init__(self, first, second, third):
            self.first = first
            self.second = second
            self.third = third

    def setUp(self):
        self.entity1 = self.TestClass(1, 2, 8)
        self.entity2 = self.TestClass(4, 5, 5)
        self.entity3 = self.TestClass(7, 5, 2)
        
        self.col = [self.entity3, self.entity1, self.entity2]
        
    def test_grouping_adds_right_expression_for_name_expression(self):
        query = From(self.col).group_by("second")
        assert isinstance(query.group_expression, NameExpression)
    
    def test_grouping_returns_two_keys_on_select(self):
        items = From(self.col).group_by("second").select_many()
        assert len(items.keys()) == 2
        
    def test_grouping_returns_the_two_right_keys_on_select(self):
        items = From(self.col).group_by("second").select_many()
        assert items.has_key(2)
        assert items.has_key(5)

    def test_grouping_returns_the_right_length_of_items_on_select(self):
        items = From(self.col).group_by("second").select_many()
        assert len(items[2]) == 1
        assert len(items[5]) == 2

    def test_grouping_returns_the_right_items_on_select(self):
        items = From(self.col).order_by("first").group_by("second").select_many()
        assert items[2][0].first == 1
        assert items[5][0].first == 4
        assert items[5][1].first == 7
      
if __name__ == '__main__':
    unittest.main()
