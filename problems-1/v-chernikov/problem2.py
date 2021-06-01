#!/usr/bin/env python3

import sys


def cut_off(min_value, max_value, args):
    if max_value < min_value:
        raise ValueError("Invalid input, max_value is lower than min_value: " + str(max_value) + "<" + str(min_value))
    return list(map(lambda x: max(min(max_value, x), min_value), args))


def print_help():
    print("Provide a sequence of decimal integers separated with spaces:")
    print("max_value min_value [value1 [value2 [...]]]")


if __name__ == '__main__':
    try:
        try:
            nums = list(map(int, input().split(' ')))
        except ValueError as e:
            raise ValueError("Error while parsing input numbers: " + str(e))
        if len(nums) < 2:
            sys.stderr.write("Not enough arguments\n")
            print_help()
        else:
            try:
                print(cut_off(nums[0], nums[1], nums[2:]))
            except ValueError as e:
                sys.stderr.write(str(e) + "\n")
                print_help()
    except ValueError as e:
        sys.stderr.write(str(e) + "\n")
        print_help()
