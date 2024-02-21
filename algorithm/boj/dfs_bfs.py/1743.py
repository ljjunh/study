import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    global cnt
    graph[x][y] = False
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if graph[nx][ny]:
            dfs(nx, ny)
            cnt += 1



N, M, K = map(int, input().split())
MAX = 100 + 10
graph = [[False] * MAX for _ in range(MAX)]
max_num = 0
for i in range(K):
    x, y = map(int, input().split())
    graph[x][y] = True

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if graph[i][j]:
            cnt = 1
            dfs(i, j)
            if max_num < cnt:
                max_num = cnt
print(max_num)