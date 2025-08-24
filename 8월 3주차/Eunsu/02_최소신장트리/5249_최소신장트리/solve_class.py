# import sys
# sys.stdin = open('sample_input.txt')

class DisjointSet:
    def __init__(self, v):
        self.p = [0] * (len(v)+1)
        self.rank = [0] * (len(v)+1)

    def make_set(self, x):
        self.p[x] = x
        self.rank[x] = 0

    def find_set(self, x):
        if x != self.p[x]:
            self.p[x] = self.find_set(self.p[x])
        return self.p[x]

    def union(self, x, y):
        px = self.find_set(x)
        py = self.find_set(y)
        if px != py:
            if self.rank[px] < self.rank[py]:
                self.p[px] = py
            elif self.rank[px] > self.rank[py]:
                self.p[py] = px
            else:
                self.p[py] = px
                self.rank[px] += 1

def mst_kruskal(vertices, edges):
    '''
        1. 모든 간선을 가중치 기준으로 오름차순 정렬
        2. 가중치가 가장 작은 간선부터 하나씩 확인
        3. 두 정점이 같은 집합(=사이클 생성)인지 확인
            - 서로 다른 집합이면 → 간선 추가 (union)
            - 같은 집합이면 → 사이클 생기므로 버림
        4. 간선의 수가 (정점 수 - 1)개가 되면 종료
    '''

    mst = [] # 최소 신장 트리
    total_weight = 0

    edges.sort(key=lambda x: x[2]) # 가중치 기준 오름차순 정렬

    ds = DisjointSet(vertices) # DisjointSet 생성
    for v in range(len(vertices)+1):
        ds.make_set(v)

    for edge in edges:
        start, end, weight = edge
        if ds.find_set(start) != ds.find_set(end):
            ds.union(start, end)
            total_weight += weight
            mst.append(edge)

    return total_weight, mst


T = int(input())
for test_case in range(1, T+1):
    V, E = map(int, input().split()) # V: 정점, E: 간선
    vertices = [i for i in range(1, V+1)] # 정점 집합
    edges = [list(map(int, input().split())) for _ in range(E)] # [시작정점, 도착정점, 가중치]

    mst_weight, mst_edges = mst_kruskal(vertices, edges) # Kruskal 알고리즘

    print(f'#{test_case} {mst_weight}')