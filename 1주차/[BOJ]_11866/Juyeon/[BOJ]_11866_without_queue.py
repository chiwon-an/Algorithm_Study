# 큐 없이 진행한 코드
# 결과는 나오지만 백준에 제출했을 때 런타임 에러 발생

def Joshephus(N, K):
    quo = N // K
    remainder = N % K
    if len(lst) == 0:
        print(f"<{', '.join(map(str, ans))}>")
    else:
        for i in range(quo):
            ans.append(lst.pop(K * (i+1) -(1+i)))
        while 0 in lst:
            lst.remove(0)
        for i in range(remainder):
            lst.insert(0, 0)
        Joshephus(len(lst), K)
    
N, K = map(int,input().split())
lst = list(range(1, N+1))

ans = []
Joshephus(N, K)