dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def recur(x, y, n, lst):
    if n ==7:
        ans.add(lst)
        return
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < 4 and 0 <= ny < 4:
            recur(nx, ny, n+1, lst+str(arr[nx][ny]))

T = int(input())
for tc in range(1, T + 1):
    arr = [list(map(int, input().split())) for _ in range(4)]
    ans = set()
    for i in range(4):
        for j in range(4):
            recur(i, j, 0, "")
    print(f"#{tc} {len(ans)}")