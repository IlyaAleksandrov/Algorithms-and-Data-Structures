# Problem Introduction
# In this problem you will implement in-order, pre-order and post-order traversals of a binary tree. These
# traversals were defined in the week 1 lecture on tree traversals, but it is very useful to practice implementing
# them to understand binary search trees better.

# Task. You are given a rooted binary tree. Build and output its in-order, pre-order and post-order traversals.

# Input Format. The first line contains the number of vertices 𝑛. The vertices of the tree are numbered
# from 0 to 𝑛 − 1. Vertex 0 is the root.
# The next 𝑛 lines contain information about vertices 0, 1, ..., 𝑛−1 in order. Each of these lines contains
# three integers 𝑘𝑒𝑦𝑖, 𝑙𝑒𝑓𝑡𝑖 and 𝑟𝑖𝑔ℎ𝑡𝑖 — 𝑘𝑒𝑦𝑖 is the key of the 𝑖-th vertex, 𝑙𝑒𝑓𝑡𝑖 is the index of the left
# child of the 𝑖-th vertex, and 𝑟𝑖𝑔ℎ𝑡𝑖 is the index of the right child of the 𝑖-th vertex. If 𝑖 doesn’t have
# left or right child (or both), the corresponding 𝑙𝑒𝑓𝑡𝑖 or 𝑟𝑖𝑔ℎ𝑡𝑖 (or both) will be equal to −1.

# Constraints. 1 ≤ 𝑛 ≤ 105; 0 ≤ 𝑘𝑒𝑦𝑖 ≤ 109; −1 ≤ 𝑙𝑒𝑓𝑡𝑖, 𝑟𝑖𝑔ℎ𝑡𝑖 ≤ 𝑛 − 1. It is guaranteed that the input
# represents a valid binary tree. In particular, if 𝑙𝑒𝑓𝑡𝑖 ̸= −1 and 𝑟𝑖𝑔ℎ𝑡𝑖 ̸= −1, then 𝑙𝑒𝑓𝑡𝑖 ̸= 𝑟𝑖𝑔ℎ𝑡𝑖. Also,
# a vertex cannot be a child of two different vertices. Also, each vertex is a descendant of the root vertex.

# Output Format. Print three lines. The first line should contain the keys of the vertices in the in-order
# traversal of the tree. The second line should contain the keys of the vertices in the pre-order traversal
# of the tree. The third line should contain the keys of the vertices in the post-order traversal of the tree.

import sys, threading

sys.setrecursionlimit(10 ** 6)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size


class TreeOrders:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]

        for i in range(self.n):
            [a, b, c] = map(int, sys.stdin.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c
        self.tree = []
        for i in range(len(self.key)):
            self.tree.append([self.key[i], self.left[i], self.right[i]])

    # во всех видах обходов деревьев мы используем похожий алгоритм, отличия заключаются в порядке рекурсивного вызова
    # дочерних узлов и добавления обрабатываемого узла в итоговый список.
    def inOrder(self):
        def inorder_recursive(node, result):
                # проверяем наличие дочерних узлов
                if node [1] == -1 and node[2] == -1:
                    result.append(node[0])
                # если есть хоть один дочерний узел запускаем рекурсию
                else:
                    if node[1] != -1:
                        inorder_recursive(self.tree[node[1]], result)
                    result.append(node[0])
                    if node[2] != -1:
                        inorder_recursive(self.tree[node[2]], result)

        self.result = []
        inorder_recursive(self.tree[0], self.result)
        return self.result

    def preOrder(self):
        self.result = []
        def preorder_recursive(node, result):
            if node[1] == -1 and node [2] == -1:
                result.append(node[0])
            else:
                result.append(node[0])
                if node[1] != -1:
                    preorder_recursive(self.tree[node[1]], result)
                if node[2] != -1:
                    preorder_recursive(self.tree[node[2]], result)

        self.result = []
        preorder_recursive(self.tree[0], self.result)
        return self.result

    def postOrder(self):
        self.result = []
        def postorder_recursive(node, result):
            if node[1] == -1 and node [2] == -1:
                result.append(node[0])
            else:
                if node[1] != -1:
                    postorder_recursive(self.tree[node[1]], result)
                if node[2] != -1:
                    postorder_recursive(self.tree[node[2]], result)
                result.append(node[0])

        self.result = []
        postorder_recursive(self.tree[0], self.result)
        return self.result


def main():
    tree = TreeOrders()
    tree.read()
    print(" ".join(str(x) for x in tree.inOrder()))
    print(" ".join(str(x) for x in tree.preOrder()))
    print(" ".join(str(x) for x in tree.postOrder()))


threading.Thread(target=main).start()
