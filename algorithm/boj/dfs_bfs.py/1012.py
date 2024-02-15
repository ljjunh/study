T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split()) # M가로 N세로 K배추위치개수
    graph = [[0] * N for _ in range(M)]
    for i in range(K):
        x, y = map(int, input().split())
        graph[x][y] = 1