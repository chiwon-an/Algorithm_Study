# import sys
# sys.stdin = open('sample_input.txt')

import heapq

def dijkstra(graph, start):
    # 초기화
    distances = {v: float('inf') for v in range(N+1)}
    distances[start] = 0

    heap = [] # 최소 힙
    visited = set() # 방문 체크
    heapq.heappush(heap, [0, start]) # [거리, 시작 정점]

    while heap:
        dist, current = heapq.heappop(heap) # [거리, 시작 정점]
        if current in visited or distances[current] < dist:
            continue

        visited.add(current)
        for next, weight in graph[current].items():
            next_distance = dist + weight
            if next_distance < distances[next]:
                distances[next] = next_distance
                heapq.heappush(heap, [next_distance, next])

    return distances


T = int(input())
for test_case in range(1, T+1):
    N, E = map(int, input().split()) # N: 마지막 연결지점 번호, E: 도로의 개수
    data = [list(map(int, input().split())) for _ in range(E)] # [구간 시작, 구간 끝, 구간 거리]

    # 인접 리스트
    graph = {v:{} for v in range(N+1)}
    for start, end, weight in data:
        graph[start][end] = weight

    result = dijkstra(graph, 0)

    print(f'#{test_case} {result[N]}')