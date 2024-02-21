# 그림이 없으면 가장 넓은 그림의 넓이는 0
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    global temp
    graph[x][y] = 0
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if graph[nx][ny]:
            dfs(nx, ny)
            temp += 1
            

N, M = map(int, input().split())
MAX = 500 + 10
graph = [[0] * MAX for _ in range(MAX)]
answer = [0]
cnt = 0 # dfs호출 횟수(그림의 개수)
for i in range(1, N + 1):
    s = list(map(int, input().split()))
    for j in range(1, M + 1):
        graph[i][j] = s[j-1]

for i in range(1, N  + 1):
    max_num = 0
    for j in range(1, M + 1):
        if graph[i][j]:
            temp = 1
            dfs(i, j)
            cnt += 1
            answer.append(temp)
print(cnt)
print(max(answer))