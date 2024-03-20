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
            visited[i] = visited[v] + 1
            q.append(i)
 
for tc in range(1, 11):
    N, S = map(int, input().split())
    arr = list(map(int, input().split()))
    graph = [[] for _ in range(101)]
    visited = [0] * 101
    for i in range(0, N, 2):
        graph[arr[i]].append(arr[i+1])
    bfs(S)
    tmp = max(visited)
    ans = 0
    for i in range(101):
        if visited[i] == tmp:
            ans = i
    print(f"#{tc} {ans}")