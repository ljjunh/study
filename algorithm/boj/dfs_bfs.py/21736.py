import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    global cnt
    if graph[x][y] == "P":
        cnt += 1
    graph[x][y] = "X"
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] != "X":
            dfs(nx, ny)

N, M = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(N)]
a = b = 0
cnt = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == "I":
            a, b = i, j      

dfs(a, b)
if cnt == 0:
    print("TT")
else:
    print(cnt)