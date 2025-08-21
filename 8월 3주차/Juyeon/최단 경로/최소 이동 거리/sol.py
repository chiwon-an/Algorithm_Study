'''
    E개의 일방통행 도로 구간이 있으며
    각 구간이 만나는 연결지점에는 0부터 N번까지의 번호가 있음

    구간의 시작과 끝의 연결 지점 번호, 구간의 길이가 주어질 때,
    0번 지점에서 N번 지점까지 이동하는 데 걸리는 최소한의 거리가 얼마인지 출력하는 프로그램

    모든 연결 지점을 거쳐가야 하는 것은 아니다.

    입력
        1. T : 테스트 케이스 수 (1 <= T <= 50)
        2. N : 마지막 연결지점 번호 / E : 도로의 개수 [간선의 개수] (1 <= N <= 1000 / 1 <= E <= 1000000)
        3. s : 시작 지점 / e : 끝 지점 / w : 구간 거리 (1 <= s, e <= 1000 / 1 <= w <=10)

    출력
        - #{tc} {0번부터 N번 지점까지 이동하는 데 걸리는 최소한의 거리}
'''
import sys
sys.stdin = open('sample_input.txt')

import heapq, math

def dijkstra(graph, start):
    distances = {v : math.inf for v in graph}

    heap = []
    heapq.heappush(heap, [0, start])
    visited = set()
    visited.add(start)

    while heap:
        # print(heap)
        # print(distances)
        dist, current = heapq.heappop(heap)

        if current in visited and distances[current] < dist : continue

        for next, weight in graph[current]:
            next_distance = dist + weight
            if next_distance < distances[next]:
                distances[next] = next_distance
                heapq.heappush(heap, [next_distance, next])

    return distances

T = int(input())

for tc in range(1, T+1):
    N, E = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(E)]
    # print(edges)
    adj_list = {v : [] for v in range(N+1)}
    # print(adj_list)
    for s, e, w in edges:
        adj_list[s].append([e, w])
    # print(adj_list)

    res = dijkstra(adj_list, start=0)
    print(f'#{tc} {res.get(N)}')
