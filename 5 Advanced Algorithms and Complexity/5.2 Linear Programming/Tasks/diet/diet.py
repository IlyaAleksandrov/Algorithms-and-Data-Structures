# Problem Introduction
# In this problem, you will implement an algorithm for solving linear programming
# with only a few inequalities and apply it to determine the
# optimal diet.

# Task. You want to optimize your diet: that is, make sure that your diet satisfies all the recommendations
# of nutrition experts, but you also get maximum pleasure from your food and drinks. For each dish
# and drink you know all the nutrition facts, cost of one item, and an estimation of how much you like
# it. Your budget is limited, of course. The recommendations are of the form “total amount of calories
# consumed each day should be at least 1000” or “the amount of water you drink in liters should be at
# least twice the amount of food you eat in kilograms”, and so on. You optimize the total pleasure which
# is the sum of pleasure you get from consuming each particular dish or drink, and that is proportional
# to the amount amount𝑖 of that dish or drink consumed.
# The budget restriction and the nutrition recommendations can be converted into a system of linear
# inequalities like (sum from i = 1 to m)cost𝑖 · amount𝑖 ≤ Budget, amount𝑖 ≥ 1000 and amount𝑖 − 2 · amount𝑗 ≥ 0, where
# amount𝑖 is the amount of 𝑖-th dish or drink consumed, cost𝑖 is the cost of one item of 𝑖-th dish or
# drink, and 𝐵𝑢𝑑𝑔𝑒𝑡 is your total budget for the diet. Of course, you can only eat a non-negative amount
# amount𝑖 of 𝑖-th item, so amount𝑖 ≥ 0. The goal to maximize total pleasure is reduced to the linear
# objective (sum from i = 1 to m)amount𝑖 · pleasure𝑖 → max where pleasure𝑖 is the pleasure you get after consuming one
# unit of 𝑖-th dish or drink (some dishes like fish oil you don’t like at all, so pleasure𝑖 can be negative).
# Combined, all this is a linear programming problem which you need to solve now.

# Input Format. The first line of the input contains integers 𝑛 and 𝑚 — the number of restrictions on your
# diet and the number of all available dishes and drinks respectively. The next 𝑛 + 1 lines contain the
# coefficients of the linear inequalities in the standard form 𝐴𝑥 ≤ 𝑏, where 𝑥 = amount is the vector of
# length 𝑚 with amounts of each ingredient, 𝐴 is the 𝑛×𝑚 matrix with coefficients of inequalities and 𝑏
# is the vector with the right-hand side of each inequality. Specifically, 𝑖-th of the next 𝑛 lines contains
# 𝑚 integers 𝐴𝑖1,𝐴𝑖2, . . . ,𝐴𝑖𝑚, and the next line after those 𝑛 contains 𝑛 integers 𝑏1, 𝑏2, . . . , 𝑏𝑛. These
# lines describe 𝑛 inequalities of the form 𝐴𝑖1 · amount1 + 𝐴𝑖2 · amount2 + · · · + 𝐴𝑖𝑚 · amount𝑚 ≤ 𝑏𝑖.
# The last line of the input contains 𝑚 integers — the pleasure for consuming one item of each dish and
# drink pleasure1, pleasure2, . . . , pleasure𝑚.

# Constraints. 1 ≤ 𝑛,𝑚 ≤ 8; −100 ≤ 𝐴𝑖𝑗 ≤ 100; −1 000 000 ≤ 𝑏𝑖 ≤ 1 000 000; −100 ≤ cost𝑖 ≤ 100.

# Output Format. If there is no diet that satisfies all the restrictions, output “No solution” (without quotes).
# If you can get as much pleasure as you want despite all the restrictions, output “Infinity” (without
# quotes). If the maximum possible total pleasure is bounded, output two lines. On the first line, output
# “Bounded solution” (without quotes). On the second line, output 𝑚 real numbers — the optimal
# amounts for each dish and drink. Output all the numbers with at least 15 digits after the decimal
# point.
# The amounts you output will be inserted into the inequalities, and all the inequalities will be checked.
# An inequality 𝐿 ≤ 𝑅 will be considered satisfied if actually 𝐿 ≤ 𝑅 + 10^−3. The total pleasure of your
# solution will be calculated and compared with the optimal value. Your output will be accepted if all
# the inequalities are satisfied and the total pleasure of your solution differs from the optimal value by
# at most 10^−3. We ask you to output at least 15 digits after the decimal point, although
# we will check the answer with precision of only 10^−3. This is because in the process of
# checking the inequalities we will multiply your answers with coefficients from the matrix
# 𝐴 and with the coefficients of the vector pleasure, and those coefficients can be pretty
# large, and computations with real numbers on a computer are not always precise. This
# way, the more digits after the decimal point you output for each amount — the less likely
# it is that your answer will be rejected because of precision issues.

from sys import stdin
import itertools
import copy


class Equation:
    def __init__(self, a, b):
        self.a = a
        self.b = b


class Position:
    def __init__(self, column, row):
        self.column = column
        self.row = row


def ReadEquation():
    size = int(input())
    a = []
    b = []
    for row in range(size):
        line = list(map(float, input().split()))
        a.append(line[:size])
        b.append(line[size])
    return Equation(a, b)


