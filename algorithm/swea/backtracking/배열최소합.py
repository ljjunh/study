T = int(input())
def dfs(n, sm):
    global ans
    if sm >= ans:
        return
    if n == N:
        ans = min(ans, sm)
        return
    for j in range(N):
        if v[j] == 0:
            v[j] = 1
            dfs(n+1, sm + graph[n][j])
            v[j] = 0

for tc in range(1, T + 1):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    v = [0] * N
    ans = 100
    visited = [0] * N
    dfs(0, 0)
    print(f"#{tc} {ans}")
