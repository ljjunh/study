from collections import deque
import sys
import copy
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    global ans
    q = deque()
    tmp_graph = copy.deepcopy(graph)
    for i in range(N):
        for j in range(M):
            if tmp_graph[i][j] == 2:
                q.append((i, j))
    while q:
        cx, cy = q.popleft()
        for k in range(4):
            nx, ny = cx + dx[k], cy + dy[k]
            if 0 <= nx < N and 0 <= ny < M and tmp_graph[nx][ny] == 0:
                q.append((nx, ny))
                tmp_graph[nx][ny] = 2
    cnt = 0
    for i in range(N):
        cnt += tmp_graph[i].count(0)
    ans = max(ans, cnt)

def recur(n):
    if n == 3:
        bfs()
        return
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                graph[i][j] = 1
                recur(n + 1)
                graph[i][j] = 0

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
ans = 0
recur(0)
print(ans)