from collections import deque

N, K = map(int, input().split())
queue = deque(list(range(1, N+1)))

ans = []
i = 0
while queue:
    if i < K-1 :
        value = queue.popleft()
        queue.append(value)
        i += 1
    else:
        value = queue.popleft()
        ans.append(value)
        i = 0

print(f"<{', '.join(map(str, ans))}>")