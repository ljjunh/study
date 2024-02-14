import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def dfs(idx):
    global cnt, graph, visited
    visited[idx] = cnt
    for i in graph[idx]:
        if not visited[i]:
            cnt += 1
            dfs(i)
        
# 0. 입력받기, graph, visited 초기화
n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
cnt = 1
# 1. graph 정보 입력
for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
for i in graph:
    i.sort()
# 2. dfs호출
dfs(r)
# 3. 출력
print(*visited[1:], sep = "\n")