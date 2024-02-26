T = int(input())

def dfs(n, sm):
    global ans
    if sm >= ans:
        return
    if n > 12:
        ans = min(ans, sm)
        return
    dfs(n + 1, sm + arr[n] * day)
    dfs(n + 1, sm + mon)
    dfs(n + 3, sm + qt)
    dfs(n + 12, sm + year)

for tc in range(1, T + 1):
    day, mon, qt, year = map(int, input().split())
    arr = [0] + list(map(int, input().split()))
    ans = 36000
    dfs(1, 0) # 월, 합계
    print(f"#{tc} {ans}")