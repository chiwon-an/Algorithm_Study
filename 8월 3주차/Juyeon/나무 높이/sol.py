'''
    N개의 나무가 있다.
    초기의 각 나무의 키가 주어진다.
    하루에 한 나무에 물을 줄 수 있다.
    홀수 날에는 +1, 짝수 날에는 +2
    모든 나무의 키가 처음에 가장 키가 처음에 가장 키가 컸던 나무에 같아지도록 할 수 있는 최소 날짜 수를 계산하라.
    <물을 주지 않는 날이 있을 수 있다.>

    제약 사항
        1. 2 <= N (나무의 개수) <= 100
        2. 1 <= (초기 나무의 높이) <= 120

    입력
        1. T : 테스트 케이스 수
        2. N : 나무의 개수
        3. 나무들의 높이

    출력
        - #{tc} {모든 나무의 키가 가장 키가 컸던 나무와 같아지도록 할 수 있는 최소 날짜}
'''
import sys
sys.stdin = open('Sample_input.txt')

def diff(lst):
    highest = max(lst)
    lst_diff = []
    for i in range(N):
        if highest - lst[i] == 0:
            continue
        lst_diff.append(highest - lst[i])
    lst_diff.sort()
    return lst_diff
    # print(tree_diff)

def watering(lst):

    if not lst:
        return 0

    odd_need = sum(1 for d in lst if d % 2 == 1) # 홀수 날이 최소 몇 번 필요한지
    two_need = sum(d // 2 for d in lst) # 짝수 날이 최소 몇 번 필요한지
    # print(odd_need)
    # print(two_need)

    D = 0
    while True:
        E = D // 2   # 짝수 날 개수
        O = (D + 1) // 2  # 홀수 날 개수

        leftover_two = max(0, two_need - E)
        # 필요한 짝수 날이 실제 짝수 날보다 적을 때, 남은 만큼 홀수 날 2번으로 대신함
        need_odd_days = odd_need + 2 * leftover_two
        # 총 몇 번의 홀수 날이 필요한가 <odd_need + 짝수 날이 모자라서 홀수 날이 대신해야 하는 날>

        if O >= need_odd_days:
            return D
        # D일 동안 실제 가능한 홀수 날 개수(O)가 총 필요 홀수 날 개수 이상이면 D일이면 가능하다는 의미

        D += 1
    # return max(2 * E, 2 * O - 1)

T = int(input()) # 테스트 케이스 수

for tc in range(1, T+1):
    N = int(input()) # 나무 개수
    tree_list = list(map(int, input().split()))
    tree_diff = diff(tree_list)
    print(f'#{tc} {watering(tree_diff)}')

