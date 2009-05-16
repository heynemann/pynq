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

import sys
from os.path import dirname, abspath, join
root_path = abspath(join(dirname(__file__), "../../"))
sys.path.insert(0, root_path)

import unittest

from pynq.providers.partition_algorithm import EquivalenceClassSetPartition

class TestEquivalenceClassesAlgorithm(unittest.TestCase):

    def test_algorithm_returns_a_dictionary(self):
        partitioned = EquivalenceClassSetPartition.partition([1], lambda item: item)
        assert isinstance(partitioned, dict)
    
    def test_algorithm_returns_proper_equivalence_class(self):
        col = [10]
        r = lambda item: item * item
        
        partitioned = EquivalenceClassSetPartition.partition(col, r)
        
        assert partitioned.has_key(100)
    
    def test_algorithm_returns_a_list_for_given_equivalence_class(self):
        col = [10]
        r = lambda item: item * item
        
        partitioned = EquivalenceClassSetPartition.partition(col, r)
        
        assert isinstance(partitioned[100], list)
    
    def test_algorithm_returns_proper_number_of_items_for_given_equivalence_class(self):
        col = [10]
        r = lambda item: item * item
        
        partitioned = EquivalenceClassSetPartition.partition(col, r)
        
        assert len(partitioned[100]) == 1
    
    def test_algorithm_returns_the_item_in_the_list_for_given_equivalence_class(self):
        col = [10]
        r = lambda item: item * item
        
        partitioned = EquivalenceClassSetPartition.partition(col, r)
        
        assert partitioned[100][0] == 10
    
    def test_algorithm_returns_proper_sets_for_multiple_values(self):
        col = [1,2,3,4,5]
        r = lambda item: item % 2 == 0 and "even" or "odd"
        
        partitioned = EquivalenceClassSetPartition.partition(col, r)
        
        assert len(partitioned["even"]) == 2
        assert len(partitioned["odd"]) == 3
        
        assert partitioned["even"][0] == 2
        assert partitioned["even"][1] == 4
        assert partitioned["odd"][0] == 1
        assert partitioned["odd"][1] == 3
        assert partitioned["odd"][2] == 5
        
if __name__ == '__main__':
    unittest.main()
