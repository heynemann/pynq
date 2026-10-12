# Licensed under the Open Software License (OSL) v. 3.0.
# See http://www.opensource.org/licenses/osl-3.0.php.

"""Regression tests for computed and nested grouping keys."""
import unittest

from pynq import From


class Record(object):
    def __init__(self, value, category=None):
        self.value = value
        self.category = category


class TestGroupByExpressions(unittest.TestCase):
    def test_group_by_arithmetic_expression(self):
        items = [Record(1), Record(2), Record(3)]
        grouped = From(items).group_by("item.value % 2").select_many()
        self.assertEqual(grouped, {1: [items[0], items[2]], 0: [items[1]]})

    def test_group_by_nested_attribute(self):
        items = [Record(1, Record("a")), Record(2, Record("b")),
                 Record(3, Record("a"))]
        grouped = From(items).group_by("item.category.value").select_many()
        self.assertEqual(grouped, {"a": [items[0], items[2]], "b": [items[1]]})

    def test_group_by_expression_after_projection(self):
        grouped = From([Record(1), Record(2), Record(3)]).group_by(
            "item.value % 2").select("value")
        self.assertEqual([item.value for item in grouped[1]], [1, 3])
        self.assertEqual([item.value for item in grouped[0]], [2])

    def test_group_by_expression_on_empty_collection(self):
        self.assertEqual(From([]).group_by("item.value % 2").select_many(), {})


if __name__ == "__main__":
    unittest.main()
