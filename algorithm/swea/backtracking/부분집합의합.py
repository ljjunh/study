T = int(input())

def dfs(n, sm, cnt):
    global ans
    if n == 12:
        if sm == K and cnt == N:
            ans += 1
        return
    # n을 사용하는 경우
    dfs(n+1, sm+arr[n], cnt+1)
    # n을 사용하지 않는 경우
    dfs(n+1, sm, cnt)

for tc in range(1, T + 1):
    arr = [i for i in range(1, 13)]
    N, K = map(int, input().split())
    ans = 0
    dfs(0, 0, 0)
    print(f"#{tc} {ans}")