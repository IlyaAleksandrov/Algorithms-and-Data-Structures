# Problem Introduction
# In the previous problem, we introduced the Burrows–Wheeler transform of a string Text. It permutes the
# symbols of Text making it well compressible. However, there were no sense in this, if this process would
# not be reversible. It turns out that it is reversible, and your goal in this problem is to recover Text from
# BWT(Text).

# Task. Reconstruct a string from its Burrows–Wheeler transform.

# Input Format. A string Transform with a single “$” sign.

# Constraints. 1 ≤ |Transform| ≤ 1 000 000; except for the last symbol, Text contains symbols A, C, G, T
# only.

# Output Format. The string Text such that BWT(Text) = Transform. (There exists a unique such string.)

import sys


# возврат строки, после преобразования прошлой задачи
def InverseBWT(bwt):
    n = len(bwt)
    # сортируем символы по алфавиту
    first = [i for i in bwt]
    first.sort()
    matrix = [0 for i in range(n)]
    # заполняем матрицу, каждой строке по индексу присваиваем
    # значение из сортировки по алфавиту и изначальной BWT строки
    for i in range(n):
        matrix[i] = [i, first[i], bwt[i]]
    # сортируем строки матрицы по символам bwt сироки
    matrix.sort(key=lambda i: i[2])
    result = []
    # после сортировки, упорядоченая последовательность индексов в столбце 0 поменялась и приняла нужную нам форму
    # берем индексы исходя из представленого алгоритма и добавляем в ответ соответствующий символ исходой строки
    t = matrix[0][0]
    for i in range(n):
        t = matrix[t][0]
        result.append(bwt[t])
    return result


if __name__ == '__main__':
    bwt = sys.stdin.readline().strip()
    print(*InverseBWT(bwt), sep="")