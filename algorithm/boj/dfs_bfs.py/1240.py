import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    global cnt
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if not visited[nx][ny] and graph[nx][ny]:
            dfs(nx, ny)
            cnt += 1
    return cnt

N = int(input())
MAX = 25 + 10
graph = [[False] * MAX for _ in range(MAX)]
visited = [[False] * MAX for _ in range(MAX)]
answer = 0
arr = []
for i in range(1, N + 1):
    s = list(map(int, input().rstrip()))
    for j in range(1, N + 1):
        graph[i][j] = s[j-1]
for i in range(1, N+1):
    for j in range(1, N+1):
        if not visited[i][j] and graph[i][j]:
            cnt = 1
            arr.append(dfs(i, j))
            answer += 1
print(answer)
print(*sorted(arr), sep = "\n")