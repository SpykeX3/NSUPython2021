#!/usr/bin/env python3

import sys


def cut_off(min_value, max_value, args):
    if max_value < min_value:
        raise ValueError("Invalid input, max_value is lower than min_value")
    return list(map(lambda x: max(min(max_value, x), min_value), args))


def print_help():
    print("Illegal input, provide a sequence of decimal integers separated with spaces:")
    print("max_value min_value [value1 [value2 [...]]]")


if __name__ == '__main__':
    try:
        nums = list(map(int, input().split(' ')))
        if len(nums) < 2:
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
