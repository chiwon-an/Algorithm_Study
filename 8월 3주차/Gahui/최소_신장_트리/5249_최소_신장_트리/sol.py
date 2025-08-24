import sys
sys.stdin = open('sample_input.txt', 'r')


# 부모 찾는 함수
def find_set(x):
    if x == vertices[x]:
        return vertices[x]
    vertices[x] = find_set(vertices[x])
    return vertices[x]


# 합집합 연산하는 함수
def union(x, y):
    root_x = find_set(x)
    root_y = find_set(y)
    if root_x != root_y:
        vertices[root_y] = root_x


# kruscal 알고리즘
def mst_kruscal(vertices, edges):
    mst = []
    weight = 0
    edges.sort(key=lambda x: x[2])
    for edge in edges:
        s, e, w = edge
        if find_set(s) != find_set(e):
            union(s, e)
            weight += w
            mst.append(edge)
    return weight


# 풀이
T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(E)]
    # print(edges)
    vertices = list(range(V+1))
    # print(vertices)
    weight = mst_kruscal(vertices, edges)
    print(f'#{tc} {weight}')
