N, M = map(int, input().split())

basket = [None] * N
for i in range(N):
    basket[i] = i+1
print(basket)
for idx in range(1, M+1):
    i, j = map(int, input().split())
    new_i = basket[j-1]
    new_j = basket[i-1]
    basket[i-1] = new_i
    basket[j-1] = new_j

print(*basket)