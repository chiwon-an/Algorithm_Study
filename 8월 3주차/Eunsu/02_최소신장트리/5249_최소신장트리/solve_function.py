# import sys
# sys.stdin = open('sample_input.txt')

def make_set(n):
    parent = [i for i in range(n+1)]
    rank = [0] * (n+1)
    return parent, rank

def find_set(x, parent):
    if x != parent[x]:
        parent[x] = find_set(parent[x], parent)
    return parent[x]

def union(x, y, parent, rank):
    px = find_set(x, parent)
    py = find_set(y, parent)
    if px != py:
        if rank[px] < rank[py]:
            parent[px] = py
        elif rank[px] > rank[py]:
            parent[py] = px
        else:
            parent[py] = px
            rank[px] += 1

def mst_kruskal(V, edges):
    '''
        1. 모든 간선을 가중치 기준으로 오름차순 정렬
        2. 가중치가 가장 작은 간선부터 하나씩 확인
        3. 두 정점이 같은 집합(=사이클 생성)인지 확인
            - 서로 다른 집합이면 -> 간선 추가 (union)
            - 같은 집합이면 -> 사이클 생기므로 버림
        4. 간선의 수가 (정점 수 - 1)개가 되면 종료
    '''

    mst = [] # 최소 신장 트리
    total_weight = 0

    parent, rank = make_set(V)
    edges.sort(key=lambda x: x[2]) # 가중치 기준 오름차순 정렬

    for edge in edges:
        start, end, weight = edge
        if find_set(start, parent) != find_set(end, parent):
            union(start, end, parent, rank)
            total_weight += weight
            mst.append(edge)

    return total_weight, mst


T = int(input())
for test_case in range(1, T+1):
    V, E = map(int, input().split()) # V: 정점 수, E: 간선 수
    edges = [list(map(int, input().split())) for _ in range(E)] # [시작정점, 도착정점, 가중치]

    mst_weight, mst_edges = mst_kruskal(V, edges) # Kruskal 알고리즘

    print(f'#{test_case} {mst_weight}')