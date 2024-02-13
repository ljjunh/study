import sys
sys.setrecursionlimit(100000) # 안되면 0 하나씩 더 붙여보자
input = sys.stdin.readline

def dfs(v):
    visited[v] = True
    for i in arr[v]:
        if not visited[i]:
            dfs(i)
    
n, m = map(int, input().split()) # n = 정점, m = 간선
arr = [[] for _ in range(n+1)]
visited = [False] * (n + 1) # 정점의 개수보다 1개 더 (인덱스별로 쓰려고 일부러 인덱스0은 비워둠)
for _ in range(m): # 간선의 개수만큼 반복
    s, e = map(int, input().split())
    arr[s].append(e) # 양방향 그래프여서 양쪽에 다 추가
    arr[e].append(s)

cnt = 0

for i in range(1, n + 1):
    if not visited[i]:  # 연결 노드 중 방문하지 않았던 정점만 탐색
        cnt += 1
        dfs(i)
print(cnt)