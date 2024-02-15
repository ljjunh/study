import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(idx):
    global graph, visited, answer
    visited[idx] = True

    for next in graph[idx]:
        if not visited[next]:
            answer[next] = idx
            dfs(next)


# 0. 입력 및 초기화
N = int(input())
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
answer = [0] * (N + 1)
# 1. 그래프 정보 채우기
for _ in range(N - 1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
# 2. DFS 호출
dfs(1)
# 3. 출력
for i in range(2, N + 1):
    print(answer[i])