# import sys
# sys.stdin = open('sample_input.txt')

def floyd_warshall(graph):
    for mid in range(N):
        for start in range(N):
            for end in range(N):
                Dik = graph[start][mid]
                Dkj = graph[mid][end]
                Dij = graph[start][end]
                if Dik + Dkj < Dij:
                    graph[start][end] = Dik + Dkj
    return graph


T = int(input())
for test_case in range(1, T+1):
    N = int(input()) # N: 노드의 개수
    adj_matrix = [list(map(int, input().split())) for _ in range(N)] # [시작정점, 도착정점, 비용]

    # 초기화
    INF = float('inf')
    for x in range(N):
        for y in range(N):
            if x == y:
                continue
            if adj_matrix[x][y] == 0:
                adj_matrix[x][y] = INF

    result = floyd_warshall(adj_matrix)

    max_value = -INF
    for i in range(N):
        for j in range(N):
            max_value = max(max_value, result[i][j])

    print(f'#{test_case} {max_value}')