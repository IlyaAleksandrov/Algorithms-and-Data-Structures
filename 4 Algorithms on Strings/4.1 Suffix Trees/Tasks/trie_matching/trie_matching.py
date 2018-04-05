# Problem Introduction
# Another problem that can be solved efficiently with tries is the following.
# Multiple Pattern Matching Problem
# Find all occurrences of a collection of patterns in a text.

# Input: A string Text and a collection Patterns containing (shorter) strings.
# Output: All starting positions in Text where a string from Patterns appears as a substring.
# Again, the multiple pattern matching problem has many applications like highlighting programming
# language keywords (like if, else, elif) in your favorite IDE (see the screenshot below) and locating reads
# in a reference genome.

# Input Format. The first line of the input contains a string Text, the second line contains an integer 𝑛,
# each of the following 𝑛 lines contains a pattern from Patterns = {𝑝1, . . . , 𝑝𝑛}.

# Constraints. 1 ≤ |Text| ≤ 10 000; 1 ≤ 𝑛 ≤ 5 000; 1 ≤ |𝑝𝑖| ≤ 100 for all 1 ≤ 𝑖 ≤ 𝑛; all strings contain only
# symbols A, C, G, T; no 𝑝𝑖 is a prefix of 𝑝𝑗 for all 1 ≤ 𝑖 ̸= 𝑗 ≤ 𝑛.

# Output Format. All starting positions in Text where a string from Patterns appears as a substring in
# increasing order (assuming that Text is a 0-based array of symbols).

import sys


def solve(text, n, patterns):
    result = []

    # строим суффиксное дерево из паттернов
    def build_trie(patterns):
        tree = {0: {}}
        count = 0
        for p in patterns:
            currentNode = 0
            # для каждого символа каждого паттерна
            for i in range(len(p)):
                currentSymbol = p[i]
                # если в дереве на месте текущего символа уже есть данный символ, то идем к следующему узлу
                if tree[currentNode].get(currentSymbol) != None:
                    currentNode = tree[currentNode].get(currentSymbol)
                # если нет до добавляем
                else:
                    tree[count + 1] = {}
                    tree[currentNode][currentSymbol] = count + 1
                    currentNode = count + 1
                    count += 1
            # в конце каждого паттерна добавляем 0, как символ окончания
            tree[currentNode] = {0: 0}
        return tree

    def prefixTreeMatching(text, trie):
        count = 0
        symbol = text[count]
        v = trie[0]
        while True:
            # если мы добрались до узла с 0, то мы добрались до конца паттерна, можно возвращать 1 (успех)
            if v.get(0) != None:
                return 1
            # если текущий символ имеется в дереве, переходим к следующему, кроверяя что мы не вышли за границы текста
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
    # для алгоритма необходимо добавить в конец текста символ конца текста
    text += "0"
    # для каждого сивола из текста проверяем на сопоставление с суффиксным деревом
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
