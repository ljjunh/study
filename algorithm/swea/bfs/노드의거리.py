from collections import deque
T = int(input())

def bfs(idx):
    global end, ans
    visited[idx] = True
    q = deque([idx])
    while q:
        v = q.popleft()
        if v == end:
            ans = visited[v] - 1
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = visited[v] + 1
    # 목적지를 방문하지 못한 경우
    return 0
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]
    visited = [0] * (V + 1)
    ans = 0
    for i in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    start, end = map(int, input().split())
    bfs(start)
    print(f"#{tc} {ans}")