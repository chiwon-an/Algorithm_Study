### 27434. 팩토리얼 3 ###

N = int(input())

result = 1
for num in range(1, N+1):
    result *= num
print(result)