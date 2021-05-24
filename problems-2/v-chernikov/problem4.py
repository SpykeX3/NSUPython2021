#!/usr/bin/env python3

import sys


def get_pi(filename):
    with open(filename) as f:
        content = f.read()
        return content.replace('\n', '')


def find_all(string, substring):
    positions = []
    index = string.find(substring)
    while index != -1:
        positions.append(index)
        index = string.find(substring, index + 1)
    return positions


def find_in_pi(digits: str, pi: str):
    if not digits.isdigit():
        raise ValueError()
    return find_all(pi, digits)


def print_occurrences(occurrences):
    print('Found ' + str(len(occurrences)) + ' results.')
    if occurrences:
        print('Positions: ' + ' '.join(map(str, occurrences[:5])) + (" ..." if len(occurrences) > 5 else ''))


if __name__ == '__main__':
    try:
        pi = get_pi('pi.txt')
        while True:
            print('Enter sequence to search for.')
            target = sys.stdin.readline().strip()
            if target == "exit":
                break
            try:
                print_occurrences(find_in_pi(target, pi))
            except ValueError:
                sys.stderr.write("Sequence must be numeric!\n")
    except IOError as e:
        sys.stderr.write("Error reading file pi.txt: " + str(e) + "\n")
