'''
초기에 {1}, {2}, ... {n} 이 각각 n개의 집합을 이루고 있다.

여기에 합집합 연산과, 두 원소가 같은 집합에 포함되어 있는지를 확인하는 연산을 수행하려고 한다.
연산을 수행하는 프로그램을 작성하시오.

n(1≤n≤1,000,000), m(1≤m≤100,000)

합집합은 0 a b의 형태로 입력이 주어진다.
두 원소가 같은 집합에 포함되어 있는지를 확인하는 연산은 1 a b의 형태
이는 a와 b가 같은 집합에 포함되어 있는지를 확인하는 연산이다.

a와 b는 n 이하의 자연수이며 같을 수도 있다.
각 테스트 케이스마다 1로 시작하는 입력에 대해서 같은 집합에 속해있다면 1을, 아니면 0을 순서대로 한줄에 연속하여 출력한다.

<문제풀이>
각자 n개의 집합을 이루고 있음.

아래의 m개의 
합집합 -> 0 a b
같은 집합에 포함되어 있는지 확인 -> 1 a b
'''
import sys
sys.stdin = open('input.txt', 'r')


def find_set(x):
    if parent[x] != x:
        parent[x] = find_set(parent[x])
    return parent[x]
    
def union(x,y):

    root_x = find_set(x)
    root_y = find_set(y)

    if root_x != root_y:
        parent[root_y] = root_x

T = int(input())

for tc in range(1, T+1):
    
    # n, m 입력 받기
    n, m = map(int, input().split())
    
    arr = [list(map(int, input().split())) for _ in range(m)]

    parent = list(range(n+1))

    result = ''
    for item in arr:
        oper, x, y = item

        if oper == 0:
            union(x,y)
        
        else:
            root_x = find_set(x)
            root_y = find_set(y)

            if root_x == root_y:
                result += '1'
            
            else:
                result += '0'
    
    print(f'#{tc} {result}')
