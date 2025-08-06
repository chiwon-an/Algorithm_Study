def stack_action(action):
    if 'push' in action:
        act_list = action.split()
        num = int(act_list[1])
        stack.append(num)
    elif 'pop' in action:
        if stack:
            print(stack.pop())
        else:
            print(-1)        
    elif 'size' in action:
        print(len(stack))
    elif 'empty' in action:
        if not stack:
            print(1)
        else:
            print(0)
    elif 'top' in action:
        if stack:
            print(stack[-1])
        else:
            print(-1)
    return

N = int(input())
stack = []
for idx in range(1, N+1):
    action = input()
    stack_action(action)