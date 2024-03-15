import sys
input = sys.stdin.readline

def recur(n, lst):
    global ans
    if n == N:
        tmp = 0
        for k in range(N-1):
            tmp += abs(lst[k]-lst[k+1])
        ans = max(ans, tmp)
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            recur(n+1, lst + [arr[i]])
            visited[i] = 0

N = int(input())
arr = list(map(int, input().split()))
ans = 0
visited = [0] * N
recur(0, [])
print(ans)