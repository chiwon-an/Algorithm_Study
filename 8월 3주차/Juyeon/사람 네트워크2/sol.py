'''
    주어진 사람 네트워크에서 누가 가장 영향력이 있는 사람인지를 알 수 있는 척도로서 다음을 분석하는 프로그램 작성
    단, N은 입력 사람 네트워크 (그래프)의 노드 수

    Closeness Centrality(CC) : Closeness는 네트워크 상에서 한 사용자가 다른 모든 사람에게 얼마나 가까운가를 나타낸다.
    따라서 사용자 i의 CC(i)는 다음과 같이 계산된다.
        - CC(i) = sum(dist(i, j)) <dist(i,j)는 노드 i로부터 노드 j까지의 최단 거리>

    예제 1)
               1
              /  \
             2 -- 3
             | \  |
             4   5

        node     cc
        1        6
        2        4
        3        5
        4        7
        5        6
        사람 네트워크에서 사용자 2의 dist 합이 가장 작으며,
        CC(2) = 4임을 통해 사용자 2가 모든 사용자들로부터 가장 가까운 사용자이다.
    
    제약 사항
        1. 입력으로 주어지는 사람 네트워크에서 노드 자신을 연결하는 간선은 없다.
        2. 사람 네트워크는 하나의 연겨 요소로 구성되어 있다.
        3. 사람 네트워크의 최대 사용자 수(N) <= 1000
        4. 테스트 케이스들은 아래의 그룹들로 이루어져 있다.
            그룹 1) 싸이클이 없고 N <= 10인 경우
            그룹 2) 싸이클이 없고 10 < N <= 100인 경우
            그룹 3) 싸이클이 있고 N <= 10인 경우
            그룹 4) 싸이클이 있고 10 < N <= 100인 경우
            그룹 5) 모든 경우가 존재하고 100 < N <= 1000인 경우

    입력
        1. T : 테스트 케이스 수
        2. N : 사람의 수(양의 정수) / 사람 네트워크의 인접 행렬이 행 우선 순으로 주어짐

    출력
        - #{tc} {주어진 사람 그래프에서 사람들의 CC 값들 중에서 최솟값}
'''
import sys
sys.stdin = open('input.txt')

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

T = int(input())

INF = float('inf')

for tc in range(1, T+1):
    N, *data = map(int, input().split())
    adj_matrix = [data[i:i+N] for i in range(0, len(data), N)]
    for i in range(N):
        for j in range(N):
            if i !=j and adj_matrix[i][j] == 0:
                adj_matrix[i][j] = INF
    # print(adj_matrix)

    result = floyd_warshall(adj_matrix)

    # for row in result:
    #     print(row)

    result_total = [sum(result[i]) for i in range(N)]
    print(f'#{tc} {min(result_total)}')

