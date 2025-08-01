# def factorial(N) :
#     if N == 0 :
#         return 1
#     else :
#         return (N * factorial(N-1))

# N = int(input())

# print(factorial(N))

# N 값이 너무 클 경우 런타임 에러 발생

# N에 값 입력
N = int(input())

factorial = 1
for i in range(N):
    factorial *= i+1

print(factorial)