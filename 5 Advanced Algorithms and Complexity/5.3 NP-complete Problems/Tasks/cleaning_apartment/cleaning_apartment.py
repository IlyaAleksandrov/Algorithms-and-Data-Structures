# Problem Introduction
# In this problem, you will learn to determine whether it is possible to
# clean an apartment after a party without leaving any traces of the party.
# You will learn how to reduce it to the classic Hamiltonian Path problem,
# and then you will design and implement an efficient algorithm to reduce
# it to SAT.

# Task. You’ve just had a huge party in your parents’ house, and they are returning tomorrow. You need
# to not only clean the apartment, but leave no trace of the party. To do that, you need to clean all
# the rooms in some order. After finishing a thorough cleaning of some room, you cannot return to it
# anymore: you are afraid you’ll ruin everything accidentally and will have to start over. So, you need to
# move from room to room, visit each room exactly once and clean it. You can only move from a room
# to the neighboring rooms. You want to determine whether this is possible at all.
# This can be reduced to a classic Hamiltonian Path problem: given a graph, determine whether there is
# a route visiting each vertex exactly once. Rooms are vertices of the graph, and neighboring rooms are
# connected by edges. Hamiltonian Path problem is NP-complete, so we don’t know an efficient algorithm
# to solve it. You need to reduce it to SAT, so that it can be solved efficiently by a SAT-solver.

# Input Format. The first line contains two integers 𝑛 and 𝑚 — the number of rooms and the number of
# corridors connecting the rooms respectively. Each of the next 𝑚 lines contains two integers 𝑢 and 𝑣
# describing the corridor going from room 𝑢 to room 𝑣. The corridors are two-way, that is, you can go
# both from 𝑢 to 𝑣 and from 𝑣 to 𝑢. No two corridors have a common part, that is, every corridor only
# allows you to go from one room to one other room. Of course, no corridor connects a room to itself.
# Note that a corridor from 𝑢 to 𝑣 can be listed several times, and there can be listed both a corridor
# from 𝑢 to 𝑣 and a corridor from 𝑣 to 𝑢.

# Constraints. 1 ≤ 𝑛 ≤ 30; 0 ≤ 𝑚 ≤ 𝑛(𝑛−1)
# 2 ; 1 ≤ 𝑢, 𝑣 ≤ 𝑛.

# Output Format. You need to output a boolean formula in the CNF form in a specific format. If it is
# possible to go through all the rooms and visit each one exactly once to clean it, the formula must be
# satisfiable. Otherwise, the formula must be unsatisfiable. The sum of the numbers of variables used in
# each clause of the formula must not exceed 120 000.
# On the first line, output integers 𝐶 and 𝑉 — the number of clauses in the formula and the number of
# variables respectively. On each of the next 𝐶 lines, output a description of a single clause. Each clause
# has a form (𝑥4 𝑂𝑅 𝑥1 𝑂𝑅 𝑥8). For a clause with 𝑘 terms (in the example, 𝑘 = 3 for 𝑥4, 𝑥1 and 𝑥8), output
# first those 𝑘 terms and then number 0 in the end (in the example, output “4 − 1 8 0”). Output each
# term as integer number. Output variables 𝑥1, 𝑥2, . . . , 𝑥𝑉 as numbers 1, 2, . . . , 𝑉 respectively. Output
# negations of variables 𝑥1, 𝑥2, . . . , 𝑥𝑉 as numbers −1,−2, . . . ,−𝑉 respectively. Each number other than
# the last one in each line must be a non-zero integer between −𝑉 and 𝑉 where 𝑉 is the total number
# of variables specified in the first line of the output. Ensure that the total number of non-zero integers
# in the 𝐶 lines describing the clauses is at most 120 000.
# See the examples below for further clarification of the output format.
# If there are many different formulas that satisfy the requirements above, you can output any one of
# them.
# Note that your formula will be checked internally by the grader using a SAT-solver.
# Although SAT-solvers often solve instances of SAT of the given size very fast, it cannot
# be guaranteed. If you submit a formula which cannot be resolved by the SAT-solver we
# use under a reasonable time limit, the grader will timeout, and the problem won’t pass.
# We guarantee that there are solutions of this problem that output formulas which are
# resolved almost instantly by the SAT-solver used. However, don’t try to intentionally
# break the system by submitting very complex SAT instances, because the problem still
# won’t pass, and you will violate Coursera Honor Code by doing that.
import itertools

# задача идентична предидущей: формируем набор условий (см. gsm network)
n, m = map(int, input().split())
edges = [list(map(int, input().split())) for i in range(m)]
adj = [[] for _ in range(n)]
for (a, b) in edges:
    adj[a - 1].append(b)
    adj[b - 1].append(a)

clauses = []
digits = range(1, n + 1)


def varnum(i, j):
    return i + (j - 1)*n
    # return i*10 + j


def exactly_one_of(literals):
    clauses.append([l for l in literals])

    for pair in itertools.combinations(literals, 2):
        clauses.append([-l for l in pair])


for i in range(n):
    exactly_one_of([varnum(i + 1, j) for j in digits])

for j in range(n):
    exactly_one_of([varnum(i, j + 1) for i in digits])

listOfNonAdj = [[] for _ in range(n)]

for i in range(n):
    for j in range(n - 1):
        clauses.append([-varnum(j + 1, i + 1)] + [varnum(j + 2, z) for z in adj[i]])


def printEquisatisfiableSatFormula():
    print(len(clauses), n * n)
    for i in clauses:
        for j in range(len(i)):
            print(i[j], end=" ")
        print(0)


printEquisatisfiableSatFormula()
