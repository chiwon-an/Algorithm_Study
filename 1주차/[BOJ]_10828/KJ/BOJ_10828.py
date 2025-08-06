import sys
input = sys.stdin.readline

N = int(input())

def commander(x):
    if x == 'top':
        if not stack:
            print(-1)
        else:
            print(stack[-1])
    elif x == 'size':
        print(len(stack))
    elif x == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    elif x == 'pop':
        if not stack:
            print(-1)
        else:
            print(stack.pop())


stack = []
for _ in range(N):
    given = input().split()
    if len(given) == 2:
        stack.append(int(given[1]))
    else:
        commander(given[0])