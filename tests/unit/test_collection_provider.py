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

from pynq.providers import CollectionProvider
from pynq import From

class TestCollectionProvider(unittest.TestCase):

    def test_collection_provider_parses_query_and_returns_list(self):
        col = ["a", "b"]
        query = From(col).where("item == 'a'")
        provider = query.provider
        assert isinstance(provider.parse(query), list)
        
    def test_collection_provider_filters_using_binary_expression(self):
        col = ["a","b"]
        query = From(col).where("item == 'a'")
        provider = query.provider
        result = provider.parse(query)
        assert result == ['a'], "The collection was not filtered properly and now is: %s" % result

    def test_collection_provider_filters_using_binary_expression_for_numbers(self):
        col = [1, 2, 10, 11, 12]
        query = From(col).where("item > 10")
        provider = query.provider
        result = provider.parse(query)
        assert result == [11, 12], "The collection was not filtered properly and now is: %s" % result

    def test_collection_provider_parses_query_using_lesser_than(self):
        col = range(5)
        query = From(col).where("item <= 3")
        provider = query.provider
        result = provider.parse(query)
        assert result == range(4), "The collection was not filtered properly and now is: %s" % result

if __name__ == '__main__':
    unittest.main()