def SelectPivotElement(a, used_rows, used_columns):
    pivot_element = Position(0, 0)
    while used_rows[pivot_element.row]:
        pivot_element.row += 1
    while used_columns[pivot_element.column]:
        pivot_element.column += 1
    if a[pivot_element.row][pivot_element.column] == 0:
        global flagSwap
        global flagExit
        flagSwap = True
        s = pivot_element.row
        while a[pivot_element.row][pivot_element.column] == 0:
            pivot_element.row += 1
            if pivot_element.row > len(a) - 1:
                pivot_element.column += 1
                pivot_element.row = s
                if pivot_element.column > len(a[0]) - 1:
                    flagExit = True
                    break
    return pivot_element


def SwapLines(a, b, used_rows, pivot_element):
    used_rows_num = 0
    while used_rows[used_rows_num]:
        used_rows_num += 1
    a[pivot_element.row], a[used_rows_num] = a[used_rows_num], a[pivot_element.row]
    b[pivot_element.row], b[used_rows_num] = b[used_rows_num], b[pivot_element.row]
    pivot_element.row = used_rows_num
    global flagSwap
    flagSwap = False


def ProcessPivotElement(a, b, pivot_element):
    num = a[pivot_element.row][pivot_element.column]
    for i in range(len(a[pivot_element.row])):
        a[pivot_element.row][i] /= num
    if b[pivot_element.row] != 0:
        b[pivot_element.row] /= num
    for i in range(len(a)):
        h = a[i]
        if i == pivot_element.row:
            continue
        if h[pivot_element.column] != 0:
            numrow = h[pivot_element.column]
            for j in range(len(h)):
                h[j] -= a[pivot_element.row][j] * numrow
            b[i] -= b[pivot_element.row] * numrow
    pass


def MarkPivotElementUsed(pivot_element, used_rows, used_columns):
    used_rows[pivot_element.row] = True
    used_columns[pivot_element.column] = True


def SolveEquation(equation):
    a = copy.deepcopy(equation.a)
    b = copy.deepcopy(equation.b)
    size = len(a)
    global flagSwap
    global flagExit
    flagExit = False
    used_columns = [False] * (size)
    used_rows = [False] * (size)
    for step in range(size):
        pivot_element = SelectPivotElement(a, used_rows, used_columns)
        if flagExit:
            return [-1 for i in range(m)]
        if flagSwap:
            SwapLines(a, b, used_rows, pivot_element)
        ProcessPivotElement(a, b, pivot_element)
        MarkPivotElementUsed(pivot_element, used_rows, used_columns)

    return b


def test(solution, A, b):
    for i in range(len(A)):
        sum = 0
        for j in range(len(A[i])):
            sum += A[i][j] * solution[j]
        if sum - b[i] > 1e-4:
            return False
    return True


# the task uses implementation of Gaussian Elimination from the previous task (energy values)
def solve_diet_problem(n, m, A, b, c):
    # we create a set of all variants of intersection of equations of dimension m (number of variables)
    set_interseption = itertools.combinations([i for i in range(n + m + 1)], m)
    maximum = -10**9
    bestSolution = []
    # for each intersection we apply the Gaus method from the previous task (energy values)
    for i in set_interseption:
        Aevac = []
        bEvac = []
        for j in i:
            Aevac.append(A[j])
            bEvac.append(b[j])
        equation = Equation(Aevac, bEvac)
        solution = SolveEquation(equation)
        ans = 0
        for s in range(m):
            ans += c[s]*solution[s]
        # test the solution of the equation for other conditions
        if test(solution, A, b):
            if ans >= maximum:
                maximum = ans
                bestSolution = solution
                infTest = i
    if bestSolution == []:
        return -1, []
    # if the best solution contains the equation n
    # (the equation for verifying the existence of an infinite solution see line 212)
    # means the solution is unlimited
    elif n in infTest:
         return 1, []
    else:
        return 0, bestSolution


# the solution is that we take all the points of intersection of the equations and check their optimality
flagSwap = False
flagExit = False
n, m = list(map(int, stdin.readline().split()))
A = []
for i in range(n):
    A += [list(map(int, stdin.readline().split()))]
b = list(map(int, stdin.readline().split()))
c = list(map(int, stdin.readline().split()))
# we add an equation for testing the existence of an infinite solution (x + y + ... + z <inf)
A.append([1 for i in range(m)])
b.append(10 ** 9)
# add equations for each variable (the variable is greater than zero)
for i in range(m):
    s = [0 for i in range(m)]
    s[i] = -1
    A.append(s)
    b.append(0)


anst, ansx = solve_diet_problem(n, m, A, b, c)


if anst == -1:
    print("No solution")
if anst == 0:
    print("Bounded solution")
    print(' '.join(list(map(lambda x: '%.18f' % x, ansx))))
if anst == 1:
    print("Infinity")
# Example of input:
# 1 3
# 0 0 1
# 3
# 1 1 1
# Output:
# Infinity
# Explanation:
# The restrictions in this case are only that all amounts are non-negative (these restrictions are always
# there, because you cannot consume negative amount of a dish or a drink) and that amount3 ≤ 3. There
# is no restriction on how much to consume of items 1 and 2, and each of them has positive pleasure
# value, so you can take as much of items 1 and 2 as you want and receive as much total pleasure as you
# want. In this case, you should output “Infinite” (without quotes).
