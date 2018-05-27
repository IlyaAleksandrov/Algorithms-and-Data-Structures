# Problem Introduction
# Now, when you are sure that there are no cyclic dependencies in the given CS curriculum, you would like to
# find an order of all courses that is consistent with all dependencies. For this, you find a topological ordering
# of the corresponding directed graph.

# Task. Compute a topological ordering of a given directed acyclic graph (DAG) with 𝑛 vertices and 𝑚 edges.

# Input Format. A graph is given in the standard format.

# Constraints. 1 ≤ 𝑛 ≤ 105, 0 ≤ 𝑚 ≤ 105. The given graph is guaranteed to be acyclic.

# Output Format. Output any topological ordering of its vertices. (Many DAGs have more than just one
# topological ordering. You may output any of them.)

import sys


def toposort(adj):
    def explore(x):
        global count
        visited[x] = True
        for i in adj[x]:
            if not visited[i]:
                explore(i)
                postvisit.append(i + 1)

    # traverse nodes post-order and adding to the array
    for i in range(len(adj)):
        if not visited[i]:
            explore(i)
            postvisit.append(i + 1)
    postvisit.reverse()


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    visited = [False for i in range(n)]
    postvisit = []
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    toposort(adj)
    print(*postvisit)
# Example of input:
# 4 3
# 1 2
# 4 1
# 3 1
# Output:
# 4 3 1 2
