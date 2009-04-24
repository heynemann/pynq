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

from pynq.expressions import Expression, ConstantExpression, BinaryExpression
from base import BaseUnitTest

class TestBinaryExpression(BaseUnitTest):

    def test_binary_expression_only_accepts_expressions_for_arguments(self):
        a = 10
        a_expr = ConstantExpression(10)
        b = "20"
        b_expr = ConstantExpression(20)
        node_type = BinaryExpression.Add
        
        self.assertRaisesEx(ValueError, BinaryExpression, node_type, a, b_expr, exc_pattern=re.compile("Lhs must be an expression \(an instance of a class that inherits from pynq.Expression\)"))
        self.assertRaisesEx(ValueError, BinaryExpression, node_type, a_expr, b, exc_pattern=re.compile("Rhs must be an expression \(an instance of a class that inherits from pynq.Expression\)"))
        self.assertRaisesEx(ValueError, BinaryExpression, None, a_expr, b_expr, exc_pattern=re.compile("The BinaryExpression node type is required"))

if __name__ == '__main__':
    unittest.main()
