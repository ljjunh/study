from collections import deque
import sys
input = sys.stdin.readline

def dfs(idx):
    global graph, visited
    visited[idx] = 1
    q = deque([idx])    
    while q:
        v = q.popleft()
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = v


N = int(input())
graph = [[] * (N+1) for _ in range(N+1)]
visited = [0] * (N+1)
for _ in range(N-1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

dfs(1)
for i in range(2, N+1):
    print(visited[i])