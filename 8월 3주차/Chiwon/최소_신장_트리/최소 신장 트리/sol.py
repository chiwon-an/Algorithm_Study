'''
그래프에서 사이클을 제거하고 모든 노드를 포함하는 트리를 구성할 때, 가중치의 합이 최소가 되도록 만든 경우를 최소신장트리라고 한다.

0번부터 V번까지의 노드와 E개의 간선을 가진 그래프 정보가 주어질 때, 이 그래프로부터 최소신장트리를 구성하는 간선의 가중치를 모두 더해 출력하는 프로그램을 만드시오.


[입력]

첫 줄에 테스트 케이스의 개수 T가 주어지고, 테스트 케이스 별로 첫 줄에 마지막 노드번호 V와 간선의 개수 E가 주어진다.

다음 줄부터 E개의 줄에 걸쳐 간선의 양 끝 노드 n1, n2, 가중치 w가 차례로 주어진다.

1<=T<=50, 1<=V<=1000, 1<=w<=10, 1<=E<=1000000

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

KRUSKAL 알고리즘
        1. 가중치를 오름차순 정렬한다.
        2. 그 순서대로 간선들을 선택하는데
        3. 2에서 선택한 간선의 시작, 종료 노드가 같은 대표자가 아니어야 한다.
        4. 2와 3을 선택된 간선이 n-1개가 될 때까지 반복한다.
'''
import sys
sys.stdin = open('sample_input.txt', 'r')

# 노드의 대표 노드 찾아주기
def find_set(x):

    if x == vertices[x]:
        return vertices[x]

    return find_set(vertices[x])

# 노드 두 개 비교할 때 같은 집합에 있는 노드가 아니면 y의 대표 노드를 x의 대표 노드로 바꿔주기 and 1로 반환
def union(x,y):

    root_x = find_set(x)
    root_y = find_set(y)

    if root_x != root_y:
        #  원소 y가 속한 대표 노드를 x의 대표 노드로 바꾸기
        vertices[root_y] = root_x
        return 1

# kruskal 알고리즘
def mst_kruskal(edges):

    global mst
    
    # 가중치에 따라 오름차순으로 정렬된 간선정보들을 앞에서부터 하나씩 판단.
    for item in edges:
        start, end = item[0], item[1]
        
        # union으로 두 정점을 해봤을 때, 다른 노드라고 생각이 되면 return1로 받아졌고, 그건 사용할 간선이기 때문에 mst에 append
        # 1이 아니라면, 그건 이미 같은 집합 내에 있는 정점이기 때문에 가중치가 크므로 이건 제거
        if union(start, end) == 1:
            mst.append(item)

T = int(input())

for tc in range(1, T+1):

    # V는 노드의 수 / E는 간선의 갯수
    V, E = map(int, input().split())

    edges = []

    # start, end, weight로 튜플을 만들어서 edges에 넣어주기
    for _ in range(E):

        start, end, weight = map(int, input().split())
        edges.append((start, end, weight))

    # 가중치를 기준으로 정렬하기
    edges.sort(key=lambda x: x[2])

    # 정답을 모을 리스트 선언
    mst = []

    # make_set 정접 집합
    vertices = list(range(V+1))

    # 에지를 위 함수에 넣어주기
    mst_kruskal(edges)

    # 결과가 가중치의 합이니까 갱신을 위한 변수 선언
    ans = 0

    # 만든 트리의 간선의 가중치를 누적합
    for i in range(len(mst)):
        ans += mst[i][2]

    # print(mst)
    # print(vertices)
    print(f'#{tc} {ans}')