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

class TestSelectFieldExpressions(BaseUnitTest):

    def test_select_field_operator_add(self):
        class Item:
            def __init__(self, name, value, value2):
                self.name = name
                self.value = value
                self.value2 = value2

        col = [Item("A", 10, 10), Item("B", 20, 20), Item("C", 30, 30)]
        mod = From(col).select("name", "item.value + item.value2")

        assert mod[0].name == "A"
        assert mod[0].dynamic_1 == 20

        assert mod[1].name == "B"
        assert mod[1].dynamic_1 == 40

        assert mod[2].name == "C"
        assert mod[2].dynamic_1 == 60

    def test_select_many_expressions_at_once(self):
        class Item:
            def __init__(self, name, value, value2):
                self.name = name
                self.value = value
                self.value2 = value2

        col = [Item("A", 10, 20), Item("B", 20, 30), Item("C", 30, 40)]
        mod = From(col).select("name", "item.value2 - item.value", "item.value * item.value2")

        assert mod[0].name == "A"
        assert mod[0].dynamic_1 == 10
        assert mod[0].dynamic_2 == 200

        assert mod[1].name == "B"
        assert mod[1].dynamic_1 == 10
        assert mod[1].dynamic_2 == 600

        assert mod[2].name == "C"
        assert mod[2].dynamic_1 == 10
        assert mod[2].dynamic_2 == 1200
