# Problem Introduction
# You would like to compute the minimum number of flight segments to get from one city to another one. For
# this, you construct the following undirected graph: vertices represent cities, there is an edge between two
# vertices whenever there is a flight between the corresponding two cities. Then, it suffices to find a shortest
# path from one of the given cities to the other one.

# Task. Given an undirected graph with n vertices and m edges and two vertices u and v, compute the length
# of a shortest path between u and v (that is, the minimum number of edges in a path from u to v).

# Input Format. A graph is given in the standard format. The next line contains two vertices u and v.

# Constraints. 2 <= n <= 10^5, 0 <= m <= 10^5, u != v, 1 <= u,v <= n.

# Output Format. Output the minimum number of edges in a path from u to v, or -1 if there is no path.

import sys
import queue


# implementation of Breadth-first Search
# initialize the array of distances with values -1, from the initial node we look for all the connected nodes,
# assign them distance 1 and add to the processing queue. We continue to search for the child unvisited nodes,
# each time increasing the distance to it by 1 from the parent.
def distance(adj, s, t):
    Q.append(s)
    dist[s] = 0
    while Q != []:
        x = Q.pop(0)
        for i in adj[x]:
            if dist[i] == -1:
                Q.append(i)
                dist[i] = dist[x] + 1
    return dist[t]


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    dist = [-1 for i in range(n)]
    Q = []
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))
# Example of input:
# 4 4
# 1 2
# 4 1
# 2 3
# 3 1
# 2 4
# Output:
# 2
# Explanation:
# There is a unique shortest path between vertices 2 and 4 in this graph: 2 - 1 - 4.
