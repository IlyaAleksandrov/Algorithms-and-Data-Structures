# Task. Given two integers 𝑎 and 𝑏, find their greatest common divisor.


def gcd(a, b):
    if b > a:
        tmp = a
        a = b
        b = tmp
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


a, b = map(int, input().split())
print(gcd(a, b))
