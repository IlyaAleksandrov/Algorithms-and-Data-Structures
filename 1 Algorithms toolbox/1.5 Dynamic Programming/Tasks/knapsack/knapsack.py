# Problem Introduction
# This problem is about implementing an algorithm for the knapsack without repetitions problem.

# Task. In this problem, you are given a set of bars of gold and your goal is to take as much gold as possible
# into your bag. There is just one copy of each bar and for each bar you can either take it or not (hence
# you cannot take a fraction of a bar).

# Input Format. The first line of the input contains the capacity W of a knapsack and the number n of bars
# of gold. The next line contains n integers w0;w1; : : : ;wn􀀀1 defining the weights of the bars of gold.

# Constraints. 1  W  104; 1  n  300; 0  w0; : : : ;wn􀀀1  105.

# Output Format. Output the maximum weight of gold that fits into a knapsack of capacity W.
import sys

def optimal_weight(W, w):
    n = len(w)
    # заполняем матрицу n х W (количество взятых первых элементов Х заполеность рюкзака)
    value = [[0 for x in range(n + 1)] for y in range(W + 1)]
    # значения первого столбца и строки оставляем равными 0 (0 вместимось/0 элементов взято)
    for i in range(1, n + 1):
        for j in range(1, W + 1):
            # изначально, присваиваем ячейке значение с текущим размером рюкзака, но без нового элемента
            value[j][i] = value[j][i - 1]
            # если текущая вместимость рюкзака прозволяет принять элемент
            if w[i - 1] <= j:
                # то мы ищем в таблице максимально значение которое мы можем достичь с (i-1) элементами при условии
                # что останется место для нового элемента (текущий рюкзак (j) минус вес нового элемента (w[i - 1]))
                val = value[j - w[i - 1]][i - 1] + w[i - 1]
                # если значение получилось больше изначально присвоенного, принимаем его
                if value[j][i] < val:
                    value[j][i] = val
    # возвращаем значение полученное при максимальной вместимости и использовании всех элементов
    return value[W][n]

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
