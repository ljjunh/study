dx = [1, 0, -1, 1]
dy = [0, 1, 1, 1]
def func(x, y):
    for i in range(4):
        cnt = 1
        for j in range(1, 5):
            nx, ny = x + dx[i] * j, y + dy[i] * j
            if 0 <= nx < N and 0 <= ny < N:
                if arr[nx][ny] == "o":
                    cnt += 1
                if cnt == 5:
                    return True
    return False
    

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    ans = "NO"
    for i in range(N):
        for j in range(N):
            if arr[i][j] == "o":
                if func(i, j):
                    ans = "YES"
                    break
    print(f"#{tc} {ans}")
    