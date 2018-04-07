# Problem Introduction
# In this problem, we ask a simple question: how many times one string occurs as a substring of another?
# Recall that different occurrences of a substring can overlap with each other. For example, ATA occurs three
# times in CGATATATCCATAG.
# This is a classical pattern matching problem in Computer Science solved millions times per day all over
# the world when computer users use the common “Find” feature in text/code editors and Internet browsers.

# Task. Find all occurrences of a pattern in a string.

# Input Format. Strings Pattern and Genome.

# Constraints. 1 ≤ |Pattern| ≤ 106; 1 ≤ |Genome| ≤ 106; both strings are over A, C, G, T.

# Output Format. All starting positions in Genome where Pattern appears as a substring (using 0-based
# indexing as usual).

import sys


# Knuth-Morris-Pratt Algorithm
def find_pattern(pattern, text):
    """
    Find all the occurrences of the pattern in the text
    and return a list of all positions in the text
    where the pattern starts in the text.
    """

    # заполняем массив префиксными значениями (количество совпавших симвоов с паттерном)
    # преимущество подхода в том что подсчет идет основываясь на префиксном значении предидущего символа,
    # а не с начала строки
    def ComputePrefixFunction(S):
        s = [0 for i in range(len(S))]
        border = 0
        for i in range(1, len(S)):
            while border > 0 and S[i] != S[border]:
                border = s[border - 1]
            if S[i] == S[border]:
                border += 1
            else:
                border = 0
            s[i] = border
        return s

    result = []
    S = pattern + '$' + text
    s = ComputePrefixFunction(S)
    p = len(pattern)
    for i in range(len(pattern) + 1, len(S)):
        # если значение префиксной функции равно длинне паттерна, добавляем индекс в вывод
        if s[i] == p:
            result.append(i - 2 * p)
    return result


if __name__ == '__main__':
    pattern = sys.stdin.readline().strip()
    text = sys.stdin.readline().strip()
    result = find_pattern(pattern, text)
    print(" ".join(map(str, result)))
