import sys
input = sys.stdin.readline

def recur(n, s, use):
    global ans
    if s == S:
        if use != 0:
            ans += 1
    
    if n == N:
        return
    
    recur(n+1, s+arr[n], use + 1)
    recur(n+1, s, use)


N, S = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0
recur(0, 0, 0)
print(ans)