'''
N개의 나무가 있다. 초기의 각 나무의 키가 주어진다.
하루에 한 나무에 물을 줄 수 있다.
홀수 번째 날은 키가 1 자라고 짝수 번째 날은 키가 2 자란다.
모든 나무의 키가 처음에 가장 키가 컸던 나무와 같아지도록 할 수 있는 최소 날짜 수를 계산하라.
어떤 날에는 물을 주는 것을 하지 않을 수도 있다.

 

예를 들어 나무가 2그루이고 각각의 높이가 4와 2라고 하자.
첫째 날에 물을 주게 되면, 나무의 높이를 모두 4로 만들기 위해서는 3일째까지 물을 주어야 한다.
둘째 날은 아무 일도 안 하게 된다. 하지만, 첫째 날을 쉬고 둘째 날에 물을 주면 2일 만에 나무의 높이가 모두 4가 된다.

홀수 - 1
짝수 - 2
    
    # 홀수면 일단 1일씩 다 필요하긴 함.
    # 홀수를 따로 담고, 짝수를 따로 담기
    # 홀수를 하나씩 빼오고, 없다면 짝수에서 빼와서 -1을 해주고 홀수에 넣기
    # 0이 되면 아예 없애주기
    # 만약 2를 줘야하는 날이 있어. 이날 홀수에 줘버리면 ? -> 3일이 걸리게 됨. 근데 안주고 짝수까지 기다리면? -> 2일이면 끝남
    # 만약 4를 줘야하는 날이 있어. 이날 홀수에 줘버리면 ? -> 4일이 걸리게 됨. 근데 안주고 짝수까지 기다리면? -> 4일이면 끝남
    # 만약 6를 줘야하는 날이 있어. 이날 홀수에 줘버리면 ? -> 6,4일이 걸리게 됨. 근데 안주고 짝수까지 기다리면? -> 6일이면 끝남
    # 만약 8를 줘야하는 날이 있어. 이날 홀수에 줘버리면 ? -> 8, 일이 걸리게 됨. 근데 안주고 짝수까지 기다리면? -> 8일이면 끝남
    # 2가 남은게 아닌 이상 짝수 남은 것들도 홀수날에 물을 주는게 이득임.
    
'''

import sys
sys.stdin = open('input.txt', 'r')

def find_optimal_day():

    global day

    # 만약 둘 다 비어있다면?
    if len(zac) == 0 and len(hol) == 0:
        return day

    # 둘 다 0이 될 때까지 반복해라.
    while len(zac) != 0  or len(hol) != 0:
        
        # 하루씩 더해주기
        day += 1

        # 홀수 날
        if day % 2 == 1:
        
            # 둘 다 아직 빈 자리가 없거나 홀수에만 있을 경우
            if len(hol) != 0:

                cur_hol = hol.pop()
                curr = cur_hol - 1

                # 0이 아닐 경우 1을 빼고 짝수에 더해주기
                if curr == 0:
                    continue
                
                else:
                    zac.append(curr)

            # 홀수에 자리가 없는 경우
            elif len(hol) == 0:
                
                # 남은게 2면 그냥 1더해주는게 맞음
                if sum(zac) == 2:
                    day = day + 1
                    return

                # 남은게 2가 아니라면 하나 꺼내서 작업해주기
                else: 
                    cur_zac = zac.pop()
                    curr = cur_zac - 1
                    hol.append(curr)


        # 짝수날
        else:
            # 둘 다 남았거나 짝수만 남았을 경우
            if len(zac) != 0:

                cur_zac = zac.pop()
                curr = cur_zac -2

                # 0이 아니라면 하나 2로 빼주고 다시 짝수로 넣어주기
                if curr != 0:
                    zac.append(curr)
            
            # 홀수만 남았을 경우
            elif len(zac) == 0:
                continue
    
    return



T = int(input())

for tc in range(1, T+1):

    # 나무의 갯수
    N = int(input())

    # 나무들 입력받기
    trees = list(map(int, input().split()))

    # 가장 큰 값 정의
    target = max(trees)
    # print(target)

    # 높은 값에서 얼마만큼 커져야 하는지 모은 배열
    heights = []

    for i in range(N):
        height = target - trees[i]

        if height != 0:
            heights.append(height)
    

    zac = []
    hol = []

    day = 0

    for height in heights:

        if height % 2 == 0:
            zac.append(height)
        
        else:
            hol.append(height)
    
    find_optimal_day()
    
    print(f'#{tc} {day}')