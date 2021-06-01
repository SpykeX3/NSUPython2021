#!/usr/bin/env python3

import unittest
import problem2 as p

expected = [
    'www.google.com',
    'http://google.com',
    'https://google.com',
    'https://google.com.org',
    'https://google.ru/',
    'www.google.ru/',
    'www.google.ru/page',
    'http://www.com',
    'http://www.com/page',
    'http://www.com/page.php',
    'www.lego-site.com',
    'www.lego-site.co',
    'www.longurl.com.org.ucoz/this/path/is/very/very/very/very-very/long.html',
    'http://link.link',
    'www.i-have-a-port.com:8080',
    'http://top-secret.org:30/%33%f0',
    'http://username@top-secret.org:30/%33%f0',
    'http://u5%55rn4me:pa55w%0fRD@top-secret.org:30/%33%f0',
    'http://u5%55rn4me:pa55w%0fRD@top-secret.org:30/abc/100500sdfv/df%41%41%41'
]


class MyTestCase(unittest.TestCase):
    def test_urls(self):
        with open("urlsInput.txt", 'r', encoding='utf8') as file:
            actual = p.extract_urls(file.read())
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
