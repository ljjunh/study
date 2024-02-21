import sys
from collections import deque
input = sys.stdin.readline

def bfs(idx):
    visited = [False] * (N + 1)
    visited[idx] = True
    cnt = 1
    q = deque([idx])
    while q:
        v = q.popleft()
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
                cnt += 1
    return cnt


N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
arr = []
for i in range(M):
    a, b = map(int, input().split())
    graph[b].append(a)

max_num = 0
for i in range(1, N + 1):
    cnt = bfs(i)
    if cnt > max_num:
        max_num = cnt
        arr.clear()
        arr.append(i)
    elif cnt == max_num:
        arr.append(i)
        
print(*arr)