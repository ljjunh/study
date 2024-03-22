from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    visited[x][y] = 1
    q = deque()
    q.append((x, y))
    while q:
        tx, ty = q.popleft()
        for k in range(4):
            nx, ny = tx + dx[k], ty + dy[k]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and graph[nx][ny] == 1:
                visited[nx][ny] = visited[tx][ty] + 1
                q.append((nx, ny))
# for문 돌면서 1 하나씩 없애고 bfs돌고 다시 1 만들고 ans저장해놨따가 최소값 출력
# for i in range(N):
#     for j in range(M):
#         if graph[i][j] == 1:
#             graph[i][j] = 0
#             bfs(sx, sy)
#             graph[i][j] = 1
N, M = map(int, input().split())
sx, sy = map(int, input().split())
ex, ey = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
ans = 2147000000
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            visited = [[0] * M for _ in range(N)]
            graph[i][j] = 0
            bfs(sx-1, sy-1)
            ans = min(ans, visited[ex-1][ey-1])
            graph[i][j] = 1
print(ans)