N, K = map(int, input().split())

people = list(range(1, N+1))
output = []
idx = 0
while people:
    idx = (idx + K - 1) % len(people)
    output.append(people.pop(idx))

res = ", ".join(map(str, output))
print(f"<{res}>")
