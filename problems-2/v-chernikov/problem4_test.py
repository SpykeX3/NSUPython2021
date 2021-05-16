#!/usr/bin/env python3

import unittest
import problem4 as p4


class Problem4TestCase(unittest.TestCase):
    pi = p4.get_pi('pi.txt')

    def test_findall(self):
        self.assertEqual(p4.find_all('aaaaa', 'aaa'), [0, 1, 2])

    def test_find_in_pi(self):
        self.assertEqual(p4.find_in_pi('1377993', Problem4TestCase.pi), [1771626])
        self.assertEqual(p4.find_in_pi('100500', Problem4TestCase.pi), [49668, 128801, 709900])
        self.assertEqual(len(p4.find_in_pi('10', Problem4TestCase.pi)), 41878)
        self.assertEqual(len(p4.find_in_pi('123789', Problem4TestCase.pi)), 5)


if __name__ == '__main__':
    unittest.main()
