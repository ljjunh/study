def dfs(n, sm):
    global ans, path
    if n == 3:
        if sm <= M:
            ans = max(ans, sm)
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            dfs(n+1, sm + arr[i])
            visited[i] = False

N, M = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0
visited = [False] * N
dfs(0, 0)
print(ans)