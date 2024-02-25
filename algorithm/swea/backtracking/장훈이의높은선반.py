T = int(input())

def dfs(n, sm):
    global ans
    if sm - B >= ans:
        return
    if n == N:
        if sm >= B:
            ans = min(ans, sm - B)
        return
    dfs(n+1, sm + arr[n])
    dfs(n+1, sm)
for tc in range(1, T + 1):
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))
    ans = 10000 * N
    dfs(0, 0)
    print(f"#{tc} {ans}")