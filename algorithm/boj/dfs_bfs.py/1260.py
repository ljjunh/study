import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(idx):
    global visited_dfs, graph
    visited_dfs[idx] = True
    print(idx, end = " ")
    for i in graph[idx]:
        if not visited_dfs[i]:
            dfs(i)

def bfs(idx):
    global visited_bfs, graph
    visited_bfs[idx] = True
    q = [idx]
    while q:
        v = q.pop(0)
        print(v, end = " ")
        for i in graph[v]:
            if not visited_bfs[i]:
                q.append(i)
                visited_bfs[i] = True
                


N, M, V = map(int, input().split()) # N 노드 M 엣지, V 시작점
graph = [[] * (N+1) for _ in range(N+1)]
visited_dfs = [False] * (N+1)
visited_bfs = [False] * (N+1)
for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(1, N + 1):
    graph[i] = sorted(graph[i])

dfs(V)
print()
bfs(V)