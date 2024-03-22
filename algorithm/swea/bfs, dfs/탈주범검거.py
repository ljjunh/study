from collections import deque
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상 하 좌 우
tunnel = [[], [0, 1, 2, 3], [0, 1], [2, 3], [0, 3], [1, 3], [1, 2], [0, 2]]

def bfs(x, y):
    visited[x][y] = 1
    q = deque()
    q.append((x, y))
    while q:
        tx, ty = q.popleft()
        tmp = tunnel[graph[tx][ty]]
  
        for k in tmp:
            dx, dy = delta[k]
            nx, ny = tx + dx, ty + dy
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and graph[nx][ny]:
                next = tunnel[graph[nx][ny]]
                for j in next:
                    mx, my = nx + delta[j][0], ny + delta[j][1]
                    if mx == tx and my == ty:
                        visited[nx][ny] = visited[tx][ty] + 1
                        q.append((nx, ny))   
                
                
T = int(input())
for tc in range(1, T + 1):
    N, M, r, c, L = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    ans = 0
    bfs(r,c)
    for i in range(N):
        for j in range(M):
            if visited[i][j] == 0:
                continue
            if visited[i][j] <= L:
                ans += 1
    print(f"#{tc} {ans}")
