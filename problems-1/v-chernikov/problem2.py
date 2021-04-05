#!/usr/bin/env python3

def cut_off(min_value, max_value, args):
    if max_value < min_value:
        raise ValueError("Invalid input")
    return list(map(lambda x: max(min(max_value, x), min_value), args))


if __name__ == '__main__':
    nums = list(map(int, input().split(' ')))
    if len(nums) < 2:
        raise ValueError("Not enough arguments")
    print(cut_off(nums[0], nums[1], nums[2:]))
