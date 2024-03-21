def dijkstra(s, N):
    visited = [0] * N
    visited[s] = 1
    for i in range(N):
        D[i] = graph[s][i]
    for _ in range(N):
        min_v = 2147000000
        w = 0
        for i in range(N):
            if visited[i] == 0 and min_v > D[i]:
                min_v = D[i]
                w = i
        visited[w] = 1
        for j in range(N):
            if 0 < graph[w][j] < 2147000000:
                D[j] = min(D[j], D[w] + graph[w][j])   


T = int(input())
for tc in range(1, T + 1):
    N, E = map(int, input().split())
    N += 1
    graph = [[2147000000] * (N) for _ in range(N)]
    for i in range(N):
        graph[i][i] = 0
    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s][e] = w
    D = [0] * N
    dijkstra(0, N)
    print(f"#{tc} {D[-1]}")