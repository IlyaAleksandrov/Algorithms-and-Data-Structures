# Task. The goal in this code problem is to implement the binary search algorithm.

# Input Format. The first line of the input contains an integer 𝑛 and a sequence 𝑎0 < 𝑎1 < . . . < 𝑎𝑛−1 of
# 𝑛 pairwise distinct positive integers in increasing order. The next line contains an integer 𝑘 and 𝑘
# positive integers 𝑏0, 𝑏1, . . . , 𝑏𝑘−1.

# Constraints. 1 ≤ 𝑛, 𝑘 ≤ 105; 1 ≤ 𝑎𝑖 ≤ 109 for all 0 ≤ 𝑖 < 𝑛; 1 ≤ 𝑏𝑗 ≤ 109 for all 0 ≤ 𝑗 < 𝑘;

# Output Format. For all 𝑖 from 0 to 𝑘 − 1, output an index 0 ≤ 𝑗 ≤ 𝑛 − 1 such that 𝑎𝑗 = 𝑏𝑖 or −1 if there
# is no such index.

import sys


def binary_search(a, x, left, right):

    # Сравниваем центральный элемент последовательности с искомым элементом и т.к.последоательность упорядоченая,
    # отбрасываем половину последовательности где элемента быть не может.
    if right < left:
        return - 1
    # номер центрального элемента
    mid = left + (right - left) // 2
    # в случае совпадения возвращаем номер ЦЭ
    if x == a[mid]:
        return mid
    elif x < a[mid]:
        return binary_search(a, x, left, mid - 1)
    else:
        return binary_search(a, x, mid + 1, right)


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1: n + 1]
    for x in data[n + 2:]:
        print(binary_search(a, x,  0, len(a) - 1), end=' ')
