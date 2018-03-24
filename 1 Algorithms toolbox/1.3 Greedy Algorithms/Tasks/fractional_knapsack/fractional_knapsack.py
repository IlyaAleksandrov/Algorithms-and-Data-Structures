# Task. The goal of this code problem is to implement an algorithm for the fractional knapsack problem.

# Input Format. The first line of the input contains the number 𝑛 of items and the capacity 𝑊 of a knapsack.
# The next 𝑛 lines define the values and weights of the items. The 𝑖-th line contains integers 𝑣𝑖 and 𝑤𝑖—the
# value and the weight of 𝑖-th item, respectively.

# Constraints. 1 ≤ 𝑛 ≤ 103, 0 ≤ 𝑊 ≤ 2 · 106; 0 ≤ 𝑣𝑖 ≤ 2 · 106, 0 < 𝑤𝑖 ≤ 2 · 106 for all 1 ≤ 𝑖 ≤ 𝑛. All the
# numbers are integers.

# Output Format. Output the maximal value of fractions of items that fit into the knapsack. The absolute
# value of the difference between the answer of your program and the optimal value should be at most
# 10−3. To ensure this, output your answer with at least four digits after the decimal point (otherwise
# your answer, while being computed correctly, can turn out to be wrong because of rounding issues).

import sys


def get_optimal_value(capacity, weights, values):
    value = 0
    lst = []
    # Заполняем список ценностью каждой вещи за 1 кг
    for i in range(len(weights)):
        lst.append([values[i] / weights[i], i])
    # Сортируем список от самой дорогой к менее
    lst.sort(reverse=True)
    # Начиная с самой дорогой вещи пробуем положить её целиком в рюкзак
    # Если не помещается, берем сколько можем и завершаем перебор
    for j in range(len(lst)):
        if weights[lst[j][1]] <= capacity:
            capacity -= weights[lst[j][1]]
            value += values[lst[j][1]]
        else:
            value += capacity/weights[lst[j][1]] * values[lst[j][1]]
            break
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
