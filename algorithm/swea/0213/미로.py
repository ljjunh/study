def dfs(r, c, n):
    visited = [[0] * n for _ in range(n)]
    stack = []
    visited[r][c] = 1
    while True:
        if arr[r][c] == 3:
            return 1
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc] and arr[nr][nc] != 1:
                stack.append((r, c))
                visited[nr][nc] = 1
                r, c = nr, nc
                break
        else:
            if stack:
                r, c = stack.pop()
            else:
                break
    return 0

    
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    arr = [list(map(int,input())) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 2:
                print(f'#{tc} {dfs(i, j, n)}')
