def recur(n, kcal, score):
    global ans
    if kcal > L:
        return
    if n == N:
        ans = max(ans, score)
        return
    recur(n+1, kcal+arr[n][1], score + arr[n][0])
    recur(n+1, kcal, score)

T = int(input())
for tc in range(1, T + 1):
    N, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    recur(0, 0, 0)
    print(f"#{tc} {ans}")