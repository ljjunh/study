import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y):
    v[x][y] = 1
    q = deque()
    q.append((x, y))
    while q:
        tx, ty = q.popleft()
        for t in range(4):
            nx, ny = tx + dx[t], ty + dy[t]
            if 0 <= nx < N and 0 <= ny < M and not v[nx][ny] and graph[nx][ny] != 0:
                v[nx][ny] = 1
                q.append((nx, ny))

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cnt = 0 
while True:
    visited = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if graph[i][j] != 0:
                visited[i][j] = 1
                for k in range(4):
                    nx, ny = i + dx[k], j + dy[k]
                    if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0 and not visited[nx][ny]:
                        if graph[i][j] == 0:
                            continue
                        graph[i][j] -= 1
    cnt += 1

    v = [[0] * M for _ in range(N)]
    bfs_cnt = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] != 0 and not v[i][j]:
                bfs(i, j)
                bfs_cnt += 1
 
    if bfs_cnt >= 2:
        print(cnt)
        break
    max_num = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                continue
            if graph[i][j] > max_num:
                max_num = graph[i][j]
    if max_num == 0:
        print(0)
        break
                