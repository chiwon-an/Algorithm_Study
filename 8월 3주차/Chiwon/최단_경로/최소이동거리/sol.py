'''
A도시에는 E개의 일방통행 도로 구간이 있으며, 각 구간이 만나는 연결지점에는 0부터 N번까지의 번호가 붙어있다.

구간의 시작과 끝의 연결 지점 번호, 구간의 길이가 주어질 때, 0번 지점에서 N번 지점까지 이동하는데 걸리는 최소한의 거리가 얼마인지 출력하는 프로그램을 만드시오.

모든 연결 지점을 거쳐가야 하는 것은 아니다.

그림은 입력인 N=2, E=3, 시작과 끝 지점, 구간 거리가 아래와 같은 경우의 예이다.

0 1 1
0 2 6
1 2 1

'''

import sys
sys.stdin = open('sample_input (3).txt','r')
import heapq

def dijkstra(graph, start):

    distances = {v:float('inf') for v in range(N+1)}
    # print(distances)
    # {0: inf, 1: inf, 2: inf}

    distances[start] = 0

    heap = []

    heapq.heappush(heap, [0,start])
    visited = set()

    while heap:
        dist, currrent = heapq.heappop(heap)

        if currrent in visited or distances[currrent] < dist: continue
        visited.add(currrent)

        for next, weight in graph[currrent].items():
            next_distance = dist + weight

            if next_distance < distances[next]:
                distances[next] = next_distance
                heapq.heappush(heap, [next_distance, next])

    return distances






T = int(input())

for tc in range(1, T+1):
    #
    N, E = map(int, input().split())

    # start, end, length

    roads = [list(map(int, input().split())) for _ in range(E)]
    # print(roads)
    # [[0, 1, 1], [0, 2, 6], [1, 2, 1]]


    adj_list = {v : {}  for v in range(N+1)}
    # print(adj_list)
    # {0: {}, 1: {}, 2: {}}

    for road in roads:
        adj_list[road[0]][road[1]] = road[2]

    result = dijkstra(adj_list, 0)
    print(f'#{tc} {result[N]}')

    # print(adj_list)
    '''
    {
    0: {1: 1, 2: 6},
    1: {2: 1},
    2: {}
    }
    '''

