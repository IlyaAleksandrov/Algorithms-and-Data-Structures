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


# return a string, after converting the previous task
def InverseBWT(bwt):
    n = len(bwt)
    # sort symbols alphabetically
    first = [i for i in bwt]
    first.sort()
    matrix = [0 for i in range(n)]
    # fill the matrix, each row by index is assigned a value from the alphabet sorting and the original BWT line
    for i in range(n):
        matrix[i] = [i, first[i], bwt[i]]
    # sort the rows of the matrix by the characters in bwt string
    matrix.sort(key=lambda i: i[2])
    result = []
    # After sorting, the ordered sequence of indices in column 0 has changed and has taken the form we need
    # we take indices based on the presented algorithm and add into result corresponding character of initial string
    t = matrix[0][0]
    for i in range(n):
        t = matrix[t][0]
        result.append(bwt[t])
    return result


if __name__ == '__main__':
    bwt = sys.stdin.readline().strip()
    print(*InverseBWT(bwt), sep="")

# Example of input:
# AGGGAA$
# Output:
# GAGAGA$
