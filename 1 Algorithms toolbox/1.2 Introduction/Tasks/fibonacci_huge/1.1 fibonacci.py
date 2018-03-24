# Task. Given an integer 𝑛, find the 𝑛th Fibonacci number 𝐹𝑛

def get_fibonacci(n):
    if n <= 1:
        return n
    previous = 0
    current = 1
    for _ in range(n - 1):
        previous, current = current, previous + current
    return current


a = int(input())
print(get_fibonacci(a))
