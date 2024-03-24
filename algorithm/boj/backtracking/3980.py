import sys
input = sys.stdin.readline
def recur(n, sm):
    global ans
    if n == 11:
        ans = max(ans, sm)
        return
    for i in range(11):
        if not visited[i] and arr[n][i] != 0: #행은 n으로, 열은 visited로 중복 걸러짐
            visited[i] = 1
            recur(n+1, sm+arr[n][i])
            visited[i] = 0

C = int(input())
for _ in range(C):
    arr = [list(map(int, input().split())) for _ in range(11)]
    ans = 0
    visited = [0] * 11
    recur(0, 0)
    print(ans)