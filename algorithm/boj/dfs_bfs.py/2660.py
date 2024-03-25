from collections import deque
import sys
input = sys.stdin.readline

def bfs(idx):
    visited = [0] * (N+1)
    visited[idx] = 1
    q = deque()
    q.append(idx)
    while q:
        v = q.popleft()
        for i in graph[v]:
            if visited[i]:
                continue
            q.append(i)
            visited[i] = visited[v] + 1
    return max(visited) - 1

N = int(input())
graph = [[] for _ in range(N+1)]
while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
    graph[a].append(b)
    graph[b].append(a)
ans = []
for i in range(1, N + 1):
    ans.append(bfs(i))

print(min(ans), ans.count(min(ans)))
for idx, val in enumerate(ans):
    if min(ans) == val:
        print(idx+1, end=" ")
