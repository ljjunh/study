def dfs(n, s, lst):
    if n == M:
        ans.append(lst)
        return
    for i in range(s, N+1):
        dfs(n+1, i, lst + [i])
N, M = map(int, input().split())
ans = []
dfs(0, 1, [])
for i in ans:
    print(*i)