import sys
sys.stdin = open('input.txt', 'r')

from collections import deque


# 데이터 조회용 코드
def max_data():
    T = int(input())
    for test_case in range(1, T + 1):
        data = list(map(int, input().split()))
        data = data[1:]
        print(f'#{test_case} {min(data)} {max(data)}')


# BFS로 탐색하면서 데이터 탐색
# 해당 데이터까지 걸린 길이를 합산해서 반환
def BFS(search_node, adj_list):
    q = deque([(0, search_node)])
    visited = [False] * len(adj_list)
    visited[search_node] = True

    result = 0
    while q:
        depth, node = q.popleft()
        result += depth
        for i in adj_list[node]:
            if not visited[i]:
                q.append((depth+1, i))
                visited[i] = True

    if sum(visited) != len(visited):
        return len(adj_list) * (len(adj_list) + 1)
    else:
        return result


def main():
    T = int(input())
    for test_case in range(1, T+1):
        # 입력받기
        # 받은 데이터를 인접 리스트로 변환
        data = list(map(int, input().split()))
        N = data[0]
        adj_list = [[] for _ in range(N)]
        for i in range(N):
            k = i * N + 1
            mat_line = data[k:k+N]
            for j in range(N):
                if mat_line[j]:
                    adj_list[i].append(j)


        result = N*(N+1) # 최댓값 정의
        # 각 노드마다 BFS를 돌리면서 거리의 합을 반환하고, 만약 그 값이 더 작다면 결과를 그 값으로 업데이트
        for i in range(N):
            result = min(result, BFS(i, adj_list))
        print(f'#{test_case} {result}')


if __name__ == "__main__":
    max_data()