# Problem Introduction
# In this problem, you will determine how to connect the modules of an
# integrated circuit with wires so that all the wires can be routed on the
# same layer of the circuit.

# Problem Description
# Task. VLSI or Very Large-Scale Integration is a process of creating an integrated circuit by combining
# thousands of transistors on a single chip. You want to design a single layer of an integrated circuit.
# You know exactly what modules will be used in this layer, and which of them should be connected by
# wires. The wires will be all on the same layer, but they cannot intersect with each other. Also, each
# wire can only be bent once, in one of two directions — to the left or to the right. If you connect two
# modules with a wire, selecting the direction of bending uniquely defines the position of the wire. Of
# course, some positions of some pairs of wires lead to intersection of the wires, which is forbidden. You
# need to determine a position for each wire in such a way that no wires intersect.
# This problem can be reduced to 2-SAT problem — a special case of the SAT problem in which each
# clause contains exactly 2 variables. For each wire 𝑖, denote by 𝑥𝑖 a binary variable which takes value 1
# if the wire is bent to the right and 0 if the wire is bent to the left. For each 𝑖, 𝑥𝑖 must be either 0 or 1.
# Also, some pairs of wires intersect in some positions. For example, it could be so that if wire 1 is bent
# to the left and wire 2 is bent to the right, then they intersect. We want to write down a formula which
# is satisfied only if no wires intersect. In this case, we will add the clause (𝑥1 𝑂𝑅 𝑥2) to the formula
# which ensures that either 𝑥1 (the first wire is bent to the right) is true or 𝑥2 (the second wire is bent
# to the left) is true, and so the particular crossing when wire 1 is bent to the left AND wire 2 is bent to
# the right doesn’t happen whenever the formula is satisfied. We will add such a clause for each pair of
# wires and each pair of their positions if they intersect when put in those positions. Of course, if some
# pair of wires intersects in any pair of possible positions, we won’t be able to design a circuit. Your
# task is to determine whether it is possible, and if yes, determine the direction of bending for each of
# the wires.

# Input Format. The input represents a 2-CNF formula. The first line contains two integers 𝑉 and 𝐶 —
# the number of variables and the number of clauses respectively. Each of the next 𝐶 lines contains two
# non-zero integers 𝑖 and 𝑗 representing a clause in the CNF form. If 𝑖 > 0, it represents 𝑥𝑖, otherwise
# if 𝑖 < 0, it represents !𝑥−𝑖, and the same goes for 𝑗. For example, a line “2 3” represents a clause
# (𝑥2 𝑂𝑅 𝑥3), line “1 -4” represents (𝑥1 𝑂𝑅 !𝑥4), line “-1 -3” represents (𝑥1 𝑂𝑅 𝑥3), and line “0 2”
# cannot happen, because 𝑖 and 𝑗 must be non-zero.

# Constraints. 1 ≤ 𝑉,𝐶 ≤ 1 000 000; −𝑉 ≤ 𝑖, 𝑗 ≤ 𝑉 ; 𝑖, 𝑗 != 0.

# Output Format. If the 2-CNF formula in the input is unsatisfiable, output just the word “UNSATISFIABLE”
# (without quotes, using capital letters). If the 2-CNF formula in the input is satisfiable, output
# the word “SATISFIABLE” (without quotes, using capital letters) on the first line and the corresponding
# assignment of variables on the second line. For each 𝑥𝑖 in order from 𝑥1 to 𝑥𝑉 , output 𝑖 if 𝑥𝑖 = 1
# or −𝑖 if 𝑥𝑖 = 0. For example, if a formula is satisfied by assignment 𝑥1 = 0, 𝑥2 = 1, 𝑥3 = 0,
# output “-1 2 -3” on the second line (without quotes). If there are several possible assignments satisfying
# the input formula, output any one of them.
import sys
import threading

sys.setrecursionlimit(10**7)
threading.stack_size(2**27)


n, m = map(int, input().split())
clauses = [list(map(int, input().split())) for i in range(m)]
count = 0


def isSatisfiable():
    global count

    def dfs1(i):
        visited[i] = True
        for j in gV[i]:
            if not visited[j]:
                dfs1(j)
        postvisit.append(i)

    def dfs2(x):
        global count
        CCS[x] = count
        for j in gReverseV[x]:
            if CCS[j] == -1:
                dfs2(j)

    g = []
    for i in clauses:
        g.append([-i[0], i[1]])
        g.append([-i[1], i[0]])

    lst = list(range(-n, 0)) + list(range(1, n + 1))
    gReverseEdges = []
    gReverseV = {i: [] for i in lst}
    gV = {i: [] for i in lst}
    for i in g:
        gReverseEdges.append([i[1], i[0]])
    for i in gReverseEdges:
        gReverseV[i[0]] += [i[1]]
    gV = {i: [] for i in lst}
    for i in g:
        gV[i[0]] += [i[1]]
    CCS = {i: -1 for i in lst}
    postvisit = []
    visited = {i: False for i in lst}

    for i in lst:
        if not visited[i]:
            dfs1(i)

    postvisit.reverse()
    for i in postvisit:
        if CCS[i] == -1:
            dfs2(i)
            count += 1

    for i in range(1, n + 1):
        if CCS[i] == CCS[-i]:
            return

    result = {i: -1 for i in lst}

    for i in postvisit:
        if result[i] == -1:
            result[i] = 1
            result[-i] = 0

    return result


def main():
    result = isSatisfiable()
    if result is None:
        print("UNSATISFIABLE")
    else:
        print("SATISFIABLE")
        for i in range(1, n + 1):
            if result.get(i) == 1:
                print(-i, end=" ")
            else:
                print(i, end=" ")


threading.Thread(target=main).start()

# Example of input:
# 1 2
# 1 1
# -1 -1

# Output:
# UNSATISFIABLE

# Explanation:
# The input formula is (𝑥1 𝑂𝑅 𝑥1) 𝐴𝑁𝐷 (!𝑥1 𝑂𝑅 !𝑥1), and it is unsatisfiable.
