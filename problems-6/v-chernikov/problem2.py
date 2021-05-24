#!/usr/bin/env python3

import sys
import re
from argparse import ArgumentParser


def extract_urls(input_string):
    return list(
        map(lambda occ: occ[0],
            re.findall('\W(((http[s]?://)|(www\\.))([a-zA-Z-]+)*(\\.[a-zA-Z]+)+((/[a-zA-Z.-]+)+|/?))',
                       input_string)))


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument("file", help="input file")
    args = parser.parse_args()
    try:
        with open(args.file, 'r', encoding='utf8') as file:
            for line in file:
                for url in extract_urls(line):
                    print(url)
    except OSError as e:
        sys.stderr.write(str(e) + "\n")
