import sys
sys.stdin = open('input.txt')

# 각자 자기 자신의 집합으로 만들어 주기
def make_set(N):

    return [i for i in range(N+1)]

# 자신이 속합 집합의 대표자를 찾아주기
def find_set(x):

    if x == parent[x]:
        return parent[x]
    parent[x] = find_set(parent[x])
    return parent[x]

# 대표자들끼리 같으면 아무 것도 하지말고, 다르면 그거하기
def union(x,y):

    root_x = find_set(x)
    root_y = find_set(y)

    if root_x != root_y:

        parent[root_y] = root_x


T = int(input())

for tc in range(1, T+1):
    
    N, M = map(int, input().split())
    
    # parent에 N명의 집합을 만들어 주기
    parent = make_set(N)
    
    # lst에 그거 리스트 만들기
    lst = list(map(int, input().split()))
    
    # 시작정점이랑 도착 정점을 각각 union시켜주기
    for i in range(0, 2*M, 2):
        union(lst[i], lst[i+1])

    # 1234
    # [0,1,1,3,3,5]
    # print(parent)

    for i in range(1,N+1):
        find_set(i)

    # print(parent)
    print(f'#{tc} {len(set(parent)) - 1}')