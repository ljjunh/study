import sys
input = sys.stdin.readline
from collections import deque

def bfs(x, y):
    global L, R, state, ans, tmp
    # 첫 호출 먼저 방문처리
    visited[x][y] = tmp
    q = deque()
    q.append((x, y))
    bfs_state = False
    sum_num = graph[x][y] # (연합 인구수)초기값 미리 넣어줘야함 아래서 못넣음
    cnt = 1 # (연합 이루고 있는 칸 개수)
    while q:
        cx, cy = q.popleft()
        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nx, ny = cx + dx, cy + dy
            # 범위 내, 미방문, 차이가 L이상 R이하인 곳만
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and L <= abs(graph[cx][cy] - graph[nx][ny]) <= R:
                sum_num += graph[nx][ny]
                cnt += 1
                q.append((nx, ny))
                visited[nx][ny] = tmp
                state = True
                bfs_state = True

    # while문 나오고 나서 bfs_state가 True면, 인구이동이 있던거임
    # 국경이 열린칸들에 전부 sum_num // cnt를 넣어주고있음
    if bfs_state == True:
        for i in range(N):
            for j in range(N):
                if visited[i][j]== tmp: # 같은 연합끼리만 전부더하고 연합수만큼 나눠줌 
                    graph[i][j] = sum_num // cnt

N, L, R = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
ans = 0
# while문으로 인구이동이 발생 안할때까지 계속 반복
while True:
    # 하루마다 visited배열 초기화
    visited = [[0] * N for _ in range(N)]
    state = False
    tmp = 1
    # 갈수있는 나라 전부 확인
    for i in range(N):
        for j in range(N):
            # 미방문
            if not visited[i][j]:
                bfs(i, j)
                tmp += 1 # 연합끼리 visited 배열에 다르게 체크해야 해서 계속 +1씩
    # for문 끝나고 state가 True가 아니면, 아무것도 안바뀐거니까
    # while문 종료, state는 bfs에서 처리
    if state == False:
        break
    ans += 1 # break가 안걸리면 하루동안 인구이동 한거니까 정답 + 1
print(ans)
