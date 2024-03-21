from collections import deque
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
            if 0 <= nx < 16 and 0 <= ny < 16 and not visited[nx][ny] and graph[nx][ny] != 1:
                q.append((nx, ny))
                visited[nx][ny] = 1

for tc in range(1, 11):
    N = int(input())
    graph = [list(map(int, input())) for _ in range(16)]
    visited = [[0] * 16 for _ in range(16)]
    x = y = 0
    endx = endy = 0
    for i in range(16):
        for j in range(16):
            if graph[i][j] == 1 or graph[i][j] == 0:
                continue
            elif graph[i][j] == 2:
                x, y = i, j
            elif graph[i][j] == 3:
                endx, endy = i, j
    bfs(x, y)
    print(f"#{tc} {visited[endx][endy]}")
