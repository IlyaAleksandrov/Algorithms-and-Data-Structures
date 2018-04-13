# Problem Introduction
# In this problem, you will design and implement an efficient algorithm
# to plan invite the coolest people from your company to a party in such
# a way that everybody is relaxed, because the direct boss of any invited
# person is not invited.

# Task. You’re planning a company party. You’d like to invite the coolest people, and you’ve assigned each
# one of them a fun factor — the more the fun factor, the cooler is the person. You want to maximize the
# total fun factor (sum of the fun factors of all the invited people). However, you can’t invite everyone,
# because if the direct boss of some invited person is also invited, it will be awkward. Find out what is
# the maximum possible total fun factor.

# Input Format. The first line contains an integer 𝑛 — the number of people in the company. The next line
# contains 𝑛 numbers 𝑓𝑖 — the fun factors of each of the 𝑛 people in the company. Each of the next 𝑛−1
# lines describes the subordination structure. Everyone but for the CEO of the company has exactly one
# direct boss. There are no cycles: nobody can be a boss of a boss of a ... of a boss of himself. So, the
# subordination structure is a regular tree. Each of the 𝑛 − 1 lines contains two integers 𝑢 and 𝑣, and
# you know that either 𝑢 is the boss of 𝑣 or vice versa (you don’t really need to know which one is the
# boss, but you can invite only one of them or none of them).

# Constraints. 1 ≤ 𝑛 ≤ 100 000; 1 ≤ 𝑓𝑖 ≤ 1 000; 1 ≤ 𝑢, 𝑣 ≤ 𝑛; 𝑢 ̸= 𝑣.

# Output Format. Output the maximum possible total fun factor of the party (the sum of fun factors of all
# the invited people).

import sys
import threading


# This code is used to avoid stack overflow issues
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**26)  # new thread will get stack of such size


class Vertex:
    def __init__(self, weight):
        self.weight = weight
        self.children = []


def ReadTree():
    size = int(input())
    tree = [Vertex(w) for w in map(int, input().split())]
    for i in range(1, size):
        a, b = list(map(int, input().split()))
        tree[a - 1].children.append(b - 1)
        tree[b - 1].children.append(a - 1)
    return tree


# вычисляем максимальное значение fun фактора для дерева с корнем в вершине vertex,
# так как идем с низу вверх используем значение уже посчитанных вершин.
# Для листьтев дерева максимальный фан фактор равен фан фактору листа
def funParty(vertex, parent):
    global D
    if D[vertex] == 10**9:
        if tree[vertex].children == [parent]:
            D[vertex] = tree[vertex].weight
        else:
            m = tree[vertex].weight
            for u in tree[vertex].children:
                if u != parent:
                    for w in tree[u].children:
                        if D[w] != 10**9:
                            m += D[w]
            m2 = 0
            for u in tree[vertex].children:
                if u != parent:
                    m2 += D[u]
            D[vertex] = max(m, m2)
    return D[vertex]


# перебираем вершины с помощью dfs.
# для каждой вершины (начиная с нижних) выполняем функцию funParty, которая
# считает максимальное значение fun фактора для поддерева с корнем в этой вершине
def dfs(tree, vertex, parent):
    global visited
    visited[vertex] = True
    for child in tree[vertex].children:
        if not visited[child] and child != parent:
            dfs(tree, child, vertex)
    funParty(vertex, parent)


def MaxWeightIndependentTreeSubset(tree):
    dfs(tree, 0, -1)
    # возвращает значение фан фактора для корня дерева
    return D[0]


def main():
    weight = MaxWeightIndependentTreeSubset(tree)
    print(weight)


tree = ReadTree()
size = len(tree)
D = [10**9 for i in range(size)]
visited = [False for i in range(size)]
# This is to avoid stack overflow issues
threading.Thread(target=main).start()
