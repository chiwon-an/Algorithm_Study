'''
    N개의 노드로 구성된 유향 그래프에 대해 인접 노드로 이동하는 비용을 기록한 인접 행렬이 주어진다.
    모든 노드 i에 대해 다른 노드 j로 이동하는 경로가 있는 경우 최소 이동 비용을 구했을 때, 이 중 가장 큰 값을 출력하는 프로그램

    i에서 j로 이동할 때 다른 모든 노드를 지나야 하는 것은 아니며,
    인접한 노드 사이 비용이 음수인 경우는 있으나 출발한 노드로 돌아왔을 때의 비용이 음수인 사이클이 존재하지 않는다.

    다음과 같은 그래프가 있을 때 인접 행렬과 이동 비용은 다음과 같다.

         0   27  44
        -5   0   62
         0   99  0

    입력
        1. T : 테스트 케이스 수 (1 <= T <= 50)
        2. N : 노드의 개수 (3 <= N <= 100)
        3. 출발 노드 i에 대해 다른 노드 j까지의 비용인 N개의 a_ij가 주어짐
           (-99 <= a_ij <= 99, i != j and a_ij == 0인 경우, 인접하지 않음)

    출력
        - #{tc} {최소 이동 비용을 구했을 때의 가장 큰 값}
'''
import sys
sys.stdin = open('sample_input.txt')

def floyd_warshall(graph):
    n = len(graph)
    for k_node in range(n):
        for start in range(n):
            for end in range(n):
                Dik = graph[start][k_node]
                Dkj = graph[k_node][end]
                Dij = graph[start][end]
                if Dik + Dkj < Dij:
                    graph[start][end] = Dik + Dkj

    return graph

INF = float('inf')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    adj_matrix = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i != j and adj_matrix[i][j] == 0:
                adj_matrix[i][j] = INF
    # print(adj_matrix)

    result = floyd_warshall(adj_matrix)
    # for row in result:
        # print(row)
        # print(max(row))
    max_value = 0
    for row in result:
        for i in row:
            # print(i)
            max_value = max(max_value, i)
     
    print(f'#{tc} {max_value}')