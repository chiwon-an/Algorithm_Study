# import sys
# sys.stdin = open('s_input.txt')

def make_set(n):
    return [i for i in range(n+1)]

def find_set(x):
    if x != parent[x]:
        parent[x] = find_set(parent[x])
    return parent[x]

def union(x, y):
    root_x = find_set(x)
    root_y = find_set(y)
    if root_x != root_y:
        parent[root_y] = root_x


T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split()) # N: 사람의 수 (1 ≤ N ≤ 100), M: 사람의 관계 수 (0 ≤ M ≤ N(N-1)/2)
    parent = make_set(N)

    for _ in range(M):
        a, b = map(int, input().split())
        union(a, b)

    for i in range(1, N+1):
        find_set(i)

    result = len(set(parent[1:]))
    print(f'#{test_case} {result}')