# Problem Introduction
# In this problem, you will learn to reduce the real-world problem about
# assigning frequencies to the transmitting towers of the cells in a GSM
# network to a problem of proper coloring a graph into 3 colors. Then you
# will design and implement an algorithm to reduce this problem to an
# instance of SAT.

# Task. GSM network is a type of infrastructure used for communication via mobile phones. It includes
# transmitting towers scattered around the area which operate in different frequencies. Typically there is
# one tower in the center of each hexagon called “cell” on the grid above — hence the name “cell phone”.
# A cell phone looks for towers in the neighborhood and decides which one to use based on strength
# of signal and other properties. For a phone to distinguish among a few closest towers, the frequencies
# of the neighboring towers must be different. You are working on a plan of GSM network for mobile,
# and you have a restriction that you’ve only got 3 different frequencies from the government which you
# can use in your towers. You know which pairs of the towers are neighbors, and for all such pairs the
# towers in the pair must use different frequencies. You need to determine whether it is possible to assign
# frequencies to towers and satisfy these restrictions.
# This is equivalent to a classical graph coloring problem: in other words, you are given a graph, and
# you need to color its vertices into 3 different colors, so that any two vertices connected by an edge
# need to be of different colors. Colors correspond to frequencies, vertices correspond to cells, and edges
# connect neighboring cells. Graph coloring is an NP-complete problem, so we don’t currently know an
# efficient solution to it, and you need to reduce it to an instance of SAT problem which, although it is
# NP-complete, can often be solved efficiently in practice using special programs called SAT-solvers.

# Input Format. The first line of the input contains integers 𝑛 and 𝑚 — the number of vertices and edges in
# the graph. The vertices are numbered from 1 through 𝑛. Each of the next 𝑚 lines contains two integers
# 𝑢 and 𝑣 — the numbers of vertices connected by an edge. It is guaranteed that a vertex cannot be
# connected to itself by an edge.

# Constraints. 2 ≤ 𝑛 ≤ 500; 1 ≤ 𝑚 ≤ 1000; 1 ≤ 𝑢, 𝑣 ≤ 𝑛; 𝑢 ̸= 𝑣.

# Output Format. You need to output a boolean formula in the conjunctive normal form (CNF) in a specific
# format. If it is possible to color the vertices of the input graph in 3 colors such that any two vertices
# connected by an edge are of different colors, the formula must be satisfiable. Otherwise, the formula
# must be unsatisfiable. The number of variables in the formula must be at least 1 and at most 3000.
# The number of clauses must be at least 1 and at most 5000.
# On the first line, output integers 𝐶 and 𝑉 — the number of clauses in the formula and the number of
# variables respectively. On each of the next 𝐶 lines, output a description of a single clause. Each clause
# has a form (𝑥4 𝑂𝑅 𝑥1 𝑂𝑅 𝑥8). For a clause with 𝑘 terms (in the example, 𝑘 = 3 for 𝑥4, 𝑥1 and 𝑥8), output
# first those 𝑘 terms and then number 0 in the end (in the example, output “4 − 1 8 0”). Output each
# term as integer number. Output variables 𝑥1, 𝑥2, . . . , 𝑥𝑉 as numbers 1, 2, . . . , 𝑉 respectively. Output
# negations of variables 𝑥1, 𝑥2, . . . , 𝑥𝑉 as numbers −1,−2, . . . ,−𝑉 respectively. Each number other than
# the last one in each line must be a non-zero integer between −𝑉 and 𝑉 where 𝑉 is the total number
# of variables specified in the first line of the output. Ensure that 1 ≤ 𝐶 ≤ 5000 and 1 ≤ 𝑉 ≤ 3000.
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


# на выход нужно предоставить набор условий
# в случае если у условий есть единое решение, то вся задача будет иметь решение
# для решения строится сетка Xij - конкретная вершина имеет конкретный цвет
# Примеры:
# X11 X12 X13 - условие означает что вершина должна иметь минимум один цвет (все 3 переменных не могут быть равны 0)
# (-X11 -X12) (-X11 -X13) (-X12 -X13) - вершины не могут иметь два цвета
# (если две переменных будут true то условие не выполнится)

def varnum(i, j):
    return i + (j - 1)*n


# добавление условий "только один" (вершины не могут иметь два цвета)
def exactly_one_of(literals):
    clauses.append([l for l in literals])

    for pair in itertools.combinations(literals, 2):
        clauses.append([-l for l in pair])


# вывод всех условий
def printEquisatisfiableSatFormula():
    print(n * 4 + m * 3, n * 3)
    for i in clauses:
        for j in range(len(i)):
            print(i[j], end=" ")
        print(0)


n, m = map(int, input().split())
edges = [list(map(int, input().split())) for i in range(m)]

clauses = []

digits = range(1, 4)

for i in range(n):
    exactly_one_of([varnum(i + 1, j) for j in digits])

for j in edges:
    for r in digits:
        clauses.append([-varnum(j[0], r), -varnum(j[1], r)])

printEquisatisfiableSatFormula()
