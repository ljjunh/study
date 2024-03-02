N = int(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
arr = [[0] * 102 for _ in range(102)]
ans = 0
for i in range(N):
    x, y = map(int, input().split())
    for j in range(x, x + 10):
        for k in range(y, y + 10):
            arr[j][k] = 1

for i in range(1, 101):
    for j in range(1, 101):
        if arr[i][j] == 1:
            cnt = 0
            for k in range(4):
                nx, ny = i + dx[k], j + dy[k]
                if arr[nx][ny] == 1:
                    cnt += 1
            if cnt == 2:
                ans += 2
            elif cnt == 3:
                ans += 1
print(ans)