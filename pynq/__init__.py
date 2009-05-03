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

import sys
from os.path import dirname, abspath, join
root_path = abspath(join(dirname(__file__), "../../"))
sys.path.insert(0, root_path)

from pynq.providers import CollectionProvider
from pynq.parser import ExpressionParser
from pynq.guard import Guard

def From(provider):
    return Query(provider)

class Query(object):
    def __init__(self, provider):
        error_message = "The provider cannot be None. If you meant to use the CollectionProvider pass in a tuple or list"
        Guard.against_none(provider, error_message)
        if isinstance(provider, (list, tuple)):
            self.provider = CollectionProvider(provider)
        else:
            self.provider = provider
        self.expressions = [] 
        self.order_expressions = []
        self.parser = ExpressionParser()
      
    def where(self, clause):
        self.expressions.append(self.parser.parse(clause.strip()))
        return self
    
    def order_by(self, *args):
        for arg in args:
            self.order_expressions.append(arg)
        return self

    def select(self, *args):
        class DynamicItem(object):
            pass

        fields = list(args)
        
        col = self.provider.parse(self)
        
        items = []
        for item in col:
            new_item = DynamicItem()
            for field in fields:
                setattr(new_item, field, getattr(item, field))
            items.append(new_item)
        
        return items
        
    def select_many(self):
        return self.provider.parse(self)
