import sys
input = sys.stdin.readline

dx = [-1, 1, 0 ,0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    global visited, alpha
    visited[x][y] = 1
    if graph[x][y] not in alpha:
        alpha.append(graph[x][y])
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and graph[nx][ny] not in alpha:
            dfs(nx, ny)




N, M = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
alpha = []
dfs(0,0)
print(visited)