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