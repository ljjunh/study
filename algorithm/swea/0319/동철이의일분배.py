def recur(n, p):
    global ans
    if n == N:
        ans = max(ans, p * 100)
    if p * 100 <= ans:
        return
    for i in range(N):
        if visited[i]:
            continue
        visited[i] = 1
        recur(n+1, p * arr[n][i])
        visited[i] = 0

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            arr[i][j] = arr[i][j] / 100
    ans = 0
    visited = [0] * N
    recur(0, 1)
    print(f"#{tc} {ans:.6f}")