# Problem Introduction
# In this problem, we ask a simple question: how many times one string occurs as a substring of another?
# Recall that different occurrences of a substring can overlap with each other. For example, ATA occurs three
# times in CGATATATCCATAG.
# This is a classical pattern matching problem in Computer Science solved millions times per day all over
# the world when computer users use the common “Find” feature in text/code editors and Internet browsers.

# Task. Find all occurrences of a pattern in a string.

# Input Format. Strings Pattern and Genome.

# Constraints. 1 ≤ |Pattern| ≤ 10^6; 1 ≤ |Genome| ≤ 10^6; both strings are over A, C, G, T.

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

    # fill the array with prefix values (the number of matched characters with a pattern)
    # The advantage of the approach is that counting is based on the prefix value of the previous character,
    # and not from the beginning of the line
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
        # if the value of the prefix function is equal to the length of the pattern, add the index to the result
        if s[i] == p:
            result.append(i - 2 * p)
    return result


if __name__ == '__main__':
    pattern = sys.stdin.readline().strip()
    text = sys.stdin.readline().strip()
    result = find_pattern(pattern, text)
    print(" ".join(map(str, result)))

# Example of input:
# ATAT
# GATATATGCATATACTT
# Output:
# 1 3 9
# The pattern appears at positions 1, 3, and 9 in the text.
