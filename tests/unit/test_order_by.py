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

class TestOrderBy(unittest.TestCase):

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

    def test_adding_order_adds_to_query(self):
        query = From([]).order_by("some")
        assert len(query.order_expressions) == 1

    def test_adding_order_keeps_the_right_value_in_query(self):
        query = From([]).order_by("some")
        assert query.order_expressions[0] == "some"

    def test_ordering_by_first_field_asc(self):
        result = From(self.col).order_by("first").select_many()
        assert result[0].first == 1
        assert result[1].first == 4
        assert result[2].first == 7

    def test_ordering_by_two_fields(self):
        result = From(self.col).order_by("second", "third").select_many()
        assert result[0].first == 1
        assert result[1].first == 7
        assert result[2].first == 4

    def test_desc_order(self):
        result = From(self.col).order_by("-first").select_many()
        assert result[0].first == 7
        assert result[1].first == 4
        assert result[2].first == 1

    def test_desc_order_for_many_fields(self):
        result = From(self.col).order_by("-second", "-third").select_many()
        assert result[0].first == 4
        assert result[1].first == 7
        assert result[2].first == 1

if __name__ == '__main__':
    unittest.main()
