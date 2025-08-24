'''
    0번부터 V번까지의 노드와 E개의 간선을 가진 그래프 정보가 주어질 때,
    이 그래프로부터 최소신장트리를 구성하는 간선의 가중치를 모두 더해 출력하는 프로그램을 작성
    
    입력
        1. T : 테스트 케이스 수 (1 <= T <= 50)
        2. V : 마지막 노드번호 / E : 간선의 개수 (1 <= V <= 1000, 1 <= E <= 1,000,000)
        3. n1 : 시작 노드 / n2 : 끝 노드 / w : 가중치 (1 <= w <= 10)

    출력
        - #{tc} {최소신장트리를 구성하는 간선의 가중치들의 합}
'''

import sys
sys.stdin = open('sample_input.txt')

import heapq

def prim(vertices, edges):
    mst = [] # 최소 신장 트리 값을 받을 리스트 생성
    visited = set() # 방문한 곳은 가지 않도록 하기 위해 set 생성
    start_vertex = vertices[0]

    # start_vertex(0) 기준으로 갈 수 있는 노드를 (가중치, 현재 위치, 갈 수 있는 노드) 순서로 min_heap 리스트에 저장
    min_heap = [(w, start_vertex, e) for e, w in adj_list[start_vertex]]
    # 가중치, 현재 위치, 갈 수 있는 노드 순서대로 값이 작은 것부터 정렬
    # 가중치가 같은 경우, 갈 수 있는 노드 번호가 작은 것부터 정렬
    heapq.heapify(min_heap)
    visited.add(start_vertex)


    while min_heap:
        # print(min_heap)
        # min_heap 리스트의 첫번째 값을 가중치, 시작 노드, 끝 노드로 출력
        weight, start, end = heapq.heappop(min_heap)
        # 끝 노드를 방문한 적이 있다면 다음 반복문 진행
        if end in visited: continue

        # 방문한 적 없으면 visited에 추가
        visited.add(end)
        # mst 리스트에도 추가
        mst.append((start, end, weight))

        # 끝 노드를 시작 노드로 설정해서 방문한 적이 있는지 확인
        for next, weight in adj_list[end]:
            # 방문한 적 있으면 다음 반복문 진행
            if next in visited: continue
            # 방문한 적 없으면 min_heap 리스트에 (가중치, 시작 노드로 변경한 끝 노드, 다음으로 방문할 노드) 저장
            heapq.heappush(min_heap, (weight, end, next))

    # 반복문 종료 시 mst 반환
    return mst


T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    edges = []
    for _ in range(E):
        edges.append(list(map(int, input().split())))
    # print(edges)
    vertices = list(range(V+1))
    adj_list = {v : [] for v in vertices}
    for n1, n2, w in edges:
        adj_list[n1].append((n2, w))
        adj_list[n2].append((n1, w))
    # print(adj_list)

    result = prim(vertices, edges)
    # print(result)
    
    # mst 리스트에 저장했던 2차원 배열 중 가중치들의 합 출력
    total = sum([result[i][2] for i in range(len(result))])
    print(f'#{tc} {total}')