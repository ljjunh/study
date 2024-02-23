import sys
from collections import deque
input = sys.stdin.readline

# 도움요청하기 전까지의 시간출력 1칸당 1초
# 더이상 먹을수 있는게 없으면 도움요청(gg)
# 젤 처음 아기상어 크기 2
# 4방향이동
# 자기보다 큰곳으로는 못감
# 크기가 같으면 지나가기만 함
# 크기가 작으면 먹어치움
# 먹어치우면 빈칸됨
# 먹을 수 있는게 여러마리면, 가장 가까운거 먹으러감
# 4방향중 먹을 수 있는 것중 가장 윗행, 윗행이 여러마리면 왼쪽꺼먹음
# 자기크기와 같은 물고기 먹으면 크기 1증가 (크기2아기상어가 1짜리 두개먹으면 크기 3이 됨)
N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
a, b = 0, 0
# 아기상어 위치 찾기
for i in range(N):
    for j in range(N):
        if graph[i][j] == 9:
            a, b = i, j
            graph[a][b] = 0

shark_size = 2 # 상어 크기
eat = 0
time = 0
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

q = deque()
q.append((a, b))
while q:
    x, y = q.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            if graph[nx][ny] < graph[x][y]:
                q.append((nx, ny))
                time += 1
                eat += graph[nx][ny]
                if shark_size <= eat:
                    eat -= shark_size
                    shark_size += 1
                graph[nx][ny] = 0
            elif graph[nx][ny] == graph[x][y]:
                q.append((nx, ny))
                time += 1
print(time)
# 종료조건 구해야됨
# 그냥 크든 작든 같든 visited배열에 체크하면 종료됨 아닌데 이러면 크기 다시 커져서 먹을수있으면 어쩜