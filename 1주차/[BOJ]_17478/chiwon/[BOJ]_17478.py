# 문제
# 평소에 질문을 잘 받아주기로 유명한 중앙대학교의 JH 교수님은 학생들로부터 재귀함수가 무엇인지에 대하여 많은 질문을 받아왔다.
# 매번 질문을 잘 받아주셨던 JH 교수님이지만 그는 중앙대학교가 자신과 맞는가에 대한 고민을 항상 해왔다.
# 중앙대학교와 자신의 길이 맞지 않다고 생각한 JH 교수님은 결국 중앙대학교를 떠나기로 결정하였다.
# 떠나기 전까지도 제자들을 생각하셨던 JH 교수님은 재귀함수가 무엇인지 물어보는 학생들을 위한 작은 선물로 자동 응답 챗봇을 준비하기로 했다.
# JH 교수님이 만들 챗봇의 응답을 출력하는 프로그램을 만들어보자.

# 입력
# 교수님이 출력을 원하는 재귀 횟수 N(1 ≤ N ≤ 50)이 주어진다.

# 출력
# 출력 예시를 보고 재귀 횟수에 따른 챗봇의 응답을 출력한다.

# 예제 입력 1 
# 2

# 예제 출력 1 
# 어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.
# "재귀함수가 뭔가요?"
# "잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.
# 마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.
# 그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."
# ____"재귀함수가 뭔가요?"
# ____"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.
# ____마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.
# ____그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."
# ________"재귀함수가 뭔가요?"
# ________"재귀함수는 자기 자신을 호출하는 함수라네"
# ________라고 답변하였지.
# ____라고 답변하였지.
# 라고 답변하였지.

#=============================================================================================================

def story(iteration):
    
    # 글로벌에 선언한 언더바 갯수의 초안을 불러옴
    global number

    # 반복이 작아질 때 오히려 언더바가 많아져야 하므로 빼기를 써서 구현(2일 때 0에 8개 / 1에 4개 / 2에 0개)
    count = '_'*(number-4*iteration)

    # iteration이 0이면 _ 8개 + 출력
    if iteration == 0:
        print(f'{count}"재귀함수가 뭔가요?"')
        print(f'{count}"재귀함수는 자기 자신을 호출하는 함수라네"')
        print(f'{count}라고 답변하였지.')
        return 
    
    # 0이 아닐 때 반복해주는 문자열
    print(f'{count}"재귀함수가 뭔가요?"')
    print(f'{count}"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.')
    print(f'{count}마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.')
    print(f'{count}그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."')
    
    # 반복을 만들어주는 재귀함수 !
    story(iteration - 1)
    print(f'{count}라고 답변하였지.')

# 반복횟수 입력
N = int(input())

# _의 갯수를 위한 초석(iteration이 작아질 때 오히려 언더바는 더 많아져야 하므로, 글로벌에 큰 기준을 세우고 빼주는 느낌)
number = 4*N

print('어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.')
story(N)

# 버전 2

#     if iteration == 0:
#         print('"재귀함수가 뭔가요?"')
#         print('"재귀함수는 자기 자신을 호출하는 함수라네"')
#         return print('라고 답변하였지.')

#     for i in range(iteration+1):
#         number = '_'* (4*i)
#         print(f'{number}')
#         print(f'{number}재귀함수가 뭔가요?')
#         print(f'{number}"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.')
#         print(f'{number}마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.')
#         print(f'{number}그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."')
#         # story(iteration - 1)
#         print(f'{number}라고 답변하였지.')
# print('어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.')
# print(story(N))