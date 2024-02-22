T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    # N 행,열 M 스프레이 세기
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    max_num = 0
    for i in range(N):
        for j in range(N):
            cnt = 0
            cnt += arr[i][j]
            for k in range(4):
                for z in range(1, M):    
                    nx = i + dx[k] * z
                    ny = j + dy[k] * z
                    if 0 <= nx < N and 0 <= ny < N:
                        cnt += arr[nx][ny]
            if max_num < cnt:
                max_num = cnt

    tx = [-1, 1, -1, 1]
    ty = [-1, -1, 1, 1]
    for i in range(N):
        for j in range(N):
            cnt = 0
            cnt += arr[i][j]
            for k in range(4):
                for z in range(1, M):    
                    nx = i + tx[k] * z
                    ny = j + ty[k] * z
                    if 0 <= nx < N and 0 <= ny < N:
                        cnt += arr[nx][ny]
            if max_num < cnt:
                max_num = cnt


    print(f"#{tc} {max_num}")