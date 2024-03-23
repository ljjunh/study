from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    q = deque()
    cnt = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                q.append((i, j))
                visited[i][j] = 1
            elif graph[i][j] == 0:
                cnt += 1
    while q:
        x, y = q.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and graph[nx][ny] == 0:
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
                cnt -= 1
    if cnt == 0:
        return visited[x][y] - 1
    else:
        return -1
                
M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
ans = bfs()
print(ans)
