import sys
input = sys.stdin.readline

def recur(n, s, lst):
    if n == 6:
        print(*lst)
        return
    for i in range(s, N):
        if not visited[i]:
            visited[i] = 1
            recur(n+1, i+1, lst + [arr[i]])
            visited[i] = 0

while True:
    arr = list(map(int, input().split()))
    if arr[0] == 0:
        exit()
    N = arr[0]
    arr = arr[1:]
    arr.sort()
    visited = [0] * N
    recur(0, 0, [])
    print()
