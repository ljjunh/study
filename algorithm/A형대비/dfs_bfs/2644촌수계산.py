import sys
input = sys.stdin.readline
from collections import deque

def bfs(x, e):
    visited = [0] * (N+1)
    q = deque()
    q.append(x)
    while q:
        v = q.popleft()
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = visited[v] + 1
    if visited[e]:
        print(visited[e])
    else:
        print(-1)
N = int(input())
s, e = map(int, input().split())
M = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
bfs(s, e)
