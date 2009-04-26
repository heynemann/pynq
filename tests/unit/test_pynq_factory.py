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
from pynq.expressions import Expression, ConstantExpression, BinaryExpression
from base import BaseUnitTest

class TestPynqFactory(BaseUnitTest):

    def __test_where_binary_equals(self):
        col = []
        tree = From(col).where("some.other.property == 'Bernardo'")
        
        assert tree is not None, "The From method needs to return something"
        assert isinstance(tree, Query), "The lambda should have resolved to a LambdaExpression"
        assert len(tree.expressions) == 1, "There should be one where expression"
        assert isinstance(tree.expressions[0], BinaryExpression), "The first expression of the tree should be a BinaryExpression"
        
if __name__ == '__main__':
    unittest.main()
