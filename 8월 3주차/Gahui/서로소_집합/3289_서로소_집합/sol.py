import sys
sys.stdin = open('sample_input.txt', 'r')


# parent 만드는 함수
def make_set(n):
    return [i for i in range(n+1)]


# 대표자 찾는 함수 (경로 압축 적용)
def find_set(x):
    if x == parent[x]:
        return x
    parent[x] = find_set(parent[x])
    return parent[x]


# 합집합 연산하는 함수
def union(x, y):
    root_x = find_set(x)
    root_y = find_set(y)

    if root_x != root_y:
        parent[root_y] = root_x


# 같은 집합인지 확인하는 함수
def is_include(x, y):
    root_x = find_set(x)
    root_y = find_set(y)

    if root_x != root_y:
        return 0
    else:
        return 1


T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    calc = [list(map(int, input().split())) for _ in range(m)]
    parent = make_set(n)
    result = []
    for op, x, y in calc:
        if op == 0:
            union(x, y)
        elif op == 1:
            result.append(str(is_include(x, y)))
    print(f'#{tc} {"".join(result)}')
