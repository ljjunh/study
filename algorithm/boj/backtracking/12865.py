import sys
input = sys.stdin.readline
def recur(n, w, v):
    global ans
    if w > K:
        return
    if n == N:
        ans = max(ans, v)
        return
    
    recur(n+1, w+arr[n][0], v+arr[n][1])
    recur(n+1, w, v)

N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0
recur(0, 0, 0)
print(ans)