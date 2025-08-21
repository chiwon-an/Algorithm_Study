'''
    마을에는 N명의 사람이 살고 있다.
    두 사람은 서로 알고 있는 관계일 수도, 아닐 수도 있다.
    두 사람이 서로 아는 관계거나 몇 사람을 거쳐서 알 수 있는 관계라면,
    이러한 사람들을 모두 다 묶어서 하나의 무리라고 한다.
    마을에 몇 개의 무리가 존재하는지 계산하는 프로그램을 작성하라.

    입력
        1. T : 테스트 케이스 수
        2. N : 마을에 사는 사람의 수 / M : 서로 알고 있는 사람의 관계 수
        3. 서로 알고 있는 두 사람의 번호

    출력
        - #{tc} {무리의 개수}
'''
import sys
sys.stdin = open('s_input.txt')

def make_set(n):
    return [i for i in range(n+1)]

def find_set_pc(x):
    if x == parent[x]:
        return parent[x]

    parent[x] = find_set_pc(parent[x])
    return parent[x]

def union(x, y):
    root_x = find_set_pc(x)
    root_y = find_set_pc(y)
    if root_x != root_y:
        parent[root_y] = root_x

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    parent = make_set(N)
    for i in range(M):
        x, y = map(int, input().split())
        union(x, y)

    # print(parent)

    groups = { find_set_pc(i) for i in range(1, N+1)}
    print(f'#{tc} {len(groups)}')
    # print(parent)
    # print(f'#{tc} {len(set(parent))-1}')
