import sys
input = sys.stdin.readline
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    visited = [[0] * M for _ in range(N)]
    visited[x][y] = 1
    q = deque()
    q.append((x, y))
    while q:
        cx, cy = q.popleft()
        for k in range(4):
            nx, ny = cx+dx[k], cy+dy[k]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and graph[nx][ny]:
                visited[nx][ny] = visited[cx][cy] + 1
                q.append((nx, ny))
    return visited[N-1][M-1]


N, M = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(N)]
print(bfs(0, 0))
