# Problem Introduction
# You are given a primitive calculator that can perform the following three operations with the current number
# x: multiply x by 2, multiply x by 3, or add 1 to x. Your goal is given a positive integer n, find the
# minimum number of operations needed to obtain the number n starting from the number 1.

# Task. Given an integer n, compute the minimum number of operations needed to obtain the number n
# starting from the number 1.

# Input Format. The input consists of a single integer 1 <= n <= 10^6.

# Output Format. In the first line, output the minimum number k of operations needed to get n from 1.
# In the second line output a sequence of intermediate numbers. That is, the second line should contain
# positive integers a0; a2; : : : ; ak-1 such that a0 = 1, ak-1 = n and for all 0 <= i < k <= 1, ai+1 is equal to
# either ai + 1, 2ai, or 3ai. If there are many such sequences, output any one of them.

import sys


def optimal_sequence(n):
    # initializing an array, index of the array shows the quantity of actions to reach from 1 to index.
    MinNumOfCoins = [0, 0, 1, 1, 2]
    # making an array of last actions for reaching index element (1. *3, 2. *2, 3. +1)
    Actions = [0, 0, 3, 1, 2]
    # const of MAX value
    MAX = 10**6
    # filling the arrays with default values till n-th element
    for m in range(5, n + 1):
        MinNumOfCoins.append(MAX)
        Actions.append(-1)
        # checking the index to divide on 3 and 2, otherwise taking +1 operation
        if m % 3 == 0:
            NumActions = MinNumOfCoins[m // 3] + 1
            MinNumOfCoins[m] = NumActions
            Actions[m] = 1
        if m % 2 == 0:
            NumActions = MinNumOfCoins[m // 2] + 1
            # checking optimality of the answer of division by 2
            if NumActions < MinNumOfCoins[m]:
                MinNumOfCoins[m] = NumActions
                Actions[m] = 2
        NumActions = MinNumOfCoins[m - 1] + 1
        # checking optimality of the answer of adding 1
        if NumActions < MinNumOfCoins[m]:
            MinNumOfCoins[m] = NumActions
            Actions[m] = 3
    # making a sequence of changes for input
    seq = [n]
    while n != 1:
        seq.append(MakeAction(n, Actions[n]))
        n = seq[len(seq) - 1]
    seq.reverse()
    return seq


# function is used for making a sequence of of intermediate numbers
def MakeAction(s, a):
    if a == 1:
        return s//3
    elif a == 2:
        return s//2
    return s - 1


input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
# Example of input:
# 96234
# Output:
# 14
# 1 3 9 10 11 22 66 198 594 1782 5346 16038 16039 32078 96234
