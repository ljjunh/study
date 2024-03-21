from collections import deque

def bfs(idx):
    global ans
    visited[idx] = 1
    q = deque()
    q.append(idx)
    ans = idx
    while q:
        v = q.popleft()
        if visited[ans] < visited[v] or (visited[ans]==visited[v] and ans < v):
            ans = v
        for i in graph[v]:
            if visited[i]:
                continue
            visited[i] = visited[v] + 1
            q.append(i)

for tc in range(1, 11):
    N, S = map(int, input().split())
    tmp = list(map(int, input().split()))
    graph = [[] for _ in range(101)]
    for i in range(0, N, 2):
        graph[tmp[i]].append(tmp[i+1])
    visited = [0] * 101
    ans = 0
    bfs(S)
    print(f"#{tc} {ans}")