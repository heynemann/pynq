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
import re

from pynq import From
from base import BaseUnitTest

class TestPynqFactorySumAvg(BaseUnitTest):

    def test_returns_right_sum_for_full_collection(self):
        total = From([1,2,3]).sum()
        assert total == 6, "greater should be 6 but was %s" % total
                
    def test_returns_right_sum_for_filtered_collection(self):
        total = From([1,2,3]).where("item <= 2").sum()
        assert total == 3, "total should be 3 but was %s" % total

    def test_avg_returns_right_amount_for_full_collection_with_no_keyword(self):
        total = From([1,2,3]).avg()
        assert total == 2, "total should be 2 but was %s" % total

    def test_returns_right_amount_for_filtered_collection_with_no_keyword(self):
        total = From([1,2,3,4]).where("item >= 2").avg()
        assert total == 3, "total should be 3 but was %s" % total

    def test_avg_returns_right_amount_for_full_collection(self):
        total = From([1,2,3]).avg("item")
        assert total == 2, "total should be 2 but was %s" % total

    def test_returns_right_amount_for_filtered_collection(self):
        total = From([1,2,3,4]).where("item >= 2").avg("item")
        assert total == 3, "total should be 3 but was %s" % total
        
    def test_returns_right_amount_for_a_given_property(self):
        class OneValue(object):
            def __init__(self, value):
                self.value = value
        total = From([OneValue(1), OneValue(2), OneValue(3)]).avg("item.value")

    def test_returns_right_amount_for_a_given_sub_property(self):
        class OtherValue(object):
            def __init__(self, value):
                self.value = value
                
        class OneValue(object):
            def __init__(self, value):
                self.value = OtherValue(value)
                
        total = From([OneValue(1), OneValue(2), OneValue(3)]).avg("item.value.value")

    def test_raises_for_an_invalid_property(self):
        error_message = "The attribute '%s' was not found in the specified collection's items. If you meant to use the raw value of each item in the collection just use the word 'item' as a parameter to .avg or use .avg()"
        
        class OneValue(object):
            def __init__(self, value):
                self.value = value
        fr = From([OneValue(1), OneValue(2), OneValue(3)])
        self.assertRaisesEx(ValueError, fr.avg, "value", exc_pattern=re.compile(error_message % "value"))
        self.assertRaisesEx(ValueError, fr.avg, "item.dumb", exc_pattern=re.compile(error_message % "item.dumb"))
        self.assertRaisesEx(ValueError, fr.avg, "", exc_pattern=re.compile(error_message % ""))
        self.assertRaisesEx(ValueError, fr.avg, None, exc_pattern=re.compile(error_message % "None"))
        
if __name__ == '__main__':
    unittest.main()
