import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

dx = [-1, 1, 0, 0, -1, 1, -1, 1]
dy = [0, 0, -1, 1, -1, 1, 1, -1]

def dfs(x, y):
    graph[x][y] = 0
    for i in range(8):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and graph[nx][ny]:
            dfs(nx, ny)

N, M = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]
answer = 0
for i in range(N):
    for j in range(M):
        if graph[i][j]:
            dfs(i, j)
            answer += 1
print(answer)