#!/usr/bin/env python3

import unittest
from problem2 import cut_off


class MyTestCase(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(cut_off(0, 1, []), [])

    def test_nochange(self):
        self.assertEqual(cut_off(-10, 10, [-10, 10, 5, -2]), [-10, 10, 5, -2])

    def test_change(self):
        self.assertEqual(cut_off(-10, 10, [-11, 17, 5, -2, 999]), [-10, 10, 5, -2, 10])

    def test_error(self):
        with self.assertRaises(Exception) as context:
            cut_off(10, -10, [-11, 17, 5, -2, 999])

        self.assertTrue("Invalid input, max_value is lower than min_value" in str(context.exception))


if __name__ == '__main__':
    unittest.main()
