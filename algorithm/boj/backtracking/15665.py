import sys
input = sys.stdin.readline

def recur(n, lst):
    if n == M:
        ans.append(lst)
        return
    prev = 0
    for i in range(N):
        if prev != arr[i]:
            prev = arr[i]
            recur(n+1, lst + [arr[i]])

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
ans = []
recur(0, [])
for i in ans:
    print(*i)