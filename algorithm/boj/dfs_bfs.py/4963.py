import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

def dfs(x, y):
    visited[x][y] = True
    
    for i in range(8):
        nx, ny = x + dx[i], y + dy[i]
        if not visited[nx][ny] and graph[nx][ny]:
            dfs(nx, ny)


while True:
    W, H = map(int, input().split())
    if W == 0 or H == 0:
        break
    MAX = 50 + 10
    graph = [[False] * MAX for _ in range(MAX)]
    visited = [[False] * MAX for _ in range(MAX)]
    answer = 0
    for i in range(1, H + 1):
        s = list(map(int, input().split()))
        for j in range(1, W+1):
            graph[i][j] = (s[j - 1] == 1)
    for i in range(1, H + 1):
        for j in range(1, W + 1):
            if not visited[i][j] and graph[i][j]:
                dfs(i, j)
                answer += 1
    
    print(answer)    
            
        
