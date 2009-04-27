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
import re
from os.path import dirname, abspath, join
root_path = abspath(join(dirname(__file__), "../../"))
sys.path.insert(0, root_path)

from pynq.expressions import GetAttributeExpression
from base import BaseUnitTest

class TestGetAttributeExpression(BaseUnitTest):

    def test_get_attribute_expression_validates_against_empty_attributes(self):
        self.assertRaisesEx(ValueError, GetAttributeExpression, exc_pattern=re.compile("In order to create a new attribute expression you need to provide some attributes."))

    def test_get_attribute_expression_keeps_track_of_attributes(self):
        expression = GetAttributeExpression("some","expression")
        assert len(expression.attributes) == 2, "Length of attributes property should be 2 but was %d" % len(expression.attributes)
        assert expression.attributes[0] == "some"
        assert expression.attributes[1] == "expression"
    
    def test_nested_get_attribute_expressions_work_together(self):
        expression = GetAttributeExpression(GetAttributeExpression("some","weird"), "expression")
        assert len(expression.attributes) == 3
        assert expression.attributes[0] == "some"
        assert expression.attributes[1] == "weird"
        assert expression.attributes[2] == "expression"
    
if __name__ == '__main__':
    unittest.main()
