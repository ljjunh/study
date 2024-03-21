dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    visited[x][y] = 1
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < 16 and 0 <= ny < 16 and graph[nx][ny] != 1 and not visited[nx][ny]:
            dfs(nx, ny)

for tc in range(10):
    N = int(input())
    graph = [list(map(int, input())) for _ in range(16)]
    visited = [[0] * 16 for _ in range(16)]
    x = y = 0
    end_x = end_y = 0
    for i in range(16):
        for j in range(16):
            if graph[i][j] == 2:
                x, y = i, j
            elif graph[i][j] == 3:
                end_x, end_y = i, j
    dfs(x, y)
    print(f"#{N} {visited[end_x][end_y]}")