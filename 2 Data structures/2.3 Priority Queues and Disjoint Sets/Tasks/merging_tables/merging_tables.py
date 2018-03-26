# Problem Introduction
# In this problem, your goal is to simulate a sequence of merge operations with tables in a database.

# Task. There are 𝑛 tables stored in some database. The tables are numbered from 1 to 𝑛. All tables share
# the same set of columns. Each table contains either several rows with real data or a symbolic link to
# another table. Initially, all tables contain data, and 𝑖-th table has 𝑟𝑖 rows. You need to perform 𝑚 of
# the following operations:
# 1. Consider table number 𝑑𝑒𝑠𝑡𝑖𝑛𝑎𝑡𝑖𝑜𝑛𝑖. Traverse the path of symbolic links to get to the data. That
# is,
# while 𝑑𝑒𝑠𝑡𝑖𝑛𝑎𝑡𝑖𝑜𝑛𝑖 contains a symbolic link instead of real data do
# 𝑑𝑒𝑠𝑡𝑖𝑛𝑎𝑡𝑖𝑜𝑛𝑖 ← symlink(𝑑𝑒𝑠𝑡𝑖𝑛𝑎𝑡𝑖𝑜𝑛𝑖)
# 2. Consider the table number 𝑠𝑜𝑢𝑟𝑐𝑒𝑖 and traverse the path of symbolic links from it in the same
# manner as for 𝑑𝑒𝑠𝑡𝑖𝑛𝑎𝑡𝑖𝑜𝑛𝑖.
# 3. Now, 𝑑𝑒𝑠𝑡𝑖𝑛𝑎𝑡𝑖𝑜𝑛𝑖 and 𝑠𝑜𝑢𝑟𝑐𝑒𝑖 are the numbers of two tables with real data. If 𝑑𝑒𝑠𝑡𝑖𝑛𝑎𝑡𝑖𝑜𝑛𝑖 ̸=
# 𝑠𝑜𝑢𝑟𝑐𝑒𝑖, copy all the rows from table 𝑠𝑜𝑢𝑟𝑐𝑒𝑖 to table 𝑑𝑒𝑠𝑡𝑖𝑛𝑎𝑡𝑖𝑜𝑛𝑖, then clear the table 𝑠𝑜𝑢𝑟𝑐𝑒𝑖
# and instead of real data put a symbolic link to 𝑑𝑒𝑠𝑡𝑖𝑛𝑎𝑡𝑖𝑜𝑛𝑖 into it.
# 4. Print the maximum size among all 𝑛 tables (recall that size is the number of rows in the table).
# If the table contains only a symbolic link, its size is considered to be 0.
# See examples and explanations for further clarifications.

# Input Format. The first line of the input contains two integers 𝑛 and 𝑚 — the number of tables in the
# database and the number of merge queries to perform, respectively.
# The second line of the input contains 𝑛 integers 𝑟𝑖 — the number of rows in the 𝑖-th table.
# Then follow 𝑚 lines describing merge queries. Each of them contains two integers 𝑑𝑒𝑠𝑡𝑖𝑛𝑎𝑡𝑖𝑜𝑛𝑖 and
# 𝑠𝑜𝑢𝑟𝑐𝑒𝑖 — the numbers of the tables to merge.

# Constraints. 1 ≤ 𝑛,𝑚 ≤ 100 000; 0 ≤ 𝑟𝑖 ≤ 10 000; 1 ≤ 𝑑𝑒𝑠𝑡𝑖𝑛𝑎𝑡𝑖𝑜𝑛𝑖, 𝑠𝑜𝑢𝑟𝑐𝑒𝑖 ≤ 𝑛.

# Output Format. For each query print a line containing a single integer — the maximum of the sizes of all
# tables (in terms of the number of rows) after the corresponding operation.

import sys


# функция определяет корневого родителя
def getParent(i):
    if i != parent[i]:
        parent[i] = getParent(parent[i])
    return parent[i]


def merge(destination, source):
    # определяем корневых родителей элементов
    realDestination, realSource = getParent(destination), getParent(source)
    if realDestination == realSource:
        return False
    # выбираем множество с наибольшим рангом и цепляем меньшее к корневому родителя
    if rank[realSource] > rank[realDestination]:
        parent[realDestination] = realSource
        lines[realSource] += lines[realDestination]
        lines[realDestination] = 0
    else:
        parent[realSource] = realDestination
        lines[realDestination] += lines[realSource]
        lines[realSource] = 0
        if rank[realSource] == rank[realDestination]:
            rank[realDestination] += 1
    return True


n, m = map(int, sys.stdin.readline().split())
lines = list(map(int, sys.stdin.readline().split()))
# добавляем список рангов для узлв, изначально ранг у всех 1, т.к. узлы не связаны
rank = [1] * n
parent = list(range(0, n))
ans = max(lines)
for i in range(m):
    destination, source = map(int, sys.stdin.readline().split())
    merge(destination - 1, source - 1)
    ans = max(ans, lines[parent[destination - 1]], lines[parent[source - 1]])
    print(ans)
