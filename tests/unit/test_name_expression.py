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

from pynq.expressions import NameExpression

class TestNameExpression(unittest.TestCase):

    def test_name_expression(self):
        expression = NameExpression("somename")
        assert expression.name == "somename", "The name of the" \
                                               " variable in this expression should be" \
                                               " 'somename' but was %s" % expression.name
    
if __name__ == '__main__':
    unittest.main()
