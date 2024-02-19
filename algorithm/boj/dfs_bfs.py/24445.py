import sys
input = sys.stdin.readline

def bfs(idx):
    global graph, visited, order
    visited[idx] = order
    order += 1
    q = [idx]
    while q:
        v = q.pop(0)
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = order
                order += 1

N, M, R = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)
order = 1

for i in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(1, N + 1):
    graph[i] = sorted(graph[i], reverse=True)

bfs(R)
print(*visited[1:], sep = "\n")

