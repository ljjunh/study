import sys
input = sys.stdin.readline
def dfs(idx):
    global answer
    visited[idx] = True
    answer += 1

    for i in range(1, n + 1):
        if not visited[i] and graph[idx][i]:
            dfs(i)

# 0. 입력받기
n = int(input()) # 노드
m = int(input()) # 엣지
graph = [[False] * (n + 1) for _ in range(n + 1)]
visited = [False] * (n + 1)
answer = 0
# 1. 그래프 정보 입력
for i in range(m):
    x, y = map(int, input().split())
    graph[x][y] = True
    graph[y][x] = True

# 2. dfs 호출
dfs(1)
# 3. 출력
print(answer - 1)