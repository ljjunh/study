import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    global visited, graph, cnt
    visited[x][y] = True
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0<= ny < M and not visited[nx][ny] and graph[nx][ny] == 0:
            dfs(nx, ny)
            cnt += 1

M, N, K = map(int, input().split())
graph = [[0] * M for _ in range(N)]
visited = [[False] * M for _ in range(N)]
answer = 0
res = []
for i in range(K):
    a, b, c, d = map(int, input().split())
    for i in range(a, c):
        for j in range(b, d):
            graph[i][j] = 1
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0 and not visited[i][j]:
            cnt = 1
            dfs(i, j)
            answer += 1
            res.append(cnt)
print(answer)
print(*sorted(res))