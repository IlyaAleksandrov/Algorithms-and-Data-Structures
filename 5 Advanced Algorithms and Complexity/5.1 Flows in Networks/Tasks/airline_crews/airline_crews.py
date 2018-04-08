# Problem Introduction
# In this problem, you will apply an algorithm for finding maximum matching
# in a bipartite graph to assign airline crews to flights in the most
# efficient way.

# Task. The airline offers a bunch of flights and has a set of crews that can work on those flights. However,
# the flights are starting in different cities and at different times, so only some of the crews are able to
# work on a particular flight. You are given the pairs of flights and associated crews that can work on
# those flights. You need to assign crews to as many flights as possible and output all the assignments.

# Input Format. The first line of the input contains integers 𝑛 and 𝑚 — the number of flights and the number
# of crews respectively. Each of the next 𝑛 lines contains 𝑚 binary integers (0 or 1). If the 𝑗-th integer
# in the 𝑖-th line is 1, then the crew number 𝑗 can work on the flight number 𝑖, and if it is 0, then it
# cannot.

# Constraints. 1 ≤ 𝑛,𝑚 ≤ 100.

# Output Format. Output 𝑛 integers — for each flight, output the 1-based index of the crew assigned to
# this flight. If no crew is assigned to a flight, output −1 as the index of the crew corresponding to it.
# All the positive indices in the output must be between 1 and 𝑚, and they must be pairwise different,
# but you can output any number of −1’s. If there are several assignments with the maximum possible
# number of flights having a crew assigned, output any of them.


class MaxMatching:
    def read_data(self):
        n, m = map(int, input().split())
        adj_matrix = [list(map(int, input().split())) for i in range(n)]
        return adj_matrix

    def write_response(self, matching):
        line = [str(-1 if x == -1 else x + 1) for x in matching]
        print(' '.join(line))

    def find_matching(self, adj_matrix):

        class Edge:
            def __init__(self, u, v, capacity):
                self.u = u
                self.v = v
                self.capacity = capacity
                self.flow = 0

        class FlowGraph:
            def __init__(self, n):
                self.edges = []
                self.graph = [[] for _ in range(n)]

            def add_edge(self, from_, to, capacity):
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
                self.edges[id ^ 1].flow -= flow

        # механизм нахождения максимального потока расписан в предидущей задаче
        def max_flow(graph, from1, to):
            flow = 0

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
                if dist[to] > 0:
                    while to != 0:
                        route.append(parent[to])
                        to = graph.get_edge(parent[to]).u
                    route.reverse()
                    return route
                else:
                    return False

            while True:
                path = BFS(graph, from1, to)
                if not path:
                    break
                minCap = graph.get_edge(path[0]).capacity
                for i in path:
                    if graph.get_edge(i).capacity < minCap:
                        minCap = graph.get_edge(i).capacity
                for j in path:
                    graph.get_edge(j + 1).capacity += 1
                    graph.add_flow(j, minCap)
                    graph.get_edge(j).capacity -= minCap
                flow += minCap
            return flow

        # задачу поиска максимального количества путей необходимо свести к задаче максимального потока.
        # Нужно добавить исходную и конечную вершины и построить максимальный поток через них.
        # Все ребра длинны 1.
        n = len(adj_matrix)
        m = len(adj_matrix[0])
        result = [-1 for _ in range(n)]
        graph = FlowGraph(n + m + 2)
        for i in range(n):
            for j in range(m):
                if adj_matrix[i][j] == 1:
                    graph.add_edge(i + 1, n + j + 1, 1)

        for i in range(n):
            graph.add_edge(0, i + 1, 1)

        for j in range(m):
            graph.add_edge(n + j + 1, m + n + 1, 1)

        max_flow(graph, 0, n + m + 1)

        for i in range(n):
            for edge in graph.edges:
                if edge.v == i + 1 and edge.flow < 0:
                    result[i] = edge.u - n - 1
        return result

    def solve(self):
        adj_matrix = self.read_data()
        matching = self.find_matching(adj_matrix)
        self.write_response(matching)


if __name__ == '__main__':
    max_matching = MaxMatching()
    max_matching.solve()
