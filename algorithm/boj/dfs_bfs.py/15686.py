from collections import deque
# 치킨집 돌아가면서 없애면서 완탐으로 치킨거리 최솟값 출력
# 0은 빈칸, 1은 집, 2는 치킨집
# 재방문 막고 거리는 치킨집좌표 - 가정좌표 
# visted, dist 배열 사용
# 1에서 출발
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ans = 0
for i in range(5):
    for j in range(5):
        if graph[i][j] == 1:
            visited = [[0] * N for _ in range(N)] # 방문
            dist = [[0] * N for _ in range(N)] # 거리
            sm = 2147000000
            q = deque()
            q.append((i, j))
            visited[i][j] = 1
            while q:
                x, y = q.popleft()
                if graph[x][y] == 2:
                    sm = min(sm, dist[x][y])
                for k in range(4):
                    nx, ny = x + dx[k], y + dy[k]
                    if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                        visited[nx][ny] = 1
                        dist[nx][ny] = dist[x][y] + 1
                        q.append((nx, ny))
            ans += sm
# 치킨거리 제대로 입력하고
# 치킨집 지우는것만 ㄱㄱ