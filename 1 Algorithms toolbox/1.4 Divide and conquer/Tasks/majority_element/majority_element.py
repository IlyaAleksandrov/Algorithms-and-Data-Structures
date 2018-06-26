# Task. The goal in this code problem is to check whether an input sequence contains a majority element.

# Input Format. The first line contains an integer 𝑛, the next one contains a sequence of 𝑛 non-negative
# integers 𝑎0, 𝑎1, . . . , 𝑎𝑛−1.

# Constraints. 1 ≤ 𝑛 ≤ 10^5; 0 ≤ 𝑎𝑖 ≤ 10^9 for all 0 ≤ 𝑖 < 𝑛.

# Output Format. Output majority element if the sequence contains an element that appears strictly more than 𝑛/2 times,
# and -1 otherwise.

import sys


def get_majority_element(a):
    l = len(a)
    if l == 2:
        if a[0] == a[1]:
            return a[0]
        else:
            return -1
    elif l == 1:
        return a[0]

    right = get_majority_element(a[: l/2])
    left = get_majority_element(a[l/2:])

    if right == -1 and left >= 0:
        return left
    elif left == -1 and right >= 0:
        return right

    if right == left:
        return right
    else:
        return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    print(get_majority_element(a))
