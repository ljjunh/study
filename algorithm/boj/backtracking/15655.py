import sys
input = sys.stdin.readline
def dfs(n, s, lst):
    if n == M:
        print(*lst)
        return
    for i in range(s, N):
        if visited[i]:
            continue
        visited[i] = 1
        dfs(n+1, i+1, lst+[arr[i]])
        visited[i] = 0

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
visited = [0] * (N+1)
dfs(0, 0, [])
