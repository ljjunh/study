def dfs(i):
    visited[i] = 1 
    for w in graph[i]:
        if visited[w] == 0:
            dfs(w)

for tc in range(1, 11):
    T, E = map(int, input().split())
    arr = list(map(int, input().split()))
    graph = [[] for _ in range(100)] 
    visited = [0] * (100)
    for i in range(E):
        a, b = arr[i*2], arr[i*2+1]
        graph[a].append(b)
    dfs(0)
    print(f"#{T} {visited[99]}")
