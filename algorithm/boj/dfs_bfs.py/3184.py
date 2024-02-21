import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    global sheep, wolf
    if graph[x][y] == "o":
        sheep += 1
    elif graph[x][y] == "v":
        wolf += 1
    graph[x][y] = "#"
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if graph[nx][ny] != "#" and graph[nx][ny] != "":
            dfs(nx, ny)


N, M = map(int, input().split())
MAX = 250 + 10
graph = [[""] * MAX for _ in range(MAX)]
ans_sheep = 0
ans_wolf = 0
for i in range(1, N + 1):
    s = input().rstrip()
    for j in range(1, M + 1):
        graph[i][j] = s[j-1]


for i in range(1, N + 1):
    for j in range(1, M + 1):
        sheep = 0
        wolf = 0
        if graph[i][j] == "v" or graph[i][j] == "o":
            dfs(i,j)
            if wolf >= sheep:
                ans_wolf += wolf
            elif wolf < sheep:
                ans_sheep += sheep
print(ans_sheep, ans_wolf)
