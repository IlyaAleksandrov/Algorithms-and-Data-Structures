# Problem Introduction
# For a collection of strings Patterns, Trie(Patterns) is defined as follows.
# ∙ The trie has a single root node with indegree 0.
# ∙ Each edge of Trie(Patterns) is labeled with a letter of the alphabet.
# ∙ Edges leading out of a given node have distinct labels.
# ∙ Every string in Patterns is spelled out by concatenating the letters along some path from the root
# downward.
# ∙ Every path from the root to a leaf (i.e, node with outdegree 0), spells a string from Patterns.

# Tries are a common way of storing a dictionary of words and are used, e.g., for implementing an autocomplete
# feature in text editors (on your laptop or mobile phone), code editors, and web search engines like
# Google or Yandex. Just imagine how much time is saved everyday by this feature.

# Task. Construct a trie from a collection of patterns.

# Input Format. An integer 𝑛 and a collection of strings Patterns = {𝑝1, . . . , 𝑝𝑛} (each string is given on a
# separate line).

# Constraints. 1 ≤ 𝑛 ≤ 100; 1 ≤ |𝑝𝑖| ≤ 100 for all 1 ≤ 𝑖 ≤ 𝑛; 𝑝𝑖’s contain only symbols A, C, G, T; no 𝑝𝑖 is
# a prefix of 𝑝𝑗 for all 1 ≤ 𝑖 != 𝑗 ≤ 𝑛.

# Output Format. The adjacency list corresponding to Trie(Patterns), in the following format. If
# Trie(Patterns) has 𝑛 nodes, first label the root with 0 and then label the remaining nodes with the
# integers 1 through 𝑛−1 in any order you like. Each edge of the adjacency list of Trie(Patterns) will be
# encoded by a triple: the first two members of the triple must be the integers 𝑖, 𝑗 labeling the initial and
# terminal nodes of the edge, respectively; the third member of the triple must be the symbol 𝑐 labeling
# the edge; output each such triple in the format u->v:c (with no spaces) on a separate line.

import sys


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
    return tree


if __name__ == '__main__':
    patterns = sys.stdin.read().split()[1:]
    tree = build_trie(patterns)
    for node in tree:
        for c in tree[node]:
            print("{}->{}:{}".format(node, tree[node][c], c))

# Example of input:
# 1
# ATA
# Output:
# 0->1:A
# 2->3:A
# 1->2:T
