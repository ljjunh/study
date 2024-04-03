import sys
input = sys.stdin.readline
from collections import deque
# for문으로 안익은 토마토 개수를 cnt에 추가하고,  익은 토마토는 방문처리를 한 뒤 큐에 넣는다.
# while문으로 큐에 들어가있는 익은 토마토에서 주위의 안익은 토마토를 익히면서 
# 얼마나 걸리는지 visited배열에 저장하고 방문할때마다 안익은토마토를(cnt) -1씩 
# 해주면서while문을 나온 뒤에는 
# 안익은 토마토가 없으면(cnt == 0) 큐에서 가장마지막에 나온 좌표의 visited배열에 저장된 값을 출력
# 안익은 토마토가 있으면(cnt != 0) -1출력
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dh = [0, 0, 0, 0, 1, -1]

def bfs():
    q = deque()
    cnt = 0
    for h in range(H):
        for i in range(N):
            for j in range(M):
                if graph[h][i][j] == 1:
                    q.append((h, i, j))
                    visited[h][i][j] = 1
                elif graph[h][i][j] == 0:
                    cnt += 1
    while q:
        ch, cx, cy = q.popleft()
        for k in range(6):
            nh, nx, ny = ch + dh[k], cx + dx[k], cy + dy[k]
            if 0 <= nh < H and 0 <= nx < N and 0 <= ny < M and not visited[nh][nx][ny] and graph[nh][nx][ny] == 0:
                q.append((nh,nx,ny))
                visited[nh][nx][ny] = visited[ch][cx][cy] + 1
                cnt -= 1
    if cnt == 0:
        return visited[ch][cx][cy] -1
    else:
        return -1


M, N, H = map(int, input().split())
graph = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
visited = [[[0] * M for _ in range(N)] for _ in range(H)]
ans = bfs()
print(ans)