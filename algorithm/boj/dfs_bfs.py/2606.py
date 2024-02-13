def dfs(v):
    visited[v] == 1
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

n = int(input()) # 노드
m = int(input()) # 간선
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
for i in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

dfs(1)
print(visited)    