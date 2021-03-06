# Problem Introduction
# In this problem, your goal is to implement the Rabin–Karp’s algorithm.

# Task. In this problem your goal is to implement the Rabin–Karp’s algorithm for searching the given pattern
# in the given text.

# Input Format. There are two strings in the input: the pattern 𝑃 and the text 𝑇.
# Constraints. 1 ≤ |𝑃| ≤ |𝑇| ≤ 5 · 10^5. The total length of all occurrences of 𝑃 in 𝑇 doesnt exceed 108. The
# pattern and the text contain only latin letters.

# Output Format. Print all the positions of the occurrences of 𝑃 in 𝑇 in the ascending order. Use 0-based
# indexing of positions in the the text 𝑇.

import random
# Implementation of the fast version of the Rabin–Karp’s algorithm from the lectures.


def read_input():
    return (input().rstrip(), input().rstrip())


def print_occurrences(output):
    print(' '.join(map(str, output)))


def get_occurrences(pattern, text):
    S = [ord(i) for i in text]
    P = [ord(i) for i in pattern]
    # choosing a big prime number
    p = 10**9+7
    lenS = len(S)
    lenP = len(P)
    # choose x for random hash function of polynomial family
    x = random.randint(1, p - 1)
    result = []
    # computing the hash of the pattern
    pHash = PolyHash(P,p,x)
    # computing the hash of all substrings
    H = PrecomputeHashes(S, P, p, x)
    # if hashes of substring and pattern are equal we comparing strings
    for i in range(0, lenS - lenP + 1):
        if pHash == H[i]:
            if text[i : i + lenP] == pattern:
                result.append(i)
    return result


# function to compute hash function of the string
def PolyHash(S, p, x):
    ans = S[0]
    y = 1
    for i in range(1, len(S)):
        y = (y * x) % p
        ans = (ans + (S[i] * y) % p + p) % p
    return ans


# function to compute hash function for all substrings
def PrecomputeHashes(T, P, p, x):
    H = [0] * (len(T)-len(P) + 1)
    S = T[len(T) - len(P):len(T)]
    H[-1] = PolyHash(S, p, x)
    y = 1
    for i in range(len(P)):
        y = (y * x) % p
    for i in range(len(T) - len(P) - 1, -1, -1):
        H[i] = ((x * H[i + 1] + T[i] - y * T[i + len(P)]) % p + p) % p
    return H


if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
# Example of input:
# aba
# abacaba
# Output:
# 0 4
