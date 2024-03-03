import sys
input = sys.stdin.readline
H, W = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(H)]
ans = [[-1] * W for _ in range(H)]
cnt = 1
for i in range(H):
    state = False
    for j in range(W):
        if arr[i][j] == "c":
            ans[i][j] = 0
            state = True
            cnt = 1
        elif arr[i][j] != "c" and state == True:
            ans[i][j] = cnt
            cnt += 1
for i in ans:
    print(*i)

