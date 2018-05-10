# Problem Introduction
# This problem is about implementing an algorithm for the knapsack without repetitions problem.

# Task. In this problem, you are given a set of bars of gold and your goal is to take as much gold as possible
# into your bag. There is just one copy of each bar and for each bar you can either take it or not (hence
# you cannot take a fraction of a bar).

# Input Format. The first line of the input contains the capacity W of a knapsack and the number n of bars
# of gold. The next line contains n integers w0;w1; : : : ;wn-1 defining the weights of the bars of gold.

# Constraints. 1 <= W <= 10^4; 1 <= n <= 300; 0 <= w0; : : : ;wn-1 <= 10^5.

# Output Format. Output the maximum weight of gold that fits into a knapsack of capacity W.

import sys


def optimal_weight(W, w):
    n = len(w)
    # initializing matrix n х W (elements x capacity)
    value = [[0 for x in range(n + 1)] for y in range(W + 1)]
    # remain first column and first row stay equals zeroes (Zero capacity / Zero elements were taken).
    for i in range(1, n + 1):
        for j in range(1, W + 1):
            # firstly, initialize the cell with the value of same knapsack capacity (j), but without new element(i-1)
            value[j][i] = value[j][i - 1]
            # if the current capacity fits to add new element
            if w[i - 1] <= j:
                # we finding in table maximum value which we could achieve with i-1 elements? with the condition
                # that were will be enough space for new element(current capacity j minus weight of new element)
                val = value[j - w[i - 1]][i - 1] + w[i - 1]
                # if the value is greater then initially assigned, taking it in account
                if value[j][i] < val:
                    value[j][i] = val
    # return the value of the max capacity and n
    return value[W][n]


if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
# Example of input:
# 10 3 (10 - capacity, 3 - number of bars)
# 1 4 8 (weight of bars)
# Output:
# 9
