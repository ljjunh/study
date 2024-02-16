import sys
from collections import deque
input = sys.stdin.readline

def bfs(idx):
    global graph, visited, order, end, answer
    q = deque([idx])
    visited[idx] = 1
    while q:
        v = q.popleft()
        if visited[end] != 0:
            return
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = visited[v] + 1


n = int(input()) # 사람 수
start, end = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
answer = -1
order = 0
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

bfs(start)

print(visited[end] - 1)