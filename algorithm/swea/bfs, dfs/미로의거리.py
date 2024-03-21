T = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    visited[x][y] = 1
    q = [(x, y)]
    while q:
        cx, cy = q.pop(0)
        if graph[cx][cy] == 3:
            return visited[cx][cy] - 2
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny] and graph[nx][ny] != 1:
                    q.append((nx, ny))
                    visited[nx][ny] = visited[cx][cy] + 1
    return 0
for tc in range(1, T + 1):
    N = int(input())
    graph = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
  
    # 출발 위치 
    a = b = 0
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 2:
                a, b = i, j
            
    ans = bfs(a, b)
    print(f"#{tc} {ans}")