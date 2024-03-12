import sys
input = sys.stdin.readline

def dfs(n, lst):
    if n == M:
        print(*lst)
        return
    prev = 0
    for i in range(N):
        if not visited[i] and prev != arr[i]:
            prev = arr[i]        
            visited[i] = 1
            dfs(n+1, lst+[arr[i]])
            visited[i] = 0
N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
visited = [0] * N
dfs(0, [])