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

import operator
import sys
from os.path import dirname, abspath, join
root_path = abspath(join(dirname(__file__), "../../"))
sys.path.insert(0, root_path)

from pynq.enums import Actions
from pynq.guard import Guard
from pynq.expressions import NameExpression

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

    def parse(self, query, action, **kwargs):
        if action == Actions.SelectMany:
            return self.parse_select_many(query)
        elif action == Actions.Select:
            return self.parse_select(query, kwargs["cols"])
        elif action == Actions.Count:
            return self.parse_count(query)
        elif action == Actions.Max:
            return self.parse_max(query, kwargs["column"])
        elif action == Actions.Min:
            return self.parse_min(query, kwargs["column"])
        elif action == Actions.Sum:
            return self.parse_sum(query, kwargs["column"])
        elif action == Actions.Avg:
            return self.parse_avg(query, kwargs["column"])
        else:
            raise ValueError("Invalid action exception. %s is unknown." % action)
        
    def parse_select_many(self, query):
        processed_collection = list(self.collection)
        for expression in query.expressions:
            klass = BinaryExpressionProcessor()
            processed_collection = klass.process(processed_collection, expression)

        if query.order_expressions:
            self.order_expressions = query.order_expressions
            processed_collection.sort(self.compare_items)

        return processed_collection
    
    def parse_select(self, query, cols):
        columns = [query.parser.parse(col) for col in cols]
        return self.transform_collection(self.parse_select_many(query), columns)
    
    def parse_count(self, query):
        return len(self.parse_select_many(query))

    def parse_max(self, query, column):
        return self.__perform_operation_on_all(query, column, lambda items: max(items), "max")

    def parse_min(self, query, column):
        return self.__perform_operation_on_all(query, column, lambda items: min(items), "min")

    def parse_sum(self, query, column):
        return self.__perform_operation_on_all(query, column, lambda items: sum(items), "sum")

    def __perform_operation_on_all(self, query, column, operation, command_name):
        seq = self.parse_select_many(query)

        if len(seq) == 0:
            return 0

        error_message = "The attribute '%s' was not found in the specified collection's items. If you meant to use the raw value of each item in the collection just use the word 'item' as a parameter to .%s or use .%s()" % (column, command_name, command_name)

        Guard.against_empty(column, error_message)

        attribute = column.replace("item.","")
        if "item." in column:
            try:
                seq = [self.rec_getattr(item, attribute) for item in seq]
            except AttributeError:
                raise ValueError(error_message)
        else:
            if attribute.lower() != "item":
                raise ValueError(error_message)

        return operation(seq)

    def parse_avg(self, query, column):
        seq = self.parse_select_many(query)

        if len(seq) == 0:
            return 0

        error_message = "The attribute '%s' was not found in the specified collection's items. If you meant to use the raw value of each item in the collection just use the word 'item' as a parameter to .avg or use .avg()" % column

        Guard.against_empty(column, error_message)

        attribute = column.replace("item.","")

        if "item." in column:
            try:
                seq = [self.rec_getattr(item, attribute) for item in seq]
            except AttributeError:
                raise ValueError(error_message)
        else:
            if attribute.lower() != "item":
                raise ValueError(error_message)
            
        return reduce(operator.add,seq)/len(seq)
       
    def rec_getattr(self, obj, attr):
        return reduce(getattr, attr.split('.'), obj)

    def transform_collection(self, col, cols):
        dynamic_item = type('DynamicItem', (object,), {})

        items = []
        app = items.append
        for item in col:
            field_count = 0
            new_item = dynamic_item()
            for field in cols:
                if isinstance(field, NameExpression):
                    field_name = field.name
                    setattr(new_item, field_name, getattr(item, field_name))
                else:
                    setattr(new_item, "dynamic_%d" % field_count, eval(str(field)))
                field_count += 1
            app(new_item)

        return items

class BinaryExpressionProcessor(object):
    @classmethod
    def process(cls, collection, expression):
        filters = str(expression)
        return [item for item in collection if eval(filters)]
