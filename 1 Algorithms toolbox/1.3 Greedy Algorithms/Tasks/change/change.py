# Task. The goal in this problem is to find the minimum number
# of coins needed to change the input value (an integer)
#  into coins with denominations 1, 5, and 10.

import sys


def get_change(m):
    count = 0
    left = m
    while left != 0:
        if left >= 10:
            left -= 10
        elif left >= 5:
            left -= 5
        else:
            left -= 1
        count += 1
    return count


m = int(input())
print(get_change(m))
