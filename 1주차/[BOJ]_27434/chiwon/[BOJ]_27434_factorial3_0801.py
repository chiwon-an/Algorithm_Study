# 문제
# 0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 정수 N(0 ≤ N ≤ 100,000)이 주어진다.

# 출력
# 첫째 줄에 N!을 출력한다.

# 예제 입력 1 
# 10
# 예제 출력 1 
# 3628800
# 예제 입력 2 
# 0
# 예제 출력 2 
# 1

# def factorial(a):

#     if a == 1 or a == 0:
#         return 1
    
#     else:
#         return a * factorial(a-1)

# N = int(input())

# print(factorial(N))


N = int(input())
result = 1

for i in range(1,N+1):
    result *= i

print(result)