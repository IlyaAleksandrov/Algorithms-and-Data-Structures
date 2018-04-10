# Problem Description
# Task. You’re looking into a restaurant menu which shows for each dish the list of ingredients with amounts
# and the estimated total energy value in calories. You would like to find out the energy values of
# individual ingredients (then you will be able to estimate the total energy values of your favorite dishes).

# Input Format. The first line of the input contains an integer 𝑛 — the number of dishes in the menu, and
# it happens so that the number of different ingredients is the same. Each of the next 𝑛 lines contains
# description 𝑎1, 𝑎2, . . . , 𝑎𝑛,𝐸 of a single menu item. 𝑎𝑖 is the amount of 𝑖-th ingredient in the dish,
# and 𝐸 is the estimated total energy value of the dish. If the ingredient is not used in the dish, the
# amount will be specified as 𝑎𝑖 = 0; beware that although the amount of any ingredient in any
# real menu would be positive, we will test that your algorithm works even for negative
# amounts 𝑎𝑖 < 0.

# Constraints. 0 ≤ 𝑛 ≤ 20; −1000 ≤ 𝑎𝑖 ≤ 1000.

# Output Format. Output 𝑛 real numbers — for each ingredient, what is its energy value. These numbers
# can be non-integer, so output them with at least 3 digits after the decimal point.

# Your output for a particular test input will be accepted if all the numbers in the output are considered
# correct. The amounts and energy values are of course approximate, and the computations in real
# numbers on a computer are not always precise, so each of the numbers in your output will be considered
# correct if either absolute or relative error is less than 10−2. That is, if the correct number is 5.245000,
# and you output 5.235001, your number will be considered correct, but 5.225500 will not be accepted.
# Also, if the correct number is 1001, and you output 1000, your answer will be considered correct,
# because the relative error will be less than 10−2, but if the correct answer is 0.1, and you output 0.05,
# your answer will not be accepted, because in this case both the absolute error (0.05) and the relative
# error (0.5) are more than 10−2. Note that we ask you to output at least 3 digits after the
# decimal point, although we only require precision of 10−2, intentionally: if you output
# only 2 digits after the decimal point, your answer can be rejected while being correct
# because of the rounding issues. The easiest way to avoid this mistake is to output at least
# 3 digits after the decimal point.


EPS = 1e-6
PRECISION = 20


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
        flagSwap = True
        while a[pivot_element.row][pivot_element.column] == 0:
            s = pivot_element.row
            pivot_element.row += 1
            if pivot_element.row > len(a):
                pivot_element.column += 1
                pivot_element.row = s
                if pivot_element.column > len(a[0]):
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


# реализация метода Гауса для решения уравнений
def SolveEquation(equation):
    a = equation.a
    b = equation.b
    size = len(a)
    global flagSwap
    used_columns = [False] * (size)
    used_rows = [False] * (size)
    # для каждого уравнения выполняем следующие действия
    for step in range(size):
        # выбираем элемент (первый ненулевой элемент в необработаной области)
        pivot_element = SelectPivotElement(a, used_rows, used_columns)
        # при необходимости меняем строки местами(если элемент равен 0)
        if flagSwap:
            SwapLines(a, b, used_rows, pivot_element)
        # выполняем преобразования таблицы с использованием выбраного элемента
        ProcessPivotElement(a, b, pivot_element)
        # отмечаем выбраное уравнение обработанным
        MarkPivotElementUsed(pivot_element, used_rows, used_columns)

    return b


def PrintColumn(column):
    size = len(column)
    for row in range(size):
        print("%.20lf" % column[row])


if __name__ == "__main__":
    equation = ReadEquation()
    flagSwap = False
    if equation != 0:
        solution = SolveEquation(equation)
        PrintColumn(solution)
    exit(0)

