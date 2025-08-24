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
    # 모든 노드의 값이 inf인 딕셔너리 생성 [최소 거리를 저장할 딕셔너리]
    distances = {v : math.inf for v in graph}
    # print(distances)

    heap = []
    # heap에 [0, start=0] 저장
    heapq.heappush(heap, [0, start])
    # print(heap)
    visited = set() # 방문 체크할 set 생성
    visited.add(start)

    while heap:
        # print(heap)
        # print(distances)
        # 거리와 현재 위치를 각 변수에 저장 후 내보내기
        dist, current = heapq.heappop(heap)

        # 현재 위치를 방문한 적 있고 거리를 저장한 딕셔너리의 값이 dist보다 작으면 다음 반복문 진행
        if current in visited and distances[current] < dist : continue
        visited.add(current)

        # 인접 리스트에 저장한 끝 노드와 가중치
        for next, weight in graph[current]:
            # 현재 거리와 다음 거리를 합한 값
            next_distance = dist + weight
            # 이 값이 최소 거리를 저장할 리스트보다 작다면 다음 과정 실행
            if next_distance < distances[next]:
                distances[next] = next_distance
                # heap 리스트에 [거리, 다음 노드] 저장
                heapq.heappush(heap, [next_distance, next])

    return distances

T = int(input())

for tc in range(1, T+1):
    N, E = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(E)]
    # print(edges)
    # 인접 리스트 생성
    adj_list = {v : [] for v in range(N+1)}
    # print(adj_list)
    # 양방향이 아니므로 start, end 구분하고 리스트에 저장
    for s, e, w in edges:
        adj_list[s].append([e, w])
    # print(adj_list)

    res = dijkstra(adj_list, start=0)
    print(f'#{tc} {res.get(N)}')
