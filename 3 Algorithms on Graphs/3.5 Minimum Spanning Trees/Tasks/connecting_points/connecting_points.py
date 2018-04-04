# Problem Introduction
# In this problem, the goal is to build roads between some pairs of the
# given cities such that there is a path between any two cities and the
# total length of the roads is minimized.

# Task. Given n points on a plane, connect them with segments of minimum total length such that there is a
# path between any two points. Recall that the length of a segment with endpoints (x1; y1) and (x2; y2)
# is equal to
# p
# (x1 􀀀 x2)2 + (y1 􀀀 y2)2.

# Input Format. The first line contains the number n of points. Each of the following n lines defines a point
# (xi; yi).

# Constraints. 1  n  200; 􀀀103  xi; yi  103 are integers. All points are pairwise different, no three
# points lie on the same line.

# Output Format. Output the minimum total length of segments. The absolute value of the difference
# between the answer of your program and the optimal value should be at most 10􀀀6. To ensure this,
# output your answer with at least seven digits after the decimal point (otherwise your answer, while
# being computed correctly, can turn out to be wrong because of rounding issues).

import sys
import math


def minimum_distance(x, y):
    # изначально все вершины разъеденины, по мере того как мы будем их соединять, необходимо знать лежат ли они
    # в одном connected component или нет (если лежат то не нужно их соединять повторно).
    # Функция находит главный элемент каждого СС.
    def find(x):
        if ids[x] == x:
            return x
        return find(ids[x])
    # переменная хранит общую длинну всех итоговых связей
    result = 0
    # строим граф содержащий все возможные ребра между вершинами
    for i in range(n):
        for j in range(n):
            dist = [((x[j] - x[i]) ** 2 + (y[j] - y[i]) ** 2) ** 0.5, j, i]
            if dist[0] > 0:
                edges.append(dist)
    # сортируем все ребра и начиная с минимального объединяем вершины,
    # если вершины уже в одном CC, то пропускаем ребро.
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


