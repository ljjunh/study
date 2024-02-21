import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [list(map(int, input().rstrip().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
a = b = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            a, b = i, j
q = deque()
q.append((a, b))
visited[a][b] = True
graph[a][b] = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[nx][ny] == 1:
            graph[nx][ny] = graph[x][y] + 1
            visited[nx][ny] = True
            q.append((nx, ny))

for i in range(n):
    for j in range(m):
        if visited[i][j] == False:
            if graph[i][j] != 0:
                graph[i][j] = -1

for i in range(n):
    for j in range(m):
        print(graph[i][j], end = " ")
    print()
