import sys
input = sys.stdin.readline
from collections import deque

def bfs(s, e):
    visited = [-1] * 100001
    visited[s] = 0
    q = deque()
    q.append(s)
    while q:
        v = q.popleft()
        if v == e:
            print(visited[v])
            return
        for i in (v*2, v-1, v+1):
            if 0 <= i <= 100000 and visited[i] == -1:
                if i == v*2:
                    visited[i] = visited[v]
                    q.appendleft(i)
                else:
                    visited[i] = visited[v] + 1
                    q.append(i)

# x-1 : 1초
# x+1 : 1초
# x*2 : 0초
N, K = map(int, input().split())
bfs(N, K)