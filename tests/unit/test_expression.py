#!/usr/bin/env python
#-*- coding:utf-8 -*-
import unittest

import sys
from os.path import dirname, abspath, join
root_path = abspath(join(dirname(__file__), "../../"))
sys.path.insert(0, root_path)

from pynq.expressions import Expression

class TestExpresionBaseClass(unittest.TestCase):

    def test_evaluate_should_raise(self):
        expr = Expression()
        self.assertRaises(NotImplementedError, expr.evaluate)

if __name__ == '__main__':
    unittest.main()
