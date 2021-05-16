#!/usr/bin/env python3

import unittest
import problem2 as p2


class TestDict(unittest.TestCase):
    def test_double(self):
        d = p2.parse_dictionary('dictionary.txt')
        self.assertEqual(d, p2.inverse_dict(p2.inverse_dict(d)))

    def test_result(self):
        d = p2.parse_dictionary('dictionary.txt')
        i = p2.inverse_dict(d)

        self.assertEqual(i['malum'], ['apple', 'punishment'])
        self.assertEqual(i['baca'], ['fruit'])
        self.assertEqual(i['popum'], ['fruit'])
        self.assertEqual(i['bacca'], ['fruit'])
        self.assertEqual(i['popula'], ['apple'])
        self.assertEqual(i['multa'], ['punishment'])
        self.assertEqual(i['pomum'], ['apple'])
        self.assertEqual(len(i.keys()), 7)


if __name__ == "__main__":
    unittest.main()
