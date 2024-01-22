from collections import deque
import sys
input = sys.stdin.readline

n, m, v = map(int, input().split())
graph = [[False] * (n + 1) for _ in range(n + 1)] 
for i in range(m):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1

visited1 = [False] * (n + 1)
visited2 = [False] * (n + 1)

def dfs(v):
    #방문 처리
    visited1[v] = True
    #방문 후, 정점 출력
    print(v, end= " ")
    #방문 기록이 없고, 인덱스에 값이 있다면(연결되어있다면)
    for i in range(1, n + 1):
        if not visited1[i] and graph[v][i] == 1:
            dfs(i)

def bfs(v):
    q = deque([v])
    # 방문 처리
    visited2[v] = True
    # 큐안에 데이터가 없을때까지 실행
    while q:
        # 큐 맨 앞의 값을 꺼내서 출력
        v = q.popleft()
        print(v, end = " ")
        for i in range(1, n + 1):
            #방문 기록이 없고, 인덱스에 값이 있다면(연결되어있다면)
            if not visited2[i] and graph[v][i] == 1:
                q.append(i) #큐에 추가
                visited2[i] = True

dfs(v)
print()
bfs(v)