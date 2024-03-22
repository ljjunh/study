from collections import deque
import sys
input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    border_visited = [[0] * M for _ in range(N)]
    border_visited[x][y] = 1
    q = deque()
    q.append((x, y))
    while q:
        tx, ty = q.popleft()
        for k in range(4):
            nx, ny = tx + dx[k], ty + dy[k]
            if 0 <= nx < N and 0 <= ny < M and not border_visited[nx][ny]:
                if graph[nx][ny] == 1:
                    border.append((nx, ny))
                    border_visited[nx][ny] = 1
                else:
                    border_visited[nx][ny] = 1
                    q.append((nx, ny))


N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

ans = 0
while True:
    border = []
    cheese = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                cheese += 1
    bfs(0, 0)
    ans += 1
    for i,j in border:
        graph[i][j] = 0
    r_cheese = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                r_cheese += 1
    if r_cheese == 0:
        print(ans, cheese, sep="\n")
        break
    
