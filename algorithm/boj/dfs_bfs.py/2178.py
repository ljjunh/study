import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


N, M = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

q = deque()
q.append((0, 0))
visited[0][0] = True

while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] and not visited[nx][ny]:
            graph[nx][ny] = graph[x][y] + 1
            visited[nx][ny] = True
            q.append((nx, ny))
print(graph[N-1][M-1])