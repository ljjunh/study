n, m = map(int, input())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

def dfs(x, y):
    # 주어진 범위를 벗어나면 종료
    if x <= -1 or y <= -1 or x >= n or y >= m:
        return False
    # 현재 노드를 방문하지 않았다면
    if graph[x][y] == 0:
        graph[x][y] == 1 # 방문처리
        #상,하,좌,우
        dfs(x - 1, y) 
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1
print(result)