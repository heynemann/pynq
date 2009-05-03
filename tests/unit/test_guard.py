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

from pynq.guard import Guard
from base import BaseUnitTest

class TestGuard(BaseUnitTest):

    def test_required_list_argument(self):
        class WithRequiredArgument:
            def __init__(self, a):
                Guard.against_empty(a, "Argument a is required")
                pass

        req = WithRequiredArgument(("some tuple",))
        self.assertRaisesEx(ValueError, WithRequiredArgument, tuple([]), exc_pattern=re.compile("Argument a is required"))
        self.assertRaisesEx(ValueError, WithRequiredArgument, [], exc_pattern=re.compile("Argument a is required"))
        self.assertRaisesEx(ValueError, WithRequiredArgument, {}, exc_pattern=re.compile("Argument a is required"))

    def test_required_argument(self):
        class WithRequiredArgument:
            def do(self, a):
                Guard.against_empty(a, "Argument a is required")
                pass

        req = WithRequiredArgument()
        req.do("10")
        self.assertRaisesEx(ValueError, req.do, None, exc_pattern=re.compile("Argument a is required"))
        self.assertRaisesEx(ValueError, req.do, "", exc_pattern=re.compile("Argument a is required"))

    def test_required_argument_with_default_message(self):
        class WithRequiredArgument:
            def do(self, a):
                Guard.against_empty(a)
                pass

        req = WithRequiredArgument()
        req.do("10")
        self.assertRaisesEx(ValueError, req.do, None, exc_pattern=re.compile("One of the arguments is required and was not filled."))
        self.assertRaisesEx(ValueError, req.do, "", exc_pattern=re.compile("One of the arguments is required and was not filled."))

    def test_is_of_type(self):
        class WithTypeArgument:
            def do(self, a):
                Guard.accepts(a, (int, float), "Argument a must be an integer or a float")
                pass
        req = WithTypeArgument()
        req.do(10)
        req.do(10.0)
        self.assertRaisesEx(ValueError, req.do, "a", exc_pattern=re.compile("Argument a must be an integer or a float"))
        self.assertRaisesEx(ValueError, req.do, (10,20), exc_pattern=re.compile("Argument a must be an integer or a float"))

    def test_is_of_type_with_default_message(self):
        class WithTypeArgument:
            def do(self, a):
                Guard.accepts(a, (int, float))
                pass
                
        msg = "One of the arguments should be of types %s and it isn't." % ", ".join((str(int), str(float)))
        req = WithTypeArgument()
        req.do(10)
        req.do(10.0)
        self.assertRaisesEx(ValueError, req.do, "a", exc_pattern=re.compile(msg))
        self.assertRaisesEx(ValueError, req.do, (10,20), exc_pattern=re.compile(msg))
    
    def test_accepts_only_with_message(self):
        items = ["a", "b"]
        items_failing = ["a", "b", 1]
        message = "There should be only strings."
        
        Guard.accepts_only(items, [str], message)
        
        self.assertRaisesEx(ValueError, Guard.accepts_only, items_failing, [str], message, exc_pattern=re.compile(message))

    def test_accepts_only_without_message(self):
        items = ["a", "b"]
        items_failing = ["a", "b", 1]
        message = u"All arguments in the given collection should be of type\(s\) \[str\] and at least one of them isn't."
        
        Guard.accepts_only(items, [str])
        
        self.assertRaisesEx(ValueError, Guard.accepts_only, items_failing, [str], exc_pattern=re.compile(message))
        
if __name__ == '__main__':
    unittest.main()
