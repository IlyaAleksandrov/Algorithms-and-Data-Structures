# Problem Introduction
# In this problem you will convert an array of integers into a heap. This is the crucial step of the sorting
# algorithm called HeapSort. It has guaranteed worst-case running time of 𝑂(𝑛 log 𝑛) as opposed to QuickSort’s
# average running time of 𝑂(𝑛 log 𝑛). QuickSort is usually used in practice, because typically it is faster, but
# HeapSort is used for external sort when you need to sort huge files that don’t fit into memory of your
# computer.

# Task. The first step of the HeapSort algorithm is to create a heap from the array you want to sort. By the
# way, did you know that algorithms based on Heaps are widely used for external sort, when you need
# to sort huge files that don’t fit into memory of a computer?
# Your task is to implement this first step and convert a given array of integers into a heap. You will
# do that by applying a certain number of swaps to the array. Swap is an operation which exchanges
# elements 𝑎𝑖 and 𝑎𝑗 of the array 𝑎 for some 𝑖 and 𝑗. You will need to convert the array into a heap
# using only 𝑂(𝑛) swaps, as was described in the lectures. Note that you will need to use a min-heap
# instead of a max-heap in this problem.

# Input Format. The first line of the input contains single integer 𝑛. The next line contains 𝑛 space-separated
# integers 𝑎𝑖.

# Constraints. 1 ≤ 𝑛 ≤ 100 000; 0 ≤ 𝑖, 𝑗 ≤ 𝑛 − 1; 0 ≤ 𝑎0, 𝑎1, . . . , 𝑎𝑛−1 ≤ 109. All 𝑎𝑖 are distinct.

# Output Format. The first line of the output should contain single integer 𝑚 — the total number of swaps.
# 𝑚 must satisfy conditions 0 ≤ 𝑚 ≤ 4𝑛. The next 𝑚 lines should contain the swap operations used
# to convert the array 𝑎 into a heap. Each swap is described by a pair of integers 𝑖, 𝑗 — the 0-based
# indices of the elements to be swapped. After applying all the swaps in the specified order the array
# must become a heap, that is, for each 𝑖 where 0 ≤ 𝑖 ≤ 𝑛 − 1 the following conditions must be true:
# 1. If 2𝑖 + 1 ≤ 𝑛 − 1, then 𝑎𝑖 < 𝑎2𝑖+1.
# 2. If 2𝑖 + 2 ≤ 𝑛 − 1, then 𝑎𝑖 < 𝑎2𝑖+2.
# Note that all the elements of the input array are distinct. Note that any sequence of swaps that has
# length at most 4𝑛 and after which your initial array becomes a correct heap will be graded as correct.

import math


class HeapBuilder:
    def __init__(self):
        self._swaps = []
        self._data = []

    def ReadData(self):
        n = int(input())
        self._data = [int(s) for s in input().split()]
        assert n == len(self._data)

    def WriteResponse(self):
        print(len(self._swaps))
        for swap in self._swaps:
            print(swap[0], swap[1])

    def GenerateSwaps(self):
        def Parent(i):
            return math.ceil(i/2 - 1)

        def LeftChild(i):
            return i*2 + 1

        def RightChild(i):
            return i*2 + 2

        def SiftDown(i):
            l = LeftChild(i)
            r = RightChild(i)
            # проверяем наличие обоих детей у узла
            if l < size and r < size:
                # определяем минимальный из трех узлов
                minimum = min(self._data[l], self._data[r], self._data[i])
                # если родительский узел минимальный, ничего не делаем
                # иначе меняем родителя с минимальным узлом и просееваем родительский узел вниз
                if minimum != self._data[i]:
                    if minimum == self._data[l]:
                        self._data[i], self._data[l] = self._data[l], self._data[i]
                        self._swaps.append((i, l))
                        SiftDown(l)
                    else:
                        self._data[i], self._data[r] = self._data[r], self._data[i]
                        self._swaps.append((i, r))
                        SiftDown(r)
            # если одного из дочерних узлов нет и родительский узел больше, меняем узлы местами и просееваем родителя вниз
            else:
                if l < size and self._data[l] < self._data[i]:
                    self._data[i], self._data[l] = self._data[l], self._data[i]
                    self._swaps.append((i, l))
                    SiftDown(l)

        # начиная с середины кучи и до корня делаем SiftDown (просеевание вниз) для каждого элемента
        size = len(self._data)
        for i in range(size // 2, 0, -1):
            SiftDown(i - 1)

    def CheckIt(x):
        for i in range(1, len(x)):
            if x[i] < x[math.ceil(i/2 - 1)]:
                print(i)
                return False
        return True

    def Solve(self):
        self.ReadData()
        self.GenerateSwaps()
        self.WriteResponse()


if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.Solve()
