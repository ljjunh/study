import sys
input = sys.stdin.readline

def dfs(idx):
    visited[idx] = True
    for i in range(1, n + 1):
        if not visited[i] and graph[idx][i]:
            dfs(i)


# 0. 입력받기, visited, graph 초기화
n, m = map(int, input().split()) # n : 노드   m : 엣지
graph = [[False] * (n + 1) for _ in range(n+1)]
visited = [False] * (n + 1)
cnt = 0
# 1. 그래프 입력
for i in range(m):
    x, y = map(int, input().split())
    graph[x][y] = True
    graph[y][x] = True
    
# 2. dfs호출
for i in range(1, n + 1):
    if not visited[i]:
        cnt += 1
        dfs(i)
# 3. 출력
print(cnt)        
