# Task. The goal in this code problem is to check whether an input sequence contains a majority element.

# Input Format. The first line contains an integer 𝑛, the next one contains a sequence of 𝑛 non-negative
# integers 𝑎0, 𝑎1, . . . , 𝑎𝑛−1.

# Constraints. 1 ≤ 𝑛 ≤ 105; 0 ≤ 𝑎𝑖 ≤ 109 for all 0 ≤ 𝑖 < 𝑛.

# Output Format. Output 1 if the sequence contains an element that appears strictly more than 𝑛/2 times,
# and 0 otherwise.

import sys

def get_majority_element(a, left, right):
    b = {}
    for i in a:
        b[i] = b.get(i, 0) + 1
    for j in b:
        if b.get(j) > len(a)/2:
            return 1
    return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    print(get_majority_element(a, 0, n))

