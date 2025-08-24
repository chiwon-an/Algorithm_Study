# import sys
# sys.stdin = open('input.txt')

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
    data = list(map(int, input().split()))

    N = data[0] # N: 사람 수
    adj_matrix = [data[N*i+1:N*i+N+1] for i in range(N)] # 인접 행렬

    INF = float('inf')
    for x in range(N):
        for y in range(N):
            if x != y and adj_matrix[x][y] == 0:
                adj_matrix[x][y] = INF

    cc = floyd_warshall(adj_matrix)
    result = min(sum(c) for c in cc)

    print(f'#{test_case} {result}')