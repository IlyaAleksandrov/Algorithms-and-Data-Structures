# Problem Introduction
# Now, you are interested in minimizing not the number of segments, but the total cost of a flight. For this
# you construct a weighted graph: the weight of an edge from one city to another one is the cost of the
# corresponding flight.

# Task. Given an directed graph with positive edge weights and with n vertices and m edges as well as two
# vertices u and v, compute the weight of a shortest path between u and v (that is, the minimum total
# weight of a path from u to v).

# Input Format. A graph is given in the standard format. The next line contains two vertices u and v.

# Constraints. 1  n  103, 0  m  105, u 6= v, 1  u; v  n, edge weights are non-negative integers not
# exceeding 103.

# Output Format. Output the minimum weight of a path from u to v, or 􀀀1 if there is no path.

import sys
import queue

# реализуем алгоритм дийкстры

def distance(adj, cost, s, t):
    # изначально расстояние до всех узлов infinity
    dist[s] = 0
    # добавляем в очередь исходный узел
    H.append(s)
    while H != []:
        count = 0
        min = 0
        #
        for i in range(len(H)):
            if dist[H[i]] < dist[H[min]]:
                min = i
        # выбираем узел в очереди путь до которого минимален
        u = H.pop(min)
        # для каждого узла достижимого из выбранного ближайшего узла,
        # мы про проверяем оптимальность пути через этот узел
        for v in adj[u]:
            if dist[v] > dist[u] + cost[u][count]:
                dist[v] = dist[u] + cost[u][count]
                # сохраняем узел который привел нас к текущему для итогого построения пути
                # (для данной задачи можно опустить)
                prev[v] = u
                H.append(v)
            count += 1
    # итоговая проверка достижим ли искомый узел
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
