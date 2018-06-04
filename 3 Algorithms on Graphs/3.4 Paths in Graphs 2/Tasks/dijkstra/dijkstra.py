# Problem Introduction
# Now, you are interested in minimizing not the number of segments, but the total cost of a flight. For this
# you construct a weighted graph: the weight of an edge from one city to another one is the cost of the
# corresponding flight.

# Task. Given an directed graph with positive edge weights and with n vertices and m edges as well as two
# vertices u and v, compute the weight of a shortest path between u and v (that is, the minimum total
# weight of a path from u to v).

# Input Format. A graph is given in the standard format. The next line contains two vertices u and v.

# Constraints. 1 <= n <= 10^3, 0 <= m <= 10^5, u != v, 1 <= u; v <= n, edge weights are non-negative integers not
# exceeding 103.

# Output Format. Output the minimum weight of a path from u to v, or 􀀀1 if there is no path.

import sys
import queue

# implementation of dijkstra algorithm


def distance(adj, cost, s, t):
    # initially the distance to all nodes is equal to infinity
    dist[s] = 0
    # add the initial node to the queue
    H.append(s)
    while H != []:
        count = 0
        min = 0
        for i in range(len(H)):
            if dist[H[i]] < dist[H[min]]:
                min = i
        # select the node in the queue path to which is minimal
        u = H.pop(min)
        # for each node reachable from the selected nearest node,
        # we check the optimality of the path through this node
        for v in adj[u]:
            if dist[v] > dist[u] + cost[u][count]:
                dist[v] = dist[u] + cost[u][count]
                # save the node that led us to the current one for the total path construction
                # (for that task can be omitted)
                prev[v] = u
                H.append(v)
            count += 1
    # final check whether the target node is reachable
    if dist[t] != 10**8 + 1:
        return dist[t]
    return -1


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
    s, t = data[0] - 1, data[1] - 1

    dist = [10**8 + 1 for i in range(n)]
    prev = [-1 for i in range(n)]
    H = []

    print(distance(adj, cost, s, t))

# Input:
# 4 4
# 1 2 1
# 4 1 2
# 2 3 2
# 1 3 5
# 1 3
# Output:
# 3
# Explanation:
# There is a unique shortest path from vertex 1 to vertex 3 in this graph (1 - 2 - 3), and it has weight 3.
