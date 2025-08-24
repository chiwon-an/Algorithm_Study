# import sys
# sys.stdin = open('re_sample_input.txt')

def prim():
    visited = [False] * N # 방문 확인
    min_cost = [float('inf')] * N # 초기화
    min_cost[0] = 0 # 시작 정점
    total = 0 # 비용

    # MST에 섬 추가
    for _ in range(N):
        min_value = float('inf')
        u = -1

        # 방문하지 않은 최소 비용 섬 선택
        for i in range(N):
            if not visited[i] and min_cost[i] < min_value:
                min_value = min_cost[i]
                u = i

        if u == -1: # 선택한 섬이 없는 경우
            break

        visited[u] = True # 방문 처리
        total += min_cost[u] # 최소 비용

        # 다른 섬까지의 비용 갱신
        for v in range(N):
            if not visited[v]:
                dist = (xs[u]-xs[v])**2 + (ys[u]-ys[v])**2
                if min_cost[v] > dist:
                    min_cost[v] = dist

    return round(total * E)


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    xs = list(map(int, input().split()))
    ys = list(map(int, input().split()))
    E = float(input())

    result = prim()
    print(f'#{test_case} {result}')