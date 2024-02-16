from collections import deque

def bfs(idx):
    global graph, visited, G, answer
    visited[idx] = 1
    q = deque([idx])

    while q:
        v = q.popleft()
        if visited[G] != 0:
            answer = visited[G] - 1
            return
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = visited[v] + 1

T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split()) # V노드의 개수 E 간선개수
    graph = [[] for _ in range(V+1)]
    visited = [0] * (V+1)
    answer = 0
    for _ in range(E):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)
    S, G = map(int, input().split()) # S출발 G도착
    
    bfs(S)

    print(f"#{tc} {answer}")
