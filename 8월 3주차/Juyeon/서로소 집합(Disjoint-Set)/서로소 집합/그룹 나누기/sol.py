'''
    같은 조에 참여하고 싶은 사람끼리 두 사람의 출석 번호를 종이에 적어 제출함
    한 조의 인원에 제한을 두지 않았기 때문에,
    한 사람이 여러 장의 종이를 제출하거나 여러 사람이 한 사람을 지목한 경우 모두 같은 조가 됨.

    ex)
        1-2, 1-3이 같은 조가 되고 싶다고 하면, 1-2-3이 같은 조가 됨.
        번호를 적지도 않고 다른 사람에게 지목되지도 않은 사람은 단독으로 조를 구성함.

    1 ~ N번까지의 출석번호가 있고, M장의 신청서가 제출되었을 때 전체 몇 개의 조가 만들어지는지 출력하는 프로그램

    입력
        1. T : 테스트 케이스
        2. N : 학생 수 / M : 신청서 수 (2 <= N <= 100, 1 <= M <= 100)
        3. M쌍의 번호가 주어짐

    출력
        - #{tc} {조 개수}
'''


import sys
sys.stdin = open('sample_input.txt')

def make_set(n):
    return [i for i in range(n + 1)]


def find_set_pc(x):
    if x == parent[x]:
        return parent[x]

    parent[x] = find_set_pc(parent[x])
    return parent[x]
    # return find_set(parent[x])


def union(x, y):
    root_x = find_set_pc(x)
    root_y = find_set_pc(y)

    if root_x != root_y:
        parent[max(root_x, root_y)] = min(root_x, root_y)


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    parent = make_set(N)
    # print(parent)
    # ★ M쌍(= 2*M개 숫자)을 전부 모을 때까지 읽기
    nums = []
    while len(nums) < 2 * M:
        nums += list(map(int, input().split()))

    for i in range(0, 2 * M, 2):
        union(nums[i], nums[i + 1])

    # ★ 모든 노드에 대해 최종 루트로 정규화
    for i in range(1, N + 1):
        find_set_pc(i)

    # 방법 B: 고유 루트값 종류 수
    groups = len(set(parent[1:]))

    print(f'#{tc} {groups}')
