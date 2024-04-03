import sys
from collections import deque
input = sys.stdin.readline
# for문으로 안익은 토마토 개수를 세고 익은 토마토는 방문처리를 하고 큐에 넣어놓고
# while문으로 큐에 들어가있는 익은 토마토에서 안익은 토마토를 익히면서 
# 얼마나 걸리는지 visited배열에 저장하고 방문할때마다 안익은토마토를 -1씩 해주면서while문을 나오고 나서 
# 안익은 토마토가 없으면 큐에서 가장마지막에 나온 좌표의 visited배열에 저장된 값을 출력
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