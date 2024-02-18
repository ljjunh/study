import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

dx = [0, 1]
dy = [1, 0]

def dfs(x, y):
    visited[x][y] = True
    for i in range(2):
        nx = x + dx[i] * graph[x][y]
        ny = y + dy[i] * graph[x][y]
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
            dfs(nx,ny)

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

dfs(0, 0)
if visited[N-1][N-1]:
    print("HaruHaru")
else:
    print("Hing")