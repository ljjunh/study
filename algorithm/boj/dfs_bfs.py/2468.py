import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, t):
    visited[x][y] = True
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if not visited[nx][ny] and graph[nx][ny] > t:
            dfs(nx, ny, t)
    
N = int(input())
MAX = 100 + 10
graph = [[0] * MAX for _ in range(MAX)]
visited = [[False] * MAX for _ in range(MAX)]
min_num = 1
max_num = 0
res = 1 # 입력값전부 1111일때 높이가0이면 1은 출력되야하니까
for i in range(1, N + 1):
    s = list(map(int, input().split()))
    for j in range(1, N + 1):
        graph[i][j] = s[j-1]
        if graph[i][j] > max_num:
            max_num = graph[i][j]
        
for t in range(min_num, max_num + 1):
    cnt = 0
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if graph[i][j] > t and not visited[i][j]:
                dfs(i, j, t)
                cnt += 1
    visited = [[False] * MAX for _ in range(MAX)]
    if res < cnt:
        res = cnt
print(res)
