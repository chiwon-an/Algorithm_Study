import sys
sys.stdin = open('re_sample_input.txt', 'r')


def make_set(N):
    # 0번 인덱스는 사용 안 할 것이므로 N+1개의 정점 생성
    return [i for i in range(N)]


def find_set(x):
    if x == parent[x]:
        return parent[x]
    parent[x] = find_set(parent[x])
    return parent[x]


def union(x, y):
    x_root = find_set(x)
    y_root = find_set(y)
    if x_root != y_root:
        parent[y_root] = x_root


def make_edges(N, X, Y):
    # 가능한 모든 비용 찾아서 (시작 정점, 끝 정점, 가중치) 리스트에 추가
    edges = []
    for i in range(N):
        for j in range(N):
            if i >= j:
                continue
            distance = (X[i]-X[j])**2 + (Y[i]-Y[j])**2
            edges.append([i, j, distance])
    edges.sort(key=lambda x: x[2])
    return edges


def kruscal(edges, N, E):
    edge_count = 0
    total_cost = 0
    for start, end, dist in edges:
        start_parent = find_set(start)
        end_parent = find_set(end)
        if start_parent != end_parent:
            union(start, end)
            total_cost += dist * E
            edge_count += 1
            if edge_count == N-1:
                return total_cost
        else:
            continue


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    E = float(input())
    edges = make_edges(N, X, Y)
    parent = make_set(N)
    result = kruscal(edges, N, E)
    print(f'#{tc} {round(result)}')