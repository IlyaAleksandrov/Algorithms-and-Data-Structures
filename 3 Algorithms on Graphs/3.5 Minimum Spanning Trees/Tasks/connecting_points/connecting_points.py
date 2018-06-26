# Problem Introduction
# In this problem, the goal is to build roads between some pairs of the
# given cities such that there is a path between any two cities and the
# total length of the roads is minimized.

# Task. Given n points on a plane, connect them with segments of minimum total length such that there is a
# path between any two points. Recall that the length of a segment with endpoints (x1; y1) and (x2; y2)
# is equal to ((x1 - x2)^2 + (y1 - y2)^2)^(1/2).

# Input Format. The first line contains the number n of points. Each of the following n lines defines a point
# (xi; yi).

# Constraints. 1 <= n <= 200; -10^3 <= xi, yi <= 10^3 are integers. All points are pairwise different, no three
# points lie on the same line.

# Output Format. Output the minimum total length of segments. The absolute value of the difference
# between the answer of your program and the optimal value should be at most 10^-6. To ensure this,
# output your answer with at least seven digits after the decimal point (otherwise your answer, while
# being computed correctly, can turn out to be wrong because of rounding issues).

import sys
import math

# implementation of Kruskal’s algorithm

def minimum_distance(x, y):
    # Initially, all the vertices are disconnected, as we connect them, it is necessary to know do they lie
    # in one connected component or not (if they are, then you do not need to reconnect them).
    # The function finds the main element of each CC.
    def find(x):
        if ids[x] == x:
            return x
        return find(ids[x])
    # variable stores the total length of all resulting distances
    result = 0
    # we construct a graph containing all possible edges between vertices
    for i in range(n):
        for j in range(n):
            dist = [((x[j] - x[i]) ** 2 + (y[j] - y[i]) ** 2) ** 0.5, j, i]
            if dist[0] > 0:
                edges.append(dist)
    # sort all edges and starting from the minimum join vertices,
    # if vertices are already in same CC we skip such edges
    edges.sort()
    for e in edges:
        if find(e[1]) != find(e[2]):
            result += e[0]
            ids[find(e[1])] = e[2]
    return result


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]

    ids = [i for i in range(n)]

    edges = []
    print("{0:.9f}".format(minimum_distance(x, y)))

# Example of input:
# 5
# 0 0
# 0 2
# 1 1
# 3 0
# 3 2
# Output:
# 7.064495102
