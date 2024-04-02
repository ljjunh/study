import sys
input = sys.stdin.readline
from collections import deque


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    global ans
    cnt = 1
    visited[x][y] = cnt
    q = deque()
    q.append((x, y))
    while q:
        cx, cy = q.popleft()
        for k in range(4):
            nx, ny = cx + dx[k], cy + dy[k]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and graph[nx][ny]:
                cnt += 1
                visited[nx][ny] = cnt
                q.append((nx, ny))
    ans.append(visited[cx][cy])

N = int(input())
graph = [list(map(int, input().rstrip())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
ans = []
result = 0
for i in range(N):
    for j in range(N):
        if graph[i][j] and not visited[i][j]:
            bfs(i, j)
            result += 1
ans.sort()
print(result, *ans, sep="\n")