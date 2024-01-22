import sys
from collections import deque
# 3. bfs입력
def bfs():
    pass
# 4. dfs입력
def dfs():
    pass

input = sys.stdin.readline
# 1. 입력받기
n, m, k = map(int, input().split())
graph = [[False] * (n + 1) for _ in range(n + 1)]
visited = [False] * (n + 1)
# 2. 그래프 정보 입력
for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True
print(graph)
