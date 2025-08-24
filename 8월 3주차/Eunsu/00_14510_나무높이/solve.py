# 각각 H의 높이를 가지는 N개의 나무
# 하루에 한 번 물주기 가능 -> 물 안주기: 나무의높이+0, 홀수날: 나무의높이+1, 짝수날:나무의높이+2
# 모든 나무의 키가 처음에 가장 키가 컸던 나무와 같아지도록 하는 최소 날짜 수?

### => ACCEPT

# import sys
# sys.stdin = open('sample_input.txt')

T = int(input())
for test_case in range(1, T + 1):
    numbers = int(input())  # N: 나무의 개수 (2 <= N <= 100)
    heights = list(map(int, input().split()))  # H: 나무의 높이 (1 <= H <= 120)

    # 각 나무와 높이가 가장 큰 나무의 차이 구하기
    tallest_tree = max(heights)
    difference = sum(tallest_tree-height for height in heights)
    print(difference)

    # 물 주기 할 홀수날, 짝수날
    odd_day = 0
    even_day = 0

    # 홀수날, 짝수날 번갈아가며 주는 것이 이득이므로 처음에는 모든 날 물 주기
    if difference >= 3:
        odd_day += difference // 3
        even_day += difference // 3
        difference %= 3
    print(difference)

    # 남은 날에 따라 홀수날 또는 짝수날에 물 주기
    if difference == 2:
        even_day += 1
    elif difference == 1:
        odd_day += 1
    print('odd_day', odd_day)
    print('even_day', even_day)

    # 최소 날짜 수 계산
    if even_day > odd_day:
        result = even_day * 2
    elif even_day < odd_day:
        result = odd_day * 2 - 1
    else:
        result = even_day * 2

    print(f'#{test_case} {result}')