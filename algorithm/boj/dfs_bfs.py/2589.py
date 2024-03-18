import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
ans = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(N):
    for j in range(M):
        if graph[i][j] == "L":
            visited = [[0] * M for _ in range(N)]
            dist = [[0] * M for _ in range(N)]
            q = deque()
            q.append((i,j))
            visited[i][j] = 1
            while q:
                x, y = q.popleft()
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and graph[nx][ny] == "L":
                        visited[nx][ny] = 1
                        dist[nx][ny] = dist[x][y] + 1
                        ans = max(ans, dist[nx][ny])
                        q.append((nx, ny))
                
print(ans)