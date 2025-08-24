'''
    N개의 섬들을 연결하는 교통시스템 설계 프로젝트 진행
        - 모든 섬을 해저터널로 연결하는 것이 목표
        - 해저터널은 반드시 두 섬을 선분으로 연결하며,
        - 두 해저 터널이 교차된다고 하더라도 물리적으로는 연결되지 않는 것으로 가정
        - 해저터널 건설로 인해 파괴되는 자연을 위해 다음과 같은 환경 부담금 정책 있음
            - 환경 부담 세율(E)과 각 해저터널 길이(L)의 제곱의 곱(E*L^2)만큼 지불
        - 총 환경 부담금을 최소로 지불하며, 모든 섬을 연결할 수 있는 교통 시스템 설계

    입력
        1. T : 테스트 케이스 수
        2. N : 섬의 개수 (1 <= N <= 1000)
        3. X : 각 섬들의 정수인 X 좌표 (0 <= X <= 1000000)
        4. Y : 각 섬들의 정수인 Y 좌표 (0 <= Y <= 1000000)
        5. E : 해저터널 건설의 환경 부담 세율 실수 (0 <= E <= 1)

    출력
        - #{tc} {모든 섬들을 잇는 최소 환경 부담금을 소수 첫째 자리에서 반올림한 정수 형태}
'''

def find_set(x):
    if x != parent[x]:
        parent[x] = find_set(parent[x])
    return parent[x]


def union(x, y):
    root_x = find_set(x)
    root_y = find_set(y)
    if root_x != root_y:
        parent[root_y] = root_x


def mst_kruskal(temp):
    mst = [] # 최소 신장 트리를 저장할 리스트 생성
    # 가중치 값을 기준으로 temp 리스트 정렬
    temp.sort(key=lambda x: x[2])
    for tp in temp:
        # 각 좌표 번호와 가중치를 각자 변수에 저장
        s, e, w = tp
        # 두 좌표의 부모 노드가 다르면 union 실행
        # 실행 후 mst 리스트에 저장
        if find_set(s) != find_set(e):
            union(s, e)
            mst.append(tp)
            print(mst)
    return mst

# import sys
# sys.stdin = open('re_sample_input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    x_list = list(map(int, input().split()))
    y_list = list(map(int, input().split()))
    # 각 좌표의 x,y 좌표 저장할 리스트 생성
    lst = []
    for i in range(N):
        lst.append([x_list[i], y_list[i]])

    # 환경 부담율
    E = float(input())

    # 모든 노드 간의 간선 정보를 기록한다.
    parent = [i for i in range(N)]
    temp = [] # 두 좌표를 선택해 그 좌표들의 거리를 저장할 리스트 생성

    # 각 좌표들의 조합 생성
    for i in range(N):
        for j in range(i + 1, N):
            # 가중치 : 두 좌표 거리의 제곱값
            w = (lst[i][0] - lst[j][0]) ** 2 + (lst[i][1] - lst[j][1]) ** 2
            temp.append((i, j, w))

    # 가중치 최솟값 찾기
    result = mst_kruskal(temp)
    total = 0

    # 길이의 제곱 총합 구하기
    for re in result:
        total += re[2]

    ans = E * total

    print(f'#{tc} {round(ans)}')
