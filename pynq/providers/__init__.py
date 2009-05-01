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

import pynq.providers

class IPynqProvider(object):
    def parse(self, query):
        pass

class CollectionProvider(IPynqProvider):
    def __init__(self, collection):
        self.collection = collection

    def compare_items(self, a, b):
        expression = None
        for order_expression in self.order_expressions:
            if order_expression.startswith("-"):
                field = order_expression[1:]
                result = cmp(-getattr(a, field), -getattr(b, field))
            else:
                result = cmp(getattr(a, order_expression), getattr(b, order_expression))

            expression = expression is None and result or (expression or result)

        return expression

    def parse(self, query):
        processed_collection = list(self.collection)
        for expression in query.expressions:
            klass = getattr(pynq.providers, expression.__class__.__name__ + "Processor")
            processed_collection = klass.process(processed_collection, expression)

        if query.order_expressions:
            self.order_expressions = query.order_expressions
            processed_collection.sort(self.compare_items)

        return processed_collection

class BinaryExpressionProcessor(object):
    @classmethod
    def process(cls, collection, expression):
        filters = str(expression)
        return [item for item in collection if eval(filters)]
