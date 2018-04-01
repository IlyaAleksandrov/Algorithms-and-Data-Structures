# Problem Introduction
# A Computer Science curriculum specifies the prerequisites for each course as a list of courses that should be
# taken before taking this course. You would like to perform a consistency check of the curriculum, that is,
# to check that there are no cyclic dependencies. For this, you construct the following directed graph: vertices
# correspond to courses, there is a directed edge (𝑢, 𝑣) is the course 𝑢 should be taken before the course 𝑣.
# Then, it is enough to check whether the resulting graph contains a cycle.

# Task. Check whether a given directed graph with 𝑛 vertices and 𝑚 edges contains a cycle.

# Input Format. A graph is given in the standard format.

# Constraints. 1 ≤ 𝑛 ≤ 103, 0 ≤ 𝑚 ≤ 103.

# Output Format. Output 1 if the graph contains a cycle and 0 otherwise.

import sys


def acyclic(adj):

    def explore(x):
        global count
        visited[x] = True
        for i in adj[x]:
            if not visited[i]:
                explore(i)
        postvisit[x] = count
        count += 1

    # перебираем все узлы и номеруем их post-order
    for i in range(len(adj)):
        if not visited[i]:
            visited[i] = True
            explore(i)
    # если у дочернего узла Post-order номер меньше чем у узла-роителя, то в графе есть цикл
    for x in range(len(adj)):
        for h in adj[x]:
            if postvisit[x] < postvisit[h]:
                return 1
    return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    visited = [False for i in range(n)]
    count = 1
    postvisit = [0 for i in range(n)]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))

