# 명령 갯수를 받기

def empty():
    if len(stack) == 0:
        return 1
    
    else: return 0

def top():
    if len(stack) == 0:
        return -1
    
    else: return stack[len(stack)-1]

def size():
    return len(stack)

def pop():
    if len(stack) == 0:
        return -1
    else:
        return stack.pop()

# N갯수 받기
N = int(input())

# 스택 설정
stack = []

# 딕셔너리로 명령 모음 만들기
dict = {
    'pop' : pop,
    'size' : size,
    'empty' : empty,
    'top' : top   
}

 

for _ in range(N):

    # 명령 받기    
    order = input()

    # push만 형식이 다르고, 숫자도 받아줘야 하기 때문에 if문으로 뺴주기
    if ' ' in order:
        order, number = order.split()
        stack.append(int(number))

    # 나머지는 딕셔너리에서 찾아서 적용
    else:
        print(dict[order]())