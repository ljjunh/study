import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    global cnt
    visited[x][y] = 1
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and graph[nx][ny]:
            dfs(nx, ny)
            cnt += 1
    return cnt

N = int(input())
graph = [list(map(int, input().rstrip())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
ans = []
result = 0
cnt = 0
for i in range(N):
    for j in range(N):
        if graph[i][j] and not visited[i][j]:
            cnt = 1
            ans.append(dfs(i,j))
            result += 1
print(result, *sorted(ans), sep="\n")