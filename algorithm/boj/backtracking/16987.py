import sys
input = sys.stdin.readline

def recur(n, cnt):
    global ans
    if n == N:
        ans = max(ans, cnt)
        return
    if arr[n][0] < 1: # 현재 계란이 깨지면 다음 계란으로 
        recur(n+1, cnt)
    else: # 현재 계란이 안깨진 상태
        state = False # 한번도 안부딪혔으면 False
        for i in range(N):
            if arr[i][0]< 1 or i == n:
                continue
            state = True #한번이라도 부딪히면 True
            arr[n][0] -= arr[i][1]
            arr[i][0] -= arr[n][1]
            recur(n+1, cnt+int(arr[n][0]<1)+int(arr[i][0]<1))
                        #들고있던 계란이 깨질때+1, 때린 계란이 깨질때+1
            arr[n][0] += arr[i][1] 
            arr[i][0] += arr[n][1]
        if state == False:
            recur(n+1, cnt) # 한번도 안부딪혔으면 다음 계란으로

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0
recur(0, 0)
print(ans)