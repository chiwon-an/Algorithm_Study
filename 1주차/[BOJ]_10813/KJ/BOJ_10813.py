N, M = map(int, input().split())
basket = list(range(N+1))

for _ in range(M):
    i, j = map(int, input().split())
    temp = basket[i]
    basket[i] = basket[j]
    basket[j] = temp

print(' '.join(map(str, basket[1:])))