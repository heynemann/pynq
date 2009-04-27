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

from base import BaseUnitTest
from pynq.parser import LiteralToken, DotToken
import pynq.parser

class TestExpressionParser(BaseUnitTest):

    def test_dot_token_raises_on_different_tokens(self):
        literal = LiteralToken(None, None, None, "1")
        pynq.parser.token = literal
        token = literal
        dot = DotToken(None, None, None)
        error = u"Each part of a given get attribute expression \(some.variable.value\) needs to be a NameExpression."
        self.assertRaisesEx(ValueError, dot.led, literal, exc_pattern=re.compile(error))
        
if __name__ == '__main__':
    unittest.main()
