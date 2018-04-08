# Problem Introduction
# In this problem, you will apply an algorithm for finding maximum flow
# in a network to determine how fast people can be evacuated from the
# given city.

# Task. A tornado is approaching the city, and we need to evacuate the people quickly. There are several
# roads outgoing from the city to the nearest cities and other roads going further. The goal is to evacuate
# everybody from the city to the capital, as it is the only other city which is able to accomodate that
# many newcomers. We need to evacuate everybody as fast as possible, and your task is to find out
# what is the maximum number of people that can be evacuated each hour given the capacities of all
# the roads.

# Input Format. The first line of the input contains integers 𝑛 and 𝑚 — the number of cities and the number
# of roads respectively. Each of the next 𝑚 lines contains three integers 𝑢, 𝑣 and 𝑐 describing a particular
# road — start of the road, end of the road and the number of people that can be transported through
# this road in one hour. 𝑢 and 𝑣 are the 1-based indices of the corresponding cities.
# The city from which people are evacuating is the city number 1, and the capital city is the city number
# 𝑛.
# Note that all the roads are given as one-directional, that is, you cannot transport people
# from 𝑣 to 𝑢 using a road that connects 𝑢 to 𝑣. Also note that there can be several roads
# connecting the same city 𝑢 to the same city 𝑣, there can be both roads from 𝑢 to 𝑣 and
# from 𝑣 to 𝑢, or there can be only roads in one direction, or there can be no roads between
# a pair of cities. Also note that there can be roads going from a city 𝑢 to itself in the
# input.
# When evacuating people, they cannot stop in the middle of the road or in any city other than the
# capital. The number of people per hour entering any city other than the evacuating city 1 and the
# capital city 𝑛 must be equal to the number of people per hour exiting from this city. People who left
# a city 𝑢 through some road (𝑢, 𝑣, 𝑐) are assumed to come immediately after that to the city 𝑣. We
# are interested in the maximum possible number of people per hour leaving the city 1 under the above
# restrictions.

# Constraints. 1 ≤ 𝑛 ≤ 100; 0 ≤ 𝑚 ≤ 10 000; 1 ≤ 𝑢, 𝑣 ≤ 𝑛; 1 ≤ 𝑐 ≤ 10 000. It is guaranteed that
# 𝑚 · EvacuatePerHour ≤ 2 · 108, where EvacuatePerHour is the maximum number of people that can
# be evacuated from the city each hour — the number which you need to output.

# Output Format. Output a single integer — the maximum number of people that can be evacuated from
# the city number 1 each hour.


class Edge:

    def __init__(self, u, v, capacity):
        self.u = u
        self.v = v
        self.capacity = capacity
        self.flow = 0

# Комментарии от составителей задачи:
# This class implements a bit unusual scheme for storing edges of the graph,
# in order to retrieve the backward edge for a given edge quickly.
class FlowGraph:

    def __init__(self, n):
        # Комментарии от составителей задачи:
        # List of all - forward and backward - edges
        self.edges = []
        # These adjacency lists store only indices of edges in the edges list
        self.graph = [[] for _ in range(n)]

    def add_edge(self, from_, to, capacity):
        # Комментарий от составителей задачи:
        # Note that we first append a forward edge and then a backward edge,
        # so all forward edges are stored at even indices (starting from 0),
        # whereas backward edges are stored at odd indices.
        forward_edge = Edge(from_, to, capacity)
        backward_edge = Edge(to, from_, 0)
        self.graph[from_].append(len(self.edges))
        self.edges.append(forward_edge)
        self.graph[to].append(len(self.edges))
        self.edges.append(backward_edge)

    def size(self):
        return len(self.graph)

    def get_ids(self, from_):
        return self.graph[from_]

    def get_edge(self, id):
        return self.edges[id]

    def add_flow(self, id, flow):
        self.edges[id].flow += flow
        self.edges[id + 1].flow -= flow


def read_data():
    vertex_count, edge_count = map(int, input().split())
    graph = FlowGraph(vertex_count)
    for _ in range(edge_count):
        u, v, capacity = map(int, input().split())
        graph.add_edge(u - 1, v - 1, capacity)
    return graph


def max_flow(graph, from1, to):
    flow = 0
    # реализуем Breadth - first Search (см. 3.3)
    # Мы используем BFS для нахождения кратчайшего пути, т.к. он поможет избежать осложнений на некоторых графах
    # (см. лекции) Также необходимо понимать механизм построения residual графа.
    def BFS(graph, from1, to):
        parent = [0 for i in range(graph.size())]
        dist = [-1 for i in range(graph.size())]
        Q = []
        Q.append(from1)
        dist[from1] = 0
        while Q:
            x = Q.pop(0)
            for i in graph.get_ids(x):
                dir = graph.get_edge(i).v
                if dist[dir] == -1 and graph.get_edge(i).capacity > 0:
                    Q.append(dir)
                    dist[dir] = dist[x] + graph.get_edge(i).capacity
                    parent[dir] = i
        route = []
        # строим самый короткий маршрут
        if dist[to] > 0:
            while to != 0:
                route.append(parent[to])
                to = graph.get_edge(parent[to]).u
            route.reverse()
            return route
        else:
            return False

    # пока мы можем построить любой путь из пункта назначения в конечный продолжаем цикл
    while True:
        path = BFS(graph, from1, to)
        if not path:
            break
        # ищем в найденом маршруте ребро с наименьшей пропускной способностью
        minCap = graph.get_edge(path[0]).capacity
        for i in path:
            if graph.get_edge(i).capacity < minCap:
                minCap = graph.get_edge(i).capacity
        # добавляем поток равный пропускной способности узкого ребра в граф
        for j in path:
            graph.add_edge(graph.get_edge(j).v, graph.get_edge(j).u, minCap)
            graph.add_flow(j, minCap)
            graph.get_edge(j).capacity -= minCap
        flow += minCap
    return flow


if __name__ == '__main__':
    graph = read_data()
    print(max_flow(graph, 0, graph.size() - 1))
