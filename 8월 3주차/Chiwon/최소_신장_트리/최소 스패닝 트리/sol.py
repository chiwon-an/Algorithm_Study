import sys
sys.stdin = open('sample_input (1).txt','r')

'''
Kruskal's algorithm
1. 가중치로 정렬
2. 하나씩 뽑으면서 UNION
3. 대표 정점이 다르면 MST에 추가
              같으면 아무 것도 X

'''
def find_set(x):

    if x == parents[x]:
        return parents[x]

    parents[x] = find_set(parents[x])
    return parents[x]

def union(x,y):

    root_x = find_set(x)
    root_y = find_set(y)

    if root_x != root_y:
        parents[root_y] = root_x
        return 1

def kruskal(edges):

    global mst

    for idge in edges:
        # print(idge)
        start, end = idge[1], idge[2]

        # 유니온 값이 1이면 mst에 값을 넣어주기.
        if union(start, end) == 1:
            # print(idge)
            mst.append(idge)



T = int(input())

for tc in range(1,T+1):

    # V = 정점의 갯수
    # E = 간선의 갯수
    V, E = map(int, input().split())

    edges = []

    for i in range(E):

        start, end, weight = map(int, input().split())

        # 정렬할 때 편하게 하기 위해서 edge의 첫 번째에 weight으로 순서 바꿔줌
        edges.append((weight, start, end))

    # 가중치 기준으로 정렬
    edges.sort()

    # 간선을 담을 리스트
    mst = []

    # 각 집합 생성 완료
    parents = list(range(V+1))
    
    # 알고리즘 시작
    kruskal(edges)

    ans = 0
    for i in range(len(mst)):
        ans += mst[i][0]

    print(f'#{tc} {ans}')
