#!/usr/bin/env python3


import os
import os.path as p
import sys
from collections import defaultdict
from argparse import ArgumentParser


def get_files_tuples(path):
    files_dict = defaultdict(list)
    for f in os.listdir(path):
        filepath = p.join(path, f)
        if p.isfile(p.join(path, f)):
            files_dict[p.getsize(filepath)].append(f)
        else:
            files_dict[0].append(f)
    result = []
    for k in sorted(files_dict.keys()):
        for f in files_dict[k]:
            result.append((k, f))
    return result


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('path', nargs='?', help="Path directory.", default=os.getcwd())
    args = parser.parse_args()
    try:
        for tpl in get_files_tuples(args.path):
            print(tpl[1] + " : " + str(tpl[0]))
    except IOError as e:
        sys.stderr.write(str(e) + "\n")
