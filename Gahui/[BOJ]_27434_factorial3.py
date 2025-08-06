import sys
sys.setrecursionlimit(10**6)

T = int(input())

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n)

print(factorial(T))