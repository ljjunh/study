import sys
input = sys.stdin.readline
from collections import deque

def bfs(s, e):
    visited = [0] * 200001
    visited[s] = 1
    q = deque()
    q.append(s)
    while q:
        v = q.popleft()
        if v == e:
            return visited[v] - 1
        for i in (v+1, v-1, v*2):
            if 0 <= i <= 200000 and not visited[i]:
                # 다음 이동좌표가 범위를 넘지 않고, 방문안했으면
                visited[i] = visited[v] + 1
                q.append(i)
    

N, K = map(int, input().split())
print(bfs(N, K))