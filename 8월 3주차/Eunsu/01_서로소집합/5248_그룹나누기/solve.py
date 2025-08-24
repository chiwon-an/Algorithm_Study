# import sys
# sys.stdin = open('sample_input.txt')

def make_set(n):
    return [i for i in range(n+1)] # 자기 자신을 부모로 갖는 집합

def find_set(x):
    if x != parent[x]: # 자기 자신이 부모가 아닌 경우
        parent[x] = find_set(parent[x]) # 부모를 설정 (경로 압축)
    return parent[x]

def union(x, y):
    # if x > y:
    #     x, y = y, x
    root_x = find_set(x) # 부모 찾기
    root_y = find_set(y) # 부모 찾기
    if root_x != root_y: # 다른 집합인 경우
        parent[root_y] = root_x # 병합


T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split()) # N: 츨석번호 (2<=N<=100), M: 신청서 (1<=M<=100)
    pairs = list(map(int, input().split()))

    parent = make_set(N) # 초기화
    # print(parent) # [0, 1, 2, 3, 4, 5, 6, 7]

    for i in range(0, len(pairs), 2):
        union(pairs[i], pairs[i+1]) # union 연산
    # print(parent) # [0, 1, 2, 2, 7, 4, 4, 7]

    # 경로 압축
    for i in range(1, N+1):
        find_set(i)
    # print(parent) # [0, 1, 2, 2, 7, 7, 7, 7]

    result = len(set(parent[1:]))
    print(f'#{test_case} {result}')