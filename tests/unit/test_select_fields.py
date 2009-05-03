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
import datetime
import re
import sys
from os.path import dirname, abspath, join
root_path = abspath(join(dirname(__file__), "../../"))
sys.path.insert(0, root_path)

from pynq import From
from base import BaseUnitTest

class TestSelectFields(BaseUnitTest):

    class TestClass(object):
        def __init__(self, first, second, third):
            self.first = first
            self.second = second
            self.third = third

    def setUp(self):
        self.entity1 = self.TestClass(1, 2, 3)
        self.entity2 = self.TestClass(4, 5, 6)
        self.entity3 = self.TestClass(7, 8, 9)
        
        self.col = [self.entity1, self.entity2, self.entity3]

    def test_select_returns_something(self):
        filtered = From(self.col).select("first","second")
        assert filtered is not None    

    def test_select_returns_three_elements(self):
        filtered = From(self.col).select("first","second")
        assert len(filtered) == 3, "There should be three items in the filtered collection."

    def test_select_returns_dynamic_items(self):
        filtered = From(self.col).select("first","second")
        for i in range(3):
            assert filtered[i].__class__.__name__ == "DynamicItem"

    def test_select_returns_proper_values(self):
        filtered = From(self.col).select("first","second")
        for i in range(3):
            assert filtered[i].first == i * 3 + 1
            assert filtered[i].second == i * 3 + 2

    def test_select_returns_class_without_third_attribute(self):
        filtered = From(self.col).select("first","second")
        for i in range(3):
            assert not hasattr(filtered[i], "third")
    
    def test_selecting_twice_returns_different_objects(self):
        filtered = From(self.col).select("first","second")
        filtered2 = From(self.col).select("first")
        
        for i in range(3):
            assert not hasattr(filtered2[i], "second")
            assert not hasattr(filtered2[i], "third")

    def test_selecting_no_fields_raises_value_error(self):
        fr = From(self.col)
        msg = re.compile("Selecting with no fields is not valid. " \
                         "When using From\(provider\).select method, " \
                         "please provide a list of expressions or strings as fields.")
        self.assertRaisesEx(ValueError, fr.select, None, exc_pattern=msg)
        self.assertRaisesEx(ValueError, fr.select, exc_pattern=msg)
        self.assertRaisesEx(ValueError, fr.select, [], exc_pattern=msg)
        self.assertRaisesEx(ValueError, fr.select, tuple([]), exc_pattern=msg)
 
    def test_selecting_with_invalid_type_raises_value_error(self):
        fr = From(self.col)  
        msg = re.compile("Selecting with invalid type. " \
                         "When using From\(provider\).select method, " \
                         "please provide a list of expressions or strings as fields.")
        self.assertRaisesEx(ValueError, fr.select, 1, exc_pattern=msg)
        self.assertRaisesEx(ValueError, fr.select, datetime.datetime.now(), exc_pattern=msg)

if __name__ == '__main__':
    unittest.main()
