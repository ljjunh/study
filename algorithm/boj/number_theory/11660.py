import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = [[0] * (N+1) for _ in range(N+1)]
for i in range(1, N+1):
    tmp = list(map(int, input().split()))
    for j in range(1, N+1):
        arr[i][j] = tmp[j-1]

graph = [[0] * (N+1) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, N+1):
        graph[i][j] = graph[i][j-1] + graph[i-1][j] - graph[i-1][j-1] + arr[i][j]
for i in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    ans = 0
    ans = graph[x2][y2] - graph[x2][y1-1] - graph[x1-1][y2] + graph[x1-1][y1-1]
    print(ans)