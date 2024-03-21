from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    visited[x][y] = 1
    ans = []
    q = deque()
    q.append((x, y))
    ans.append(graph[x][y])
    while q:
        tx, ty = q.popleft()
        for k in range(4):
            nx, ny = tx + dx[k], ty + dy[k]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if abs(graph[nx][ny] - graph[tx][ty]) == 1:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                    ans.append((graph[nx][ny]))
    return min(ans), len(ans)

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    num = N * N
    cnt = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                tnum, tcnt = bfs(i, j)
                if cnt < tcnt or (cnt == tcnt and num>tnum):
                    num, cnt = tnum, tcnt
    print(f"#{tc} {num} {cnt}")