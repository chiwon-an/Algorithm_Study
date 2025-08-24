'''
    N개의 섬들을 연결하는 교통시스템 설계 프로젝트 진행
        - 모든 섬을 해저터널로 연결하는 것이 목표
        - 해저터널은 반드시 두 섬을 선분으로 연결하며,
        - 두 해저 터널이 교차된다고 하더라도 물리적으로는 연결되지 않는 것으로 가정
        - 해저터널 건설로 인해 파괴되는 자연을 위해 다음과 같은 환경 부담금 정책 있음
            - 환경 부담 세율(E)과 각 해저터널 길이(L)의 제곱의 곱(E*L^2)만큼 지불
        - 총 환경 부담금을 최소로 지불하며, 모든 섬을 연결할 수 있는 교통 시스템 설계

    입력
        1. T : 테스트 케이스 수
        2. N : 섬의 개수 (1 <= N <= 1000)
        3. X : 각 섬들의 정수인 X 좌표 (0 <= X <= 1000000)
        4. Y : 각 섬들의 정수인 Y 좌표 (0 <= Y <= 1000000)
        5. E : 해저터널 건설의 환경 부담 세율 실수 (0 <= E <= 1)

    출력
        - #{tc} {모든 섬들을 잇는 최소 환경 부담금을 소수 첫째 자리에서 반올림한 정수 형태}
'''
import sys
sys.stdin = open('re_sample_input.txt')

def prim(vertices):
    N_local = len(vertices)
    INF = 10**30

    visited = [False] * N_local
    min_d2 = [INF] * N_local
    parent = [-1] * N_local

    start_idx = 0
    min_d2[start_idx] = 0

    for _ in range(N_local):

        u = -1
        best = INF
        for i in range(N_local):
            if not visited[i] and min_d2[i] < best:
                best = min_d2[i]
                u = i

        visited[u] = True

        ux, uy = X[vertices[u]], Y[vertices[u]]
        for v in range(N_local):
            if not visited[v]:
                dx = ux - X[vertices[v]]
                dy = uy - Y[vertices[v]]
                d2 = dx**2 + dy**2
                if d2 < min_d2[v]:
                    min_d2[v] = d2
                    parent[v] = u

    mst = []
    for v in range(N_local):
        if parent[v] != -1:
            s_idx = vertices[parent[v]]
            e_idx = vertices[v]
            mst.append([s_idx, e_idx, min_d2[v]])

    return mst

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))

    island = []
    for i in range(len(X)):
        island.append([i, X[i], Y[i]])

    vertices = list(range(N))

    E = float(input())

    result = prim(vertices)

    L = [result[i][2] for i in range(len(result))]
    cost = sum(L) * E

    print(f'#{tc} {round(cost)}')