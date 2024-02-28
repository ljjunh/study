import sys
input = sys.stdin.readline

def chk(lst):
    max_cnt = 1
    for i in range(N):
        cnt1 = 1
        cnt2 = 1
        for j in range(N - 1):
            if lst[i][j] == lst[i][j+1]:
                cnt1 += 1
                max_cnt = max(max_cnt, cnt1)
            elif lst[i][j] != lst[i][j+1]:
                cnt1 = 1
            if lst[j][i] == lst[j+1][i]:
                cnt2 += 1
                max_cnt = max(max_cnt, cnt2)
            elif lst[j][i] != lst[j+1][i]:
                cnt2 = 1
    return max_cnt
        

N = int(input())
arr = [list(input().rstrip()) for _ in range(N)]
ans = 1
for i in range(N):
    for j in range(N):
        if j + 1 < N and arr[i][j] != arr[i][j+1]:
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
            temp = chk(arr)
            ans = max(temp, ans)
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
        if i + 1 < N and arr[i][j] != arr[i+1][j]:
            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]
            temp = chk(arr)
            ans = max(temp, ans)
            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]
print(ans)