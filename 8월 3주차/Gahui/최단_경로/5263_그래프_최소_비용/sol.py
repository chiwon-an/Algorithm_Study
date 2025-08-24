import math

import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    # 거리를 저장할 2차원 리스트, 초기값은 무한대로 설정
    dist = [[math.inf] * N for _ in range(N)]

    # 1. 비용 표 초기화
    for i in range(N):
        row = list(map(int, input().split()))
        for j in range(N):
            if i == j:
                dist[i][j] = 0  # 자기 자신으로 가는 비용은 0
            elif row[j] != 0:
                dist[i][j] = row[j]  # 길이 있는 경우, 주어진 비용으로 설정

    # 2. 플로이드-워셜 알고리즘 적용
    # k = 거쳐가는 노드
    for k in range(N):
        # i = 출발 노드
        for i in range(N):
            # j = 도착 노드
            for j in range(N):
                # i에서 j로 가는 기존 비용 vs k를 거쳐 가는 새로운 경로 비용
                if dist[i][k] != math.inf and dist[k][j] != math.inf:
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    # 3. 정답(최댓값) 찾기
    max_cost = 0
    # 모든 경로가 계산된 dist 리스트에서 최댓값을 찾음
    for i in range(N):
        for j in range(N):
            # 경로가 존재하는 경우에만 최댓값 비교
            if dist[i][j] != math.inf:
                if dist[i][j] > max_cost:
                    max_cost = dist[i][j]

    print(f"#{tc} {max_cost}")