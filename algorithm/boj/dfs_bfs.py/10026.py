import sys
import copy
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    temp = graph[x][y]
    graph[x][y] = 0
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == temp:
            dfs(nx, ny)

def dfs2(x, y):
    graph[x][y] = 0
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and (graph[nx][ny] == "R" or graph[nx][ny] == "G"):
            dfs2(nx, ny)

N = int(input())
graph = [list(input().rstrip()) for _ in range(N)]
r = 0
g = 0
b = 0
peo2 = 0
tmp = copy.deepcopy(graph)
for i in range(N):
    for j in range(N):
        if graph[i][j] == "R":
            dfs(i, j)
            r += 1
        elif graph[i][j] == "G":
            dfs(i, j)
            g += 1
        elif graph[i][j] == "B":
            dfs(i, j)
            b += 1

graph = tmp
for i in range(N):
    for j in range(N):
        if graph[i][j] == "R" or graph[i][j] == "G":
            dfs2(i, j)
            peo2 += 1

print(r+g+b, b + peo2)