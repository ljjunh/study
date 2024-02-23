import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    global wolf, sheep
    if graph[x][y] == "v":
        wolf += 1
    elif graph[x][y] == "k":
        sheep += 1
    graph[x][y] = "#"
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if graph[nx][ny] != "#":
                dfs(nx, ny)

N, M = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(N)]
res_sheep = 0
res_wolf = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == "v" or graph[i][j] == "k":
            sheep = 0
            wolf = 0
            dfs(i, j)
            if sheep > wolf:
                res_sheep += sheep
            else:
                res_wolf += wolf
print(res_sheep, res_wolf)
