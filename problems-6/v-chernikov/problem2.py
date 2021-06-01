#!/usr/bin/env python3

import sys
import re
from argparse import ArgumentParser


def extract_urls(input_string):
    return list(
        map(lambda occ: occ[0],
            # (http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+)
            re.findall('\W(((http[s]?://(' +
                       '([a-zA-Z0-9s-]|%[0-9a-fA-F][0-9a-fA-F])+' +  # username
                       '(:([a-zA-Z0-9-]|%[0-9a-fA-F][0-9a-fA-F])+)?' +  # password
                       '@)?(www\\.)?)|(www\\.))' +  # prefix
                       '(([a-zA-Z0-9](?:[a-zA-Z0-9-]{0,63}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,})' +  # domain name
                       '(:[0-9]+)?' +
                       '((/([a-zA-Z0-9.-]|(%[0-9a-fA-F][0-9a-fA-F]))+)*(/?)))',  # path
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
