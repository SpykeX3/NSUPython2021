#!/usr/bin/env python3

import sys
from collections import defaultdict


def inverse_dict(dictionary):
    inversed_dict = defaultdict(list)
    for k, v in dictionary.items():
        for word in v:
            inversed_dict[word].append(k)
    return inversed_dict


def pretty_print(dictionary):
    keys = sorted(dictionary.keys())
    for k in keys:
        print(k + ' - ' + (', '.join(dictionary[k])))


def parse_dictionary(filename):
    dictionary = defaultdict(list)
    with open(filename) as f:
        content = f.readlines()
    for line in content:
        line = line.strip().replace(' ', '').replace('-', ',')
        words = line.split(',')
        word = words[0]
        for definition in words[1:]:
            dictionary[word].append(definition)
    return dictionary


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.stderr.write("Error: no dictionary specified\n")
    else:
        try:
            dictionary = parse_dictionary(sys.argv[1])
            pretty_print(inverse_dict(dictionary))
        except IOError as e:
            sys.stderr.write("Can't read file " + sys.argv[1] + ": " + str(e)+"\n")
