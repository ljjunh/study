import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def dfs(idx):
    global graph, visited, cnt
    visited[idx] = cnt
    for i in graph[idx]:
        if not visited[i]:
            cnt += 1
            dfs(i)

# 0. 입력받기, graph, visited 초기화
n, m, r = map(int, input().split()) # n:노드 m:엣지 r:시작노드
graph = [[] for i in range(n + 1)]
visited = [0] * (n + 1)
cnt = 1
# 1. graph 정보입력
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
for i in graph:
    i.sort(reverse=True)

# 2. 함수 호출
dfs(r)
# 3. 출력
print(*visited[1:])