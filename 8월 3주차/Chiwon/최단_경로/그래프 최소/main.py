'''
N개의 노드로 구성된 유향 그래프에 대해 인접 노드로 이동하는 비용을 기록한 인접 행렬이 주어진다.

모든 노드 i에 대해 다른 노드 j로 이동하는 경로가 있는 경우 최소 이동 비용을 구했을 때,
이 중 가장 큰 값을 출력하는 프로그램을 만드시오.

i에서 j로 이동할 때 다른 모든 노드를 지나야 하는 것은 아니며,
인접한 노드 사이 비용이 음수인 경우는 있으나 출발한 노드로 돌아왔을 때의 비용이 음수인 사이클은 존재하지 않는다.

다음과 같은 그래프가 있을 때 인접 행렬과 이동 비용은 다음과 같다.


'''

import sys
sys.stdin = open('sample_input.txt', 'r')

def bellman_ford(graph, start):

    N = len(graph)


    # 최솟값으로 갱신할 거니까, 무한대로 초기값 설정
    # {0: inf, 1: inf, 2: inf}
    distances = {v: float('inf') for v in graph}

    # 시작 정점 거리 0 초기화
    distances[start] = 0

    # 마지막 정점을 제외한 횟수만큼 순회
    # n-1번 해주는 이유는 사이클 없는 경로에서 한 정점에서 다른 정점으로 갈 때 최대로 지나칠 수 있는 노드는 n-1개뿐이기 때문
    for _ in range(N-1):

        # 각 회차에서 간선을 전부 확인했는데도 아무 값도 갱신되지 않았다면 → 이미 최단 경로가 다 구해졌다는 뜻.
        updated = False

        # 각 정점별 인접 정점 순회
        for u in graph:
            # .items는 딕셔러니에서 키랑 벨류를 받아오는 메서드임. 여기
            for end, weight in graph[u].items():
                # print(end, weight)
                # print(f'#{v}, {next}, {weight}')


                # 만약 내가 지금 있는 노드가 inf가 아니고(이건 그냥 for문으로 돌기 때문에, 지금 내가 있는 곳이 간선으로 연결된 곳인가 판단이 필요)
                # 그리고 지금 있는 u 정점에서 갈 수 있는 end랑 weight를 받고,
                # 지금까지 짊어진 가중치와 end로 갈 때 필요한 가중치를 더했을 때 다음 값에 저장된 가중치 값보다 작으면 갱신
                if distances[u] != float('inf') and distances[u] + weight < distances[end]:
                    distances[end] = distances[u] + weight
                    updated = True

        if updated == False:
            break

    # 문제에선 음수싸이클이 없다고 했지만, 일단 한 번 해봄
    # for u in graph:
    #     # print(graph[u].items())
    #     for end, weight in graph[u].items():
    #         # 음수싸이클 확인하는 방법은 이미 위에서 다 끝났는데, 또 갱신해야 하는 값이 있다라면, 그건 음수싸이클임.
    #         if distances[u] != float('inf') and distances[u] + weight < distances[end]:
    #             print('음수 싸이클이 있습니다.')
    #             return False
    #         print(end, weight)

    return distances


T = int(input())

for tc in range(1, T+1):

    # 노드의 갯수
    N = int(input())

    # 가중치 리스트
    cost_list = [list(map(int, input().split())) for _ in range(N)]
    # print(cost_list)

    # 그래프 만들기
    adj_list = {v : {} for v in range(N)}

    # 인접 리스트 만들기
    for i in range(N):
        for j in range(N):
            # 여기가 살짝 헷갈린 부분임. 딕셔러니 내에 있는 딕셔너리에 넣을 때 어떻게 추가해야 하는지 확인
            if i != j and cost_list[i][j] == 0:
                continue

            adj_list[i][j] = cost_list[i][j]
    print(adj_list)
    # print(adj_list)
    '''
    {
    0: {0: 0, 1: 27, 2: 44},
    1: {0: -5, 1: 0, 2: 62},
    2: {1: 99, 2: 0}
    }
    '''

    '''
    bellman_ford(adj_list, 0)
    
    {
    0: {0: 0, 1: 27, 2: 44},
    1: {0: -5, 1: 0, 2: 62},
    2: {1: 99, 2: 0}
    }
    
    '''
    # 마지막은 최댓값을 구하는 거니까, -무한대로 설정
    ans = -float('inf')

    # 시작 지점이 정해진게 아니라 어디서든 시작할 수 있는 거기 때문에 모든 노드에서 시작을 해줌.
    for i in range(N):
        result = bellman_ford(adj_list, i)

        # print(result)
        for v in range(N):
            if v != i and result[v] != float('inf'):
                ans = max(ans, result[v])
    print(f'#{tc} {ans}')