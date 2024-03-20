from collections import deque
def bfs():
    q = deque()
    q.append((N, 0))
    while q:
        n, cnt = q.popleft()
        if n == M:
            print(f"#{tc} {cnt}")
            return
        if visited[n]:
            continue
        visited[n] = 1
        cnt += 1
        if 0 < n + 1 <= 10 ** 6:
            q.append((n+1, cnt))
        if 0 < n - 1 <= 10 ** 6:
            q.append((n-1, cnt)) 
        if 0 < n * 2 <= 10 ** 6:
            q.append((n*2, cnt)) 
        if 0 < n - 10 <= 10 ** 6:
            q.append((n-10, cnt)) 

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    visited = [0] * (10 ** 6 + 1)
    bfs()
    