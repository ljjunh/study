import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(idx, count):
    global graph, visited, end, answer
    visited[idx] = True
    if idx == end:
        answer = count
        return
    for i in range(1, n+1):
        if not visited[i] and graph[idx][i]:
            dfs(i, count + 1)

# 0. 입력 및 초기화
n = int(input()) # 노드
start, end = map(int, input().split()) # 촌수 계산해야 할 사람 둘
m = int(input()) # 엣지 개수
MAX = 100 + 10
graph = [[False] * MAX for _ in range(MAX)]
visited = [False] * (MAX)
answer = -1
# 1. graph에 정보 입력
for _ in range(m):
    x, y = map(int, input().split())
    graph[x][y] = True
    graph[y][x] = True
# 2. dfs호출
dfs(start, 0)
# 3. 출력
print(answer)