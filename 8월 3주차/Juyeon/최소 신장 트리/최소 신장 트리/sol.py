'''
    0번부터 V번까지의 노드와 E개의 간선을 가진 그래프 정보가 주어질 때,
    이 그래프로부터 최소신장트리를 구성하는 간선의 가중치를 모두 더해 출력하는 프로그램을 작성
    
    입력
        1. T : 테스트 케이스 수 (1 <= T <= 50)
        2. V : 마지막 노드번호 / E : 간선의 개수 (1 <= V <= 1000, 1 <= E <= 1,000,000)
        3. n1 : 시작 노드 / n2 : 끝 노드 / w : 가중치 (1 <= w <= 10)

    출력
        - #{tc} {최소신장트리를 구성하는 간선의 가중치들의 합}
'''

# import sys
# sys.stdin = open('sample_input.txt')

import heapq

def prim(vertices, edges):
    mst = []
    visited = set()
    start_vertex = vertices[0]

    min_heap = [(w, start_vertex, e) for e, w in adj_list[start_vertex]]
    heapq.heapify(min_heap)
    visited.add(start_vertex)

    while min_heap:
        # print(min_heap)
        weight, start, end = heapq.heappop(min_heap)
        if end in visited: continue

        visited.add(end)
        mst.append((start, end, weight))

        for next, weight in adj_list[end]:
            if next in visited: continue
            heapq.heappush(min_heap, (weight, end, next))

    return mst


T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    edges = []
    for _ in range(E):
        edges.append(list(map(int, input().split())))
    # print(edges)
    vertices = list(range(V+1))
    adj_list = {v : [] for v in vertices}
    for n1, n2, w in edges:
        adj_list[n1].append((n2, w))
        adj_list[n2].append((n1, w))
    # print(adj_list)

    result = prim(vertices, edges)
    total = sum([result[i][2] for i in range(len(result))])
    print(f'#{tc} {total}')