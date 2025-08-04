# N,M 입력 받기
N, M = map(int, input().split())

# 바스켓 N+1개로 설정
basket = [0]*(N+1)

# basket에 각 번호에 맞게 넣어두기
for i in range(1,N+1):
    basket[i] = i


for _ in range(M):
    idx_1, idx_2 = map(int, input().split())
    basket[idx_1], basket[idx_2] = basket[idx_2], basket[idx_1]

print(*basket[1:])