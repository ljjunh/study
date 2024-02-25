T = int(input())

def dfs(n, sm):
    global ans
    if ans <= sm:
        return
    if n == N:
        ans = min(ans, sm)
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            dfs(n+1, sm + arr[n][i])
            visited[i] = 0
        

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 15 * 99
    visited = [0] * N
    dfs(0, 0)
    print(f"#{tc} {ans}")