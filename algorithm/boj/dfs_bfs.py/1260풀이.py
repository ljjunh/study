import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs(idx):
    visited[idx] = True
    print(idx, end = " ")
    for i in range(1, N+1):
        if not visited[i] and graph[idx][i]:
            dfs(i)

def bfs():
    queue = []
    queue.append(V)
    visited[V] = True
    while queue:
        idx = queue.pop(0)
        print(idx, end = " ")
        for i in range(1, N + 1):
            if not visited[i] and graph[idx][i]:
                queue.append(i)
                visited[i] = True
# 0. 입력 및 초기화
N, M, V = map(int, input().split())

MAX = 1000 + 10
graph = [[False] * MAX for _ in range(MAX)]
visited = [False] * MAX

# 1. graph에 연결 정보 채우기 2차원배열써서 오름차순 안해도 자동으로 됨
for _ in range(M):
    x, y = map(int, input().split())
    graph[x][y] = True
    graph[y][x] = True
# 2. DFS 호출
dfs(V)
print()

visited = [False] * MAX # visited배열 한번 더 쓰지말고 그냥 bfs 호출하기 전에 초기화 해줌

# 3. BFS 호출
bfs()