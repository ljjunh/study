import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

dx = [-1, 1, 0, 0, -1, 1, -1, 1]
dy = [0, 0, -1, 1, -1, -1, 1, 1]

def dfs(x, y):
    global graph, visited, state
    visited[x][y] = True
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if graph[x][y] < graph[nx][ny]:
                state = False
            if not visited[nx][ny] and graph[nx][ny] == graph[x][y]:
                dfs(nx, ny)


N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
answer = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] != 0 and not visited[i][j]:
            state = True
            dfs(i, j)
            if state:
                answer += 1
print(answer)