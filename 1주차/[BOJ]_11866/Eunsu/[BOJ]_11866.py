### 11866. 요세푸스 문제 0 ###

from collections import deque

N, K = map(int, input().split())
queue = deque(range(1, N+1))

result = []
while queue:
    queue.rotate(-K+1)
    result.append(queue.popleft())

print('<' + ', '.join(map(str, result)) + '>')