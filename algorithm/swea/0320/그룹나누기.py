from collections import deque
def bfs(idx):
    visited[idx] = 1
    q = deque()
    q.append(idx)
    while q:
        v = q.popleft()
        for i in graph[v]:
            if visited[i]:
                continue
            visited[i] = 1
            q.append(i)


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    graph = [[] for _ in range(N+1)]
    visited = [0] * (N+1)
    ans = 0
    for i in range(0, len(arr), 2):
        graph[arr[i]].append(arr[i+1])
        graph[arr[i+1]].append(arr[i])
    for i in range(1, N + 1):
        if visited[i]:
            continue
        bfs(i)
        ans += 1
    print(f"#{tc} {ans}")
        