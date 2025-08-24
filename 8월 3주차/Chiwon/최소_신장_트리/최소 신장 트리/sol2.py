import sys
import heapq
sys.stdin = open('sample_input.txt', 'r')

'''
prim algorithm은
1. visited행렬이 필요
2. 

'''

def prim(vertices, edges):
    mst = []
    visited = set()
    start_vertex = vertices[0]

    min_heap = [(w, start_vertex, e) for e, w in adj_list[start_vertex]]
    heapq.heapify(min_heap)
    visited.add(start_vertex)

    while min_heap:
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

    # V는 노드의 수 / E는 간선의 갯수
    V, E = map(int, input().split())

    edges = []

    # start, end, weight로 튜플을 만들어서 edges에 넣어주기
    for _ in range(E):

        start, end, weight = map(int, input().split())
        edges.append((start, end, weight))

    vertices = list(range(V+1))

    # {0: [], 1: [], 2: []}
    adj_list = {v: [] for v in vertices}

    # {0: [(1, 1), (2, 1)], 1: [(0, 1), (2, 6)], 2: [(0, 1), (1, 6)]}
    for s, e, w in edges:
        adj_list[s].append((e,w))
        adj_list[e].append((s,w))

    result = prim(vertices, edges)

    ans = 0

    for i in range(len(result)):
        ans += result[i][2]

    print(ans)