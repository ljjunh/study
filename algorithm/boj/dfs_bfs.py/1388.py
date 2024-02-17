import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs(x, y):
    visisted[x][y] = True
    if graph[x][y] == "-" and graph[x][y+1] == "-":
        dfs(x, y + 1)
    elif graph[x][y] == "|" and graph[x+1][y] == "|":
        dfs(x+1, y)

MAX = 50 + 10
N, M = map(int, input().split())
graph = [[""] * MAX for _ in range(MAX)]
visisted = [[False] * MAX for _ in range(MAX)]
for i in range(1, N+1):
    s = input()
    for j in range(1, M+1):
        graph[i][j] = s[j-1]

answer= 0
for i in range(1, N+1):
    for j in range(1, M+1):
        if not visisted[i][j]:
            dfs(i, j)
            answer += 1
        
print(answer)