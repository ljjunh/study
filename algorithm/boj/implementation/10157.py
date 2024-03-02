x, y = map(int, input().split())
target = int(input())
arr = [[0] * x for _ in range(y)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
dir = 0
s = e = 0
for i in range(1, x * y + 1):
    arr[s][e] = i
    s += dx[dir]
    e += dy[dir]
    if 0 > s or y <= s or 0 > e or x <= e or arr[s][e] != 0:
        s -= dx[dir]
        e -= dy[dir]
        dir = (dir + 1) % 4
        s += dx[dir]
        e += dy[dir]
ans = 0
for i in range(y):
    for j in range(x):
        if arr[i][j] == target:
            print(j+1, i+1)
            exit()
print(ans)


    