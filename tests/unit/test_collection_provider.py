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
        
if __name__ == '__main__':
    unittest.main()
