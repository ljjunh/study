def recur(n, cnt):
    global ans
    if n >= N-1:
        ans = min(ans, cnt)
        return
    if cnt >= ans:
        return
    
    for i in range(arr[n]):
        recur(n + 1 + i, cnt+1)

T = int(input())
for tc in range(1, T + 1):
    arr = list(map(int, input().split()))
    N = arr[0]
    arr = arr[1:]
    ans = 2147000000
    recur(0, -1)
    print(f"#{tc} {ans}")