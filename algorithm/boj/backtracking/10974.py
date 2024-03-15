import sys
input = sys.stdin.readline

def recur(n, lst):
    if n == N:
        print(*lst)
        return
    for i in range(1, N + 1):
        if visited[i]:
            continue
        visited[i] = 1
        recur(n + 1, lst + [i])
        visited[i] = 0
        

N = int(input())
visited = [0] * (N+1)
recur(0, [])