import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    graph[x][y] = 0

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if graph[nx][ny]:
            dfs(nx, ny)


T = int(input())
while T > 0:
    T -= 1
    M, N, K = map(int, input().split())
    # M 가로 T 세로 K 배추개수
    MAX = 50 + 10
    graph = [[0] * MAX for _ in range(MAX)]
    answer = 0
    for i in range(K):
        x, y = map(int, input().split())
        graph[y+1][x+1] = True
    for i in range(N+1):
        for j in range(M+1):
            if graph[i][j]:
                dfs(i, j)
                answer += 1
    print(answer)