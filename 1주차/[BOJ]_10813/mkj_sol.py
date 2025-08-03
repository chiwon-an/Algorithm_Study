def facto(n):
    if n <= 1:
        return 1
    else:
        return n * facto(n-1) # 재귀함수
    

# print(facto(int(input)))

print(facto(5))
# facto(5) -> 5*facto(4) -> 5*4*facto(3) -> 5*4*3*facto(2) -> 5*4*3*2*facto(1) -> 5*4*3*2*1 = 120