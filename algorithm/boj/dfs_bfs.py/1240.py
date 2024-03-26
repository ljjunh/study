import sys
from collections import deque
input = sys.stdin.readline

def bfs(s, e):
    visited = [0] * (N+1)
    visited[s] = 1
    q = deque()
    q.append(s)
    while q:
        v = q.popleft()
        if v == e:
            return visited[e]-1
        for i in graph[v]:
            if not visited[i]:
                visited[i] = visited[v] + distance[v][i]
                q.append(i)

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
distance = [[0] * (N+1) for _ in range(N+1)]
for i in range(N-1):
    a, b, c = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    distance[a][b] = c
    distance[b][a] = c
arr = [list(map(int, input().split())) for _ in range(M)]
for j, k in arr:
    print(bfs(j,k))
