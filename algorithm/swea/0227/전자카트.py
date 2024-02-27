T = int(input())

def dfs(n):
    global ans
    if n == N:
        temp = [1] + path + [1]
        sm = 0
        for k in range(N):
            sm += arr[temp[k]-1][temp[k+1]-1]
        ans = min(ans, sm)
        return
    for i in range(2, N+1):
        if not visited[i]:
            visited[i] = True
            path.append(i)
            dfs(n + 1)
            path.pop()
            visited[i] = False
            
            


for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 2147000000
    path = []
    visited = [False] * (N + 1)
    dfs(1)
    print(f"#{tc} {ans}")
