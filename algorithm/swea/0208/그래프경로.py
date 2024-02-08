def dfs(v):
    visited[v] = 1
    for i in range(1, V + 1):
        if not visited[i] and graph[v][i] == 1:
            dfs(i)

T = int(input())
for tc in range(1, T + 1):
    V, E = map(int,input().split())
    graph = [[0] * (V + 1) for _ in range(V + 1)]
    visited = [0] * (V + 1)
    for i in range(E):
        a, b = map(int, input().split())
        graph[a][b] = 1
    n, m = map(int, input().split())
    dfs(n)
    print(f"#{tc} {visited[m]}")
   