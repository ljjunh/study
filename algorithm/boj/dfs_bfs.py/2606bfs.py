import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    global graph, visited, cnt
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                cnt += 1
                visited[i] = True

# 0. 입력 및 초기화
N = int(input())
E = int(input())
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
cnt = 0
# 1. 그래프 정보입력
for _ in range(E):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
# 2. 함수호출
bfs(1) 
# 3. 출력
print(cnt)
