import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(idx, before):
    global graph, visited, lst
    visited[idx] = True
    lst[idx] = before
    for i in graph[idx]:
        if not visited[i]:
            dfs(i, idx)



# 0. 입력 및 초기화
N = int(input())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
lst = [0] * (N+1) # 부모번호 저장 list
# 1. graph 정보 입력
for _ in range(N-1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

# 2. dfs 호출
dfs(1, 0)
# 3. 출력
print(*lst[2:], sep = "\n")