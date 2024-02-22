T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    res = 0
    dx = [-1, 1, 0, 0, -1, 1, -1, 1]
    dy = [0, 0, -1, 1, -1, 1, 1, -1]
    
    for i in range(N):
        for j in range(M):
            cnt = 0
            for k in range(8):
                nx, ny = i + dx[k], j + dy[k]
                if 0 <= nx < N and 0 <= ny < M:
                    if arr[i][j] > arr[nx][ny]:
                        cnt += 1
            if cnt >= 4:
                res += 1
    print(f"#{tc} {res}")
                    