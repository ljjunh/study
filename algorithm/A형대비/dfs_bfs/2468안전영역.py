import sys
input = sys.stdin.readline
from collections import deque

def bfs(x, y, h):
    global visited
    visited[x][y] = 1
    q = deque()
    q.append((x, y))
    while q:
        cx, cy = q.popleft()
        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nx, ny = cx+dx, cy+dy
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and graph[nx][ny] > h:
                q.append((nx, ny))
                visited[nx][ny] = 1
N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
max_num = 0
ans = 1
for i in range(N):
    max_num = max(max_num, max(graph[i]))

for x in range(1, max_num+1):
    cnt = 0
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and graph[i][j] > x:
                bfs(i, j, x) 
                cnt += 1 
    ans = max(ans, cnt)
print(ans)

