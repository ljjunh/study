import sys
input = sys.stdin.readline

def recur(n, a, b, use):
    global ans
    if n == N:
        if use == 0:
            return
        ans = min(ans, abs(a - b))
        return
    recur(n+1, a * arr[n][0], b + arr[n][1], use+1)
    recur(n+1, a, b, use)

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 2147000000
recur(0, 1, 0, 0) # 신맛은 곱이니까 1로 시작 쓴맛은 덧셈이니까 0시작
print(ans)