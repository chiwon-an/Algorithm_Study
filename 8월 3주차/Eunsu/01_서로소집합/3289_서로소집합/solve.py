# import sys
# sys.stdin = open('sample_input.txt')

def make_set(n):
    return [i for i in range(n+1)]

def find_set(x):
    if x != parent[x]:
        parent[x] = find_set(parent[x]) # 경로 압축
    return parent[x]

def union(x, y):
    root_x = find_set(x)
    root_y = find_set(y)
    if root_x != root_y:
        parent[root_y] = root_x


T = int(input())
for test_case in range(1, T+1):
    n, m = map(int, input().split()) # n: 집합 (1≤n≤1,000,000), m: 연산의 개수 (1≤m≤100,000)

    parent = make_set(n)
    result = []

    for _ in range(m):
        num, a, b = map(int, input().split())
        if num == 0:
            union(a, b)
        elif num == 1:
            result.append('1' if find_set(a) == find_set(b) else '0') # 루트 노드가 같은 경우

    print(f"#{test_case} {''.join(result)}")