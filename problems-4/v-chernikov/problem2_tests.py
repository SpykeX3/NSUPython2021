#!/usr/bin/env python3

import unittest
import problem2 as p


class Problem2Test(unittest.TestCase):
    def test_create_table(self):
        self.assertEqual(p.create_translation_table("abc", "xyz"), {"a": "x", "b": "y", "c": "z"})

    def test_duplicate_mapping(self):
        self.assertRaises(ValueError, lambda: p.create_translation_table("aba", "xyz"))

    def test_translation(self):
        table = p.create_translation_table("abc", "xyz")
        original = "abcdefg !@# aa bb cc xyz"
        expected = "xyzdefg !@# xx yy zz xyz"
        self.assertEqual(p.translate(table, set(), original), expected)

    def test_deleting(self):
        table = p.create_translation_table("abc", "xyz")
        original = "abcdefg !@# aa bb cc xyz"
        expected = "yzde !@#  yy zz xyz"
        self.assertEqual(p.translate(table, set("afg"), original), expected)


if __name__ == '__main__':
    unittest.main()
