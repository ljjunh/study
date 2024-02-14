import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs(idx):
    global graph, visited, answer, order
    visited[idx] = True # 방문처리
    answer[idx] = order # 방문순서 담기
    order += 1 # 방문순서 증가
    
    for i in graph[idx]: # 그래프의 idx번째와 연결된 노드중
        if not visited[i]: # 방문되지 않으면 호출
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
# 2. 내림차순 정렬
for i in range(1, N+1):
    graph[i] = sorted(graph[i], reverse=True)
# 3. DFS 호출
dfs(R)
# 4. 출력
for i in range(1, N+1):
    print(answer[i])