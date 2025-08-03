### 10872. 팩토리얼 ###

def factorial(N):
    if N <= 1:
        return 1
    else:
        return N * factorial(N-1)

N = int(input())
print(factorial(N))