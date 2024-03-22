import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    # 1. q, visited 생성
    visited = [[[0] * M for _ in range(N)] for _ in range(H)]
    q = deque()
    # 2. q에 초기 데이터 삽입, 안익은 토마토 카운트
    cnt = 0
    for h in range(H):
        for i in range(N):
            for j in range(M):
                if graph[h][i][j] == 1: # 익은 토마토
                    q.append((h,i,j))
                    visited[h][i][j] = 1
                elif graph[h][i][j] == 0: # 안익은 토마토
                    cnt += 1 # 갯수 기록
    while q:
        th, tx, ty = q.popleft()
        # 6방향, 범위 내, 미방문, 안익은 토마토
        for dh, dx, dy in ((0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1), (-1, 0, 0), (1, 0, 0)):
            nh, nx, ny = th + dh, tx + dx, ty + dy
            if 0 <= nh < H and 0 <= nx < N and 0 <= ny < M and not visited[nh][nx][ny] and not graph[nh][nx][ny]:
                q.append((nh, nx, ny))
                visited[nh][nx][ny] = visited[th][tx][ty] + 1
                cnt -= 1 #익혔으니까 안익은 토마토에서 -1
    if cnt == 0: # 전부 다 익었을때
        return visited[th][tx][ty] - 1
    else:
        return -1


M, N, H = map(int, input().split())
graph = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
ans = bfs()
print(ans)