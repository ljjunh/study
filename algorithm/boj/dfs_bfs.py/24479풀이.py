import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs(idx):
    global graph, visited, answer, order
    visited[idx] = True
    answer[idx] = order
    order += 1

    for i in graph[idx]: # 호출된 재귀함수의 idx와 연결된 노드가
        if not visited[i]: # 아직 방문되지 않았으면 호출
            dfs(i)
    

# 0. 입력 및 초기화
N, M, R = map(int, input().split())
MAX = 100000 + 10
graph = [[] for _ in range(N+1)]
visited = [False] * MAX
answer = [0] * MAX
order = 1
# 1. graph에 연결 정보 채우기
for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
# 2. 오름차순 정렬
for i in range(1, N+1):
    graph[i] = sorted(graph[i])

# 3. DFS 호출
dfs(R)
# 4. 출력
for i in range(1, N+1):
    print(answer[i])