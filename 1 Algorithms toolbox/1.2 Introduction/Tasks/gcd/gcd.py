# Task. Given two integers 𝑎 and 𝑏, find their greatest common divisor.


def gcd(a, b):
    if b > a:
        a, b = b, a
    if b == 0:
        return a
    return gcd(b, a % b)


a, b = map(int, input().split())
print(gcd(a, b))
