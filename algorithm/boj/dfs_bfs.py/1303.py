import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    global tmp_white, tmp_blue
    visited[x][y] = True
    if graph[x][y] == 1:
        tmp_white += 1
    elif graph[x][y] == 2:
        tmp_blue += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx <= M and 0 <= ny <= N:
            if not visited[nx][ny] and graph[x][y] == graph[nx][ny]:
                dfs(nx, ny)
        

N, M = map(int, input().split()) # N 가로 M 세로
graph = [[0] * (N+1) for _ in range(M+1)]
visited = [[False] * (N+1) for _ in range(M+1)]
white = 0
blue = 0
# W는 1 B는 2로 입력받음
for i in range(1, M + 1):
    s = input().rstrip()
    for j in range(1, N + 1):
        graph[i][j] = (1 if s[j - 1] == "W" else 2)

for i in range(1, M + 1):
    for j in range(1, N + 1):
        if not visited[i][j]:
            tmp_white = 0
            tmp_blue = 0
            dfs(i, j)
            white += tmp_white ** 2
            blue += tmp_blue ** 2
print(white, blue)

