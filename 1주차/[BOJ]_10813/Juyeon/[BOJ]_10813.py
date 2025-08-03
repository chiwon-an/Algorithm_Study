N, M = map(int, input().split())
lst = list(range(1, N+1))

for k in range(M):
    i, j = map(int, input().split())
    if i == j :
        pass
    else:
        a = lst[i-1]
        lst[i-1] = lst[j-1]
        lst[j-1] = a

# Unpacking
print(*lst)