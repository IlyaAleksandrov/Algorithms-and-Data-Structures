# Problem Introduction
# Another problem that can be solved efficiently with tries is the following.
# Multiple Pattern Matching Problem
# Find all occurrences of a collection of patterns in a text.

# Problem Introduction (extended)
# The goal in this problem is to extend the solution for the previous problem such that it will be able to handle
# cases when one of the patterns is a prefix of another pattern. In this case, some patterns are spelled in a trie
# by traversing a path from the root to an internal vertex, but not to a leaf.

# Input: A string Text and a collection Patterns containing (shorter) strings.
# Output: All starting positions in Text where a string from Patterns appears as a substring.
# Again, the multiple pattern matching problem has many applications like highlighting programming
# language keywords (like if, else, elif) in your favorite IDE (see the screenshot below) and locating reads
# in a reference genome.

# Input Format. The first line of the input contains a string Text, the second line contains an integer 𝑛,
# each of the following 𝑛 lines contains a pattern from Patterns = {𝑝1, . . . , 𝑝𝑛}.

# Constraints. 1 ≤ |Text| ≤ 10 000; 1 ≤ 𝑛 ≤ 5 000; 1 ≤ |𝑝𝑖| ≤ 100 for all 1 ≤ 𝑖 ≤ 𝑛; all strings contain only
# symbols A, C, G, T; no 𝑝𝑖 is a prefix of 𝑝𝑗 for all 1 ≤ 𝑖 != 𝑗 ≤ 𝑛.

# Output Format. All starting positions in Text where a string from Patterns appears as a substring in
# increasing order (assuming that Text is a 0-based array of symbols).

import sys


def solve(text, n, patterns):
    result = []

    # we build a suffix tree from patterns
    def build_trie(patterns):
        tree = {0: {}}
        count = 0
        for p in patterns:
            currentNode = 0
            # for each character of each pattern
            for i in range(len(p)):
                currentSymbol = p[i]
                # if in the tree at the place of the current symbol there is already a given symbol,
                # then go to the next node
                if tree[currentNode].get(currentSymbol) is not None:
                    currentNode = tree[currentNode].get(currentSymbol)
                # if not then added
                else:
                    tree[count + 1] = {}
                    tree[currentNode][currentSymbol] = count + 1
                    currentNode = count + 1
                    count += 1
            # At the end of each pattern, add 0, as the end symbol
            tree[currentNode] = {0: 0}
        return tree

    def prefixTreeMatching(text, trie):
        count = 0
        symbol = text[count]
        v = trie[0]
        while True:
            # if we got to the node with 0, then we got to the end of the pattern, we can return 1 (success)
            if v.get(0) != None:
                return 1
            # If the current symbol is present in the tree, proceed to the next one,
            # verifying that we have not exceeded the boundaries of the text
            elif v.get(symbol) != None:
                v = trie[v.get(symbol)]
                count += 1
                if count <= x:
                    symbol = text[count]
                else:
                    return 0
            else:
                return 0

    trie = build_trie(patterns)
    symbNumb = 0
    x = len(text)
    # for the algorithm it is necessary to add the end-of-text symbol
    text += "0"
    # For each character in the text matching with the suffix tree one
    while symbNumb != x:
        ans = prefixTreeMatching(text, trie)
        if ans == 1:
            result.append(symbNumb)
        text = text[1:]
        symbNumb += 1
    return result


text = sys.stdin.readline().strip()
n = int(sys.stdin.readline().strip())
patterns = []
for i in range(n):
    patterns += [sys.stdin.readline().strip()]
ans = solve(text, n, patterns)

sys.stdout.write(' '.join(map(str, ans)) + '\n')

# Example of input:
# ACATA
# 3
# AT
# A
# AG
# Output:
# 0 2 4
# Explanation:
# Text contains occurrences of A at positions 0, 2, and 4, as well as an occurrence of AT at position 2.
