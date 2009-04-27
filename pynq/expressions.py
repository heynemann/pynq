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

from pynq.guard import Guard

class Expression(object):
    def evaluate(self):
        raise NotImplementedError("The evaluate method needs to be overriden in a base class of Expression.")

class ConstantExpression(Expression):
    def __init__(self, value):
        '''Initializes the ConstantExpression with the specified value.
        Arguments:
            value - Value to initialize the ConstantExpression with.
        '''
        self.value = value

    def evaluate(self):
        '''Returns the value for this constant expression.'''
        return self.value

    def __unicode__(self):
        return unicode("%s" % self.value)
    __str__ = __unicode__

class NameExpression(Expression):
    def __init__(self, name):
        self.name = name

    def __unicode__(self):
        return unicode(self.name)
    __str__ = __unicode__

class GetAttributeExpression(Expression):
    def __init__(self, *args):
        Guard.against_empty(args, "In order to create a new attribute expression you need to provide some attributes.")
        self.attributes = []
        self.add_attributes(args)

    def add_attributes(self, attrs):
        for attr in attrs:
            if isinstance(attr, GetAttributeExpression):
                self.add_attributes(attr.attributes)
            else:
                self.attributes.append(attr)

    def __unicode__(self):
        return unicode(".".join(self.attributes))
    __str__ = __unicode__

class UnaryExpression(Expression):
    #operation types
    CollectionLength = "CollectionLength"
    Negate = "Negate"
    Not = "Not"
    
    #operation representations
    representations = {
                        CollectionLength:"len(%s)",
                        Negate:"negate(%s)",
                        Not:"(not %s)",
                      }
                      
    def __init__(self, node_type, rhs):
        '''Initializes the UnaryExpression with the specified arguments.
        Arguments:
            node_type - Specifies the type of operation that this UnaryExpression represents
            rhs - Right-hand site of the operation. Since this is an unary operation, this is the only argument.
        '''
        Guard.against_empty(node_type, "The UnaryExpression node type is required")
        if node_type == self.CollectionLength:
            Guard.accepts(rhs, (ConstantExpression,), "The CollectionLength unary expression can only take ConstantExpressions that hold tuples or lists as parameters.")
            if not isinstance(rhs.evaluate(), (list, tuple)):
                raise ValueError("The CollectionLength unary expression can only take ConstantExpressions that hold tuples or lists as parameters.")
        self.node_type = node_type
        self.rhs = rhs

    def __str__(self):
        '''Returns a string representing the expression.'''
        return self.representations[self.node_type] % str(self.rhs)
    
class BinaryExpression(Expression):
    #operation types
    
    #Arithmetic
    Add = "Add"
    Subtract = "Subtract"
    Multiply = "Multiply"
    Divide = "Divide"
    Power = "Power"
    Modulo = "Modulo"
    
    #Bitwise
    And = "And"
    Or = "Or"
        
    #Comparison Operators
    Equal = "Equal"
    NotEqual = "NotEqual"
    GreaterThan = "GreaterThan"
    GreaterThanOrEqual = "GreaterThanOrEqual"
    LessThan = "LessThan"
    LessThanOrEqual = "LessThanOrEqual"
    
    #operation representations
    representations = {
                        Add:"+",
                        Subtract:"-",
                        Multiply:"*",
                        Divide:"/",
                        Power:"^",
                        Modulo:"%",
                        And:"and",
                        Or: "or",
                        Equal: "==",
                        NotEqual: "!=",
                        GreaterThan: ">",
                        GreaterThanOrEqual: ">=",
                        LessThan: "<",
                        LessThanOrEqual: "<=",
                      }
    
    def __init__(self, node_type, lhs, rhs):
        '''Initializes the BinaryExpression with the specified arguments.
        Arguments:
            node_type - Specifies the type of operation that this BinaryExpression represents
            lhs - Left-hand side of the operation (as in the first argument)
            rhs - Right-hand site of the operation (as in the second argument)
        '''
        Guard.against_empty(node_type, "The BinaryExpression node type is required")
        Guard.accepts(lhs, (Expression,), "Lhs must be an expression (an instance of a class that inherits from pynq.Expression)")
        Guard.accepts(rhs, (Expression,), "Rhs must be an expression (an instance of a class that inherits from pynq.Expression)")
        self.node_type = node_type
        self.lhs = lhs
        self.rhs = rhs

    def __str__(self):
        '''Returns a string representing the expression.'''
        return "(%s %s %s)" % (str(self.lhs), 
                           self.representations[self.node_type], 
                           str(self.rhs))
                           
