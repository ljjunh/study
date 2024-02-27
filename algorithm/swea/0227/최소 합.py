T = int(input())
dx = [0, 1]
dy = [1, 0]

def dfs(x, y, sm):
    global N, ans
    if x == N - 1 and y == N - 1:
        ans = min(ans, sm)
        return
    if sm > ans:
        return
    visited[x][y] = True
    for i in range(2):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            if not visited[nx][ny]:
                dfs(nx, ny, sm + arr[nx][ny])
                visited[nx][ny] = False

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    ans = 130
    dfs(0, 0, arr[0][0])
    print(f"#{tc} {ans}")