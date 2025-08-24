import sys
sys.stdin = open('sample_input.txt', 'r')

import heapq, math


# 인접리스트 생성 함수
def make_graph(edges):
    # 0번 정점부터 N번 정점까지 총 N+1개 생성
    # N번 정점은 뻗어나가는 간선 없으므로 빈 리스트 유지
    adj_list = {i: [] for i in range(N+1)}
    for s, e, w in edges:
        # 시작 정점이 없으면 key로 추가
        if s not in adj_list:
            adj_list[s] = []
        # 끝 정점과 가중치를 묶어서 시작 정점 value로 추가
        adj_list[s].append((e, w))
    return adj_list


# 다익스트라 구현 함수
def dijkstra(adj_list, start):
    distances = {v: math.inf for v in adj_list}
    distances[start] = 0
    # 최초 힙
    heap = []
    # 시작 정점에서의 거리와 위치 힙에 추가
    heapq.heappush(heap, [0, start])
    # 방문처리할 set
    visited = set()
    # start 지점(시작 정점) 방문 처리
    visited.add(start)

    while heap:
        # 현재 지점의 정점과 정점까지의 거리
        dist, current = heapq.heappop(heap)
        # 만약 현재 정점을 방문했고,
        # 저장된 거리 정보가 현재 정점까지의 거리보다 작다면 갱신할 필요 X
        if current in visited and distances[current] < dist: continue
        # 현재 정점 방문 처리
        visited.add(current)
        # 현재 정점이 가진 value들 중 끝 정점, 가중치에 대해서
        for e, w in adj_list[current]:
            # 다음 정점까지의 거리는 현재까지의 거리 + 다음 정점까지의 가중치
            next_distance = dist + w
            # 다음 정점까지의 거리가 저장된 정보보다 작다면 갱신
            if next_distance < distances[e]:
                distances[e] = next_distance
                # 갱신한 후 갱신된 정보를 힙에 추가
                heapq.heappush(heap, [next_distance, e])
    return distances


T = int(input())
for tc in range(1, T+1):
    edges = []
    N, E = map(int, input().split())
    for _ in range(E):
        s, e, w = map(int, input().split())
        edges.append((s, e, w))
    adj_list = make_graph(edges)
    result = dijkstra(adj_list, 0)
    print(f'#{tc} {result[N]}')
