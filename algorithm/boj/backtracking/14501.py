import sys
input = sys.stdin.readline

def recur(idx, price):
    global ans
    if idx > N:
        if idx > N+1:
            return
        ans = max(ans, price)
        return

    recur(idx + arr[idx][0], price + arr[idx][1])
    recur(idx + 1, price)

N = int(input())
arr = [[] for _ in range(N+1)]
for i in range(1, N + 1):
    a, b = map(int, input().split())
    arr[i] = [a, b]
ans = 0
recur(1, 0)
print(ans)