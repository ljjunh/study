import sys
from collections import deque

input = sys.stdin.readline


def bfs(idx):
    global graph, visited
    visited[idx] = True
    queue = deque([idx])
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
answer = 0
# 몇 덩어리 나오는지
for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(1, N + 1):
    if not visited[i]:
        bfs(i)
        answer += 1

print(answer)
