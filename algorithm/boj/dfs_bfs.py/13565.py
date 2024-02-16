import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    global graph, visited
    visited[x][y] = 1
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < M and 0 <= ny < N and not visited[nx][ny] and graph[nx][ny] == 0:
            dfs(nx, ny)
    

M, N = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(M)]
visited = [[0] * N for _ in range(M)]
for i in range(N):
    if not graph[0][i] and not visited[0][i]:
        dfs(0, i)
if 1 in visited[M-1]:
    print("YES")
else:
    print("NO") 