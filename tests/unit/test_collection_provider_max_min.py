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

from pynq import From

class TestPynqFactoryMaxMin(unittest.TestCase):

    def test_returns_right_max_for_full_collection(self):
        greater = From([1,2,3]).max()
        assert greater == 3, "greater should be 3 but was %s" % greater
        
    def test_returns_right_max_for_filtered_collection(self):
        greater = From([1,2,3]).where("item <= 2").max()
        assert greater == 2, "greater should be 2 but was %s" % greater
        
    def test_returns_right_min_for_full_collection(self):
        lesser = From([1,2,3]).min()
        assert lesser == 1, "lesser should be 1 but was %s" % lesser
        
    def test_returns_right_max_for_filtered_collection(self):
        lesser = From([1,2,3]).where("item >= 2").min()
        assert lesser == 2, "lesser should be 2 but was %s" % lesser
    
if __name__ == '__main__':
    unittest.main()
