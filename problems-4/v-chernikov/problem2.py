#!/usr/bin/env python3

import sys
from argparse import ArgumentParser


def create_translation_table(t_from, t_to):
    if len(t_from) != len(t_to):
        raise ValueError("'from' length doesn't match 'to'")
    result = {}
    for i, symbol in enumerate(t_from):
        if symbol in result:
            raise ValueError("invalid 'from', trying to map symbol multiple times")
        result[symbol] = t_to[i]
    return result


def translate(table, to_delete, string):
    char_list = []
    for c in string:
        if c in to_delete:
            continue
        char_list.append(table.get(c, c))
    return ''.join(char_list)


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument("file", help="input file")
    parser.add_argument("src", help="characters to be translated")
    parser.add_argument("dst", help="characters replacing corresponding characters")
    parser.add_argument("-d", dest="delete", default="", help="characters to delete")
    args = parser.parse_args()
    try:
        with open(args.file, 'r', encoding='utf8') as file:
            table = create_translation_table(args.src, args.dst)
            to_delete = set(args.delete) if args.delete else set()
            content = file.read(4096)
            while content:
                sys.stdout.write(translate(table, to_delete, content))
                content = file.read(4096)
    except (OSError, ValueError) as e:
        sys.stderr.write(str(e) + "\n")
