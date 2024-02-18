import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

MAX = 50 + 10
dx = [-1, 1, 0, 0, -1, 1, -1, 1]
dy = [0, 0, -1, 1, -1, -1, 1, 1]

def dfs(x, y):
    graph[x][y] = 0
    for i in range(8):
        nx, ny = x + dx[i], y + dy[i]
        if graph[nx][ny]:
            dfs(nx, ny)
while True:
    w, h = map(int, input().split())
    answer = 0
    if w == 0 or h == 0:
        break
    graph = [[False] * MAX for _ in range(MAX)]
    for i in range(1, h+1):
        s = list(map(int, input().split()))
        for j in range(1, w+1):
            graph[i][j] = s[j-1]
    for i in range(1, h+1):
        for j in range(1, w+1):
            if graph[i][j]:
                dfs(i, j)
                answer += 1
    print(answer)