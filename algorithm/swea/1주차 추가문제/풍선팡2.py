T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
        #상,하,좌,우
    max_num = 0
    for i in range(n):
        for j in range(m):
            temp = arr[i][j]
            for k in range(4):
                if i + dx[k] >= 0 and j + dy[k] >= 0 and i + dx[k] < n and j + dy[k] < m:
                    temp += arr[i + dx[k]][j + dy[k]]
            if max_num < temp:
                max_num = temp
    print(f"#{tc} {max_num}")
