# import sys
# sys.stdin = open('sample_input.txt')

import heapq

def prim(vertices, edges):
    mst = [] # 최소신장트리
    total_weight = 0

    visited = set() # 방문 확인
    start_vertex = vertices[1] # 시작 정점

    min_heap = [(w, start_vertex, e) for e, w in adj_list[start_vertex]]
    heapq.heapify(min_heap)
    visited.add(start_vertex)

    while min_heap:
        weight, start, end = heapq.heappop(min_heap)

        if end in visited:
            continue

        visited.add(end)
        mst.append((start, end, weight))
        total_weight += weight

        for next, wt in adj_list[end]:
            if next in visited:
                continue
            heapq.heappush(min_heap, (wt, end, next))

    return total_weight, mst


T = int(input())
for test_case in range(1, T+1):
    V, E = map(int, input().split()) # V: 정점의 수, E: 간선의 수
    edges = [list(map(int, input().split())) for _ in range(E)] # [시작정점, 도착정점, 가중치]
    vertices = [i for i in range(V+1)] # 정점 집합

    # 인접 리스트
    adj_list = {v: [] for v in vertices}
    for start, end, weight in edges:
        adj_list[start].append((end, weight))
        adj_list[end].append((start, weight))

    mst_weight, mst_edges = prim(vertices, edges) # Prim 알고리즘

    print(f'#{test_case} {mst_weight}')