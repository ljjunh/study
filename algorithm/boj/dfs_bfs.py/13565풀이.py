import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    global visited, graph, answer
    visited[x][y] = True
    
    if x == N: # x가 행 끝까지 갔을 경우
        answer = True
        return

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if graph[nx][ny] and not visited[nx][ny]:
            dfs(nx, ny)


# 0. 입력 및 초기화
N, M = map(int, input().split())
MAX = 1000 + 10
graph = [[False] * MAX for _ in range(MAX)]
visited = [[False] * MAX for _ in range(MAX)]

# 1. graph에 연결 정보 채우기
for i in range(1, N + 1):
    row = input()
    for j in range(1, M + 1):
        graph[i][j] = (row[j - 1] == "0") # 0이랑 1바꿔주는 식

# 2. DFS 호출
answer = False
for j in range(1, M + 1):
    if graph[1][j]:
        dfs(1, j)

# 3. 출력
print("YES" if answer else "NO")