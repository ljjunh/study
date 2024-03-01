def dfs(n, lst):
    if n == M:
        ans.append(lst)
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            dfs(n+1, lst + [arr[i]])
            visited[i] = 0

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
ans = []
visited = [0] * N
dfs(0, [])
for i in ans:
    print(*i)