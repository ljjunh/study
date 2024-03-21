from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    distance = [[2147000000 for _ in range(N)] for _ in range(N)]
    distance[0][0] = 0
    q = deque()
    q.append((0, 0))
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                temp = 1
                if graph[nx][ny] > graph[x][y]:
                    temp += graph[nx][ny] - graph[x][y]
                if distance[nx][ny] > distance[x][y] + temp:
                    distance[nx][ny] = distance[x][y] + temp
                    q.append((nx, ny))
    print(f"#{tc} {distance[N-1][N-1]}")