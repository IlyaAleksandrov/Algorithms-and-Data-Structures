# Problem Introduction
# You are given a list of currencies c1, c2, ... cn together with a list of exchange rates: rij is the number of units
# of currency cj that one gets for one unit of ci. You would like to check whether it is possible to start with
# one unit of some currency, perform a sequence of exchanges, and get more than one unit of the same currency.
# In other words, you would like to find currencies ci1, ci2, .. cik such that ri1,i2 *  ri2,i3 * rik-1;ik ; rik;i1 > 1.
# For this, you construct the following graph: vertices are currencies c1, c2, ... cn, the weight of an edge from ci
# to cj is equal to -log rij . There it suffices to check whether is a negative cycle in this graph. Indeed, assume
# that a cycle ci - cj - ck - ci has negative weight. This means that -(log cij + log cjk + log cki) < 0 and hence
# log cij + log cjk + log cki > 0.
# This, in turn, means that
# rij rjk rki = 2^log cij * 2^log cjk * 2^log cki = 2^(log cij+log cjk+log cki) > 1.

# Task. Given an directed graph with possibly negative edge weights and with n vertices and m edges, check
# whether it contains a cycle of negative weight.

# Input Format. A graph is given in the standard format.

# Constraints. 1 <= n <= 10^3, 0 <= m <= 10^4, edge weights are integers of absolute value at most 10^3.

# Output Format. Output 1 if the graph contains a cycle of negative weight and 0 otherwise.

import sys
import math


# the graph contains a negative cycle, if we still make changes to the n + 1 iteration of the dijkstra's algorithm
def negative_cycle(adj, cost):
    for h in range(n + 1):
        # At the beginning of each iteration, we set the flag false
        flag = False
        for u in range(n):
            count = 0
            for v in adj[u]:
                if dist[v] > dist[u] + cost[u][count]:
                    dist[v] = dist[u] + cost[u][count]
                    prev[v] = u
                    # at the output of the function the flag will be true only if the changes were in n + 1 iteration
                    # (the last iteration)
                    flag = True
                count += 1
    if flag:
        return 1
    return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)

    dist = [10 ** 8 + 1 for i in range(n)]
    prev = [-1 for i in range(n)]
    dist[0] = 0

    print(negative_cycle(adj, cost))

# Input:
# 4 4
# 1 2 -5
# 4 1 2
# 2 3 2
# 3 1 1
# Output:
# 1
# Explanation:
# The weight of the cycle 1 - 2 - 3 is equal to -2, that is, negative.
