# Problem Introduction
# The goal in this problem is to construct the suffix array of a given string again, but this time for a longer
# string. In particular, a quadratic algorithm will not fit into the time limit in this problem. This will require you
# to implement an almost linear algorithm bringing you close to the state-of-the-art algorithms for constructing
# suffix arrays.

# Task. Construct the suffix array of a string.

# Input Format. A string Text ending with a “$” symbol.

# Constraints. 1 ≤ |Text| ≤ 2 · 10^5; except for the last symbol, Text contains symbols A, C, G, T only.

# Output Format. SuffixArray(Text), that is, the list of starting positions of sorted suffixes separated by
# spaces.

import sys


def build_suffix_array(text):
    """
    Build suffix array of the string text and
    return a list result of the same length as the text
    such that the value result[i] is the index (0-based)
    in text where the i-th lexicographically smallest
    suffix of text starts.
    """
    def sortCharacters(text):
        order = [0 for i in range(len(text))]
        count = [0 for i in range(26)]
        for i in range(len(text) - 1):
            count[ord(text[i].upper()) - 65] += 1
        for j in range(1, 26):
            count[j] = count[j] + count[j - 1]
        for i in range(len(text) - 2, -1, -1):
            c = ord(text[i].upper()) - 65
            count[c] = count[c] - 1
            order[count[c] + 1] = i
        order[0] = len(text) - 1
        return order

    def computeCharClasses(S, order):
        classes = [0 for i in range(len(text))]
        classes[order[0]] = 0
        for i in range(1, len(text)):
            if S[order[i]] != S[order[i - 1]]:
                classes[order[i]] = classes[order[i - 1]] + 1
            else:
                classes[order[i]] = classes[order[i - 1]]
        return classes

    def sortedDoubled(text, L, order, classes):
        n = len(text)
        count = [0 for i in range(n)]
        newOrder = [0 for i in range(n)]
        for i in range(n):
            count[classes[i]] += 1
        for j in range(1, n):
            count[j] = count[j] + count[j - 1]
        for i in range(len(text) - 1, -1, -1):
            start = (order[i] - L + n) % n
            cl = classes[start]
            count[cl] = count[cl] - 1
            newOrder[count[cl]] = start
        order[0] = len(text) - 1
        return newOrder

    def updatedClasses(order, classes, L):
        n = len(order)
        newClasses = [0 for i in range(len(text))]
        classes[order[0]] = 0
        for i in range(1, len(text)):
            cur = order[i]
            prev = order[i - 1]
            mid = cur + L
            midPrev = (prev + L) % n
            if classes[cur] != classes[prev] or classes[mid] != classes[midPrev]:
                newClasses[cur] = newClasses[prev] + 1
            else:
                newClasses[cur] = newClasses[prev]
        return newClasses

    order = sortCharacters(text)
    classes = computeCharClasses(text, order)
    L = 1
    while L < len(text):
        order = sortedDoubled(text, L, order, classes)
        classes = updatedClasses(order, classes, L)
        L = L * 2
    return order


if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    print(" ".join(map(str, build_suffix_array(text))))

# Example of input:
# AACGATAGCGGTAGA$
# Output:
# 15 14 0 1 12 6 4 2 8 13 3 7 9 10 11 5
# Sorted suffixes:
# 15 $
# 14 A$
# 0 AACGATAGCGGTAGA$
# 1 ACGATAGCGGTAGA$
# 12 AGA$
# 6 AGCGGTAGA$
# 4 ATAGCGGTAGA$
# 2 CGATAGCGGTAGA$
# 8 CGGTAGA$
# 13 GA$
# 3 GATAGCGGTAGA$
# 7 GCGGTAGA$
# 9 GGTAGA$
# 10 GTAGA$
# 11 TAGA$
# 5 TAGCGGTAGA$

