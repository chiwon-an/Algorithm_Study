# 입력 받기
N, K = map(int, input().split())

lst = []
result = []
temp = 0
idx = 0

# 리스트 생성
for i in range(1,N+1):
    lst.append(i)
# print(lst) -> [1, 2, 3, 4, 5, 6, 7]

# 길이가 짧아지는 것에 따른 인덱스를 조정해주는 로직이 필요
while lst:   
    # 초기 idx는 0이고 K값에 따라 (K-1)씩 더해줘야함. 근데 idx가 계속 커지니까 len(lst)로 해주면서 인덱스 범위에서 벗어나지 않게 구현
    idx = (idx + K - 1) % len(lst)

    # pop한 값을 임시로 저장
    temp = lst.pop(idx)

    # 임시로 저장한 값을 result 리스트에 삽입
    result.append(temp)

# 결과 출력    
print('<'+', '.join(map(str, result))+'>')





# print('<'+','.join(result)+'>')

# while len(lst) != 0:
#     if step <= len(lst):
#         temp = lst.pop(step-1)
#         result.append(temp)
#         iter += 1
#         step = iter*K
#         # print(temp)
#         print(step)

#     else:
#         step = step - len(lst)
#         temp = lst.pop(step-1)
#         result.append(temp)
#         iter += 1

# # print(result)
