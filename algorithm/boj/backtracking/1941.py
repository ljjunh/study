import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque()
    visited = [[0] * 5 for _ in range(5)]
    visited[x][y] = 1
    cnt = 1
    q.append((x, y))
    while q:
        cx, cy = q.popleft()
        for k in range(4):
            nx, ny = cx + dx[k], cy + dy[k]
            if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny] and v[nx][ny] == 1:
                q.append((nx, ny))
                visited[nx][ny] = 1
                cnt += 1
    if cnt == 7:
        return True


def chk():
    for i in range(5):
        for j in range(5):
            if v[i][j] == 1:
                return bfs(i, j)


def recur(n, cnt, ds):
    global ans
    if cnt > 7:
        return
    if n == 25:
        if cnt == 7 and ds >= 4:
            if chk():
                ans += 1
        return
    
    v[n//5][n%5] = 1
    recur(n+1, cnt+1, ds + int(graph[n//5][n%5] == "S"))
    v[n//5][n%5] = 0
    recur(n+1, cnt, ds)

graph = [list(input().rstrip()) for _ in range(5)]
ans = 0
v = [[0] * 5 for _ in range(5)]
recur(0, 0, 0)
print(ans)