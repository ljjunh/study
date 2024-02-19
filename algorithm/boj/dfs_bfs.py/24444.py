import sys
input = sys.stdin.readline

def bfs(idx):
    global graph, visited, answer, order
    visited[idx] = True
    answer[idx] = order
    order += 1
    q = []
    q.append(idx)
    while q:
        v = q.pop(0)
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
                answer[i] = order
                order += 1
                 

# 0. 입력 받기
N, M, R = map(int, input().split())
MAX = 100000 + 10
graph = [[] for _ in range(N+1)]
visited = [False] * MAX
answer = [0] * MAX
order = 1
# 1. 그래프 정보 입력
for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

# 2. 오름차순
for i in range(1, N + 1):
    graph[i] = sorted(graph[i])

# 3. BFS 호출
bfs(R)
# 4. 출력
for i in range(1, N + 1):
    print(answer[i])