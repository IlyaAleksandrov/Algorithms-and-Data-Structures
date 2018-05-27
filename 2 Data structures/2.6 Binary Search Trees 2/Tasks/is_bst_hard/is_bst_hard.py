# Problem Introduction
# In this problem you are going to solve the same problem as the previous one, but for a more general case,
# when binary search tree may contain equal keys.

# Task. You are given a binary tree with integers as its keys. You need to test whether it is a correct binary
# search tree. Note that there can be duplicate integers in the tree, and this is allowed. The definition of
# the binary search tree in such case is the following: for any node of the tree, if its key is 𝑥, then for any
# node in its left subtree its key must be strictly less than 𝑥, and for any node in its right subtree its key
# must be greater than or equal to 𝑥. In other words, smaller elements are to the left, bigger elements
# are to the right, and duplicates are always to the right. You need to check whether the given binary
# tree structure satisfies this condition. You are guaranteed that the input contains a valid binary tree.
# That is, it is a tree, and each node has at most two children.

# Input Format. The first line contains the number of vertices 𝑛. The vertices of the tree are numbered
# from 0 to 𝑛 − 1. Vertex 0 is the root.
# The next 𝑛 lines contain information about vertices 0, 1, ..., 𝑛−1 in order. Each of these lines contains
# three integers 𝑘𝑒𝑦𝑖, 𝑙𝑒𝑓𝑡𝑖 and 𝑟𝑖𝑔ℎ𝑡𝑖 — 𝑘𝑒𝑦𝑖 is the key of the 𝑖-th vertex, 𝑙𝑒𝑓𝑡𝑖 is the index of the left
# child of the 𝑖-th vertex, and 𝑟𝑖𝑔ℎ𝑡𝑖 is the index of the right child of the 𝑖-th vertex. If 𝑖 doesn’t have
# left or right child (or both), the corresponding 𝑙𝑒𝑓𝑡𝑖 or 𝑟𝑖𝑔ℎ𝑡𝑖 (or both) will be equal to −1.

# Constraints. 0 ≤ 𝑛 ≤ 105; −231 ≤ 𝑘𝑒𝑦𝑖 ≤ 231 − 1; −1 ≤ 𝑙𝑒𝑓𝑡𝑖, 𝑟𝑖𝑔ℎ𝑡𝑖 ≤ 𝑛 − 1. It is guaranteed that the
# input represents a valid binary tree. In particular, if 𝑙𝑒𝑓𝑡𝑖 ̸= −1 and 𝑟𝑖𝑔ℎ𝑡𝑖 ̸= −1, then 𝑙𝑒𝑓𝑡𝑖 ̸= 𝑟𝑖𝑔ℎ𝑡𝑖.
# Also, a vertex cannot be a child of two different vertices. Also, each vertex is a descendant of the root
# vertex. Note that the minimum and the maximum possible values of the 32-bit integer type are allowed
# to be keys in the tree — beware of integer overflow!

# Output Format. If the given binary tree is a correct binary search tree (see the definition in the problem
# description), output one word “CORRECT” (without quotes). Otherwise, output one word “INCORRECT”
# (without quotes).

import sys, threading

sys.setrecursionlimit(10 ** 7)  # max depth of recursion
threading.stack_size(2 ** 27)   # new thread will get stack of such size


# The essence of the approach is that in bsd with inorder tree traversal,
# the node processed earlier can not be larger than the node processed later.
def IsBinarySearchTree(tree):
    def inorder_recursive(node):
        if node[1] == -1 and node[2] == -1:
            result.append(node)
        else:
            if node[1] != -1:
                inorder_recursive(tree[node[1]])
            result.append(node)
            if node[2] != -1:
                inorder_recursive(tree[node[2]])
        return True

    if len(tree) == 0:
        return True
    result = []
    inorder_recursive(tree[0])
    for i in range(1, len(result)):
        if result[i][0] < result[i-1][0]:
            return False
        # added check for equality of the node with its right child (task condition)
        elif result[i][0] == result[i-1][0] and result[i - 1][0] == tree[result[i][1]][0] and result[i][1] != -1:
            return False
    return True


def main():
    nodes = int(sys.stdin.readline().strip())
    tree = []
    for i in range(nodes):
        tree.append(list(map(int, sys.stdin.readline().strip().split())))
    if IsBinarySearchTree(tree):
        print("CORRECT")
    else:
        print("INCORRECT")


threading.Thread(target=main).start()
# Example of input:
# 3
# 2 1 2
# 2 -1 -1
# 3 -1 -1
# Output:
# INCORRECT

# The key of the left child of the root must be strictly smaller than the key of the root
