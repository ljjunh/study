from collections import deque
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def is_valid(tr, tc):
    return 0 <= tr < N and 0 <= tc < N

def bfs(sr, sc):
    global visited, graph, answer
    visited[sr][sc] = 1 # 방문처리
    q = deque([(sr, sc)])
    while q:
        r, c = q.popleft()
        if graph[r][c] == 3:
            answer = visited[r][c] - 2
            return
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if is_valid(nr, nc) and graph[nr][nc] != 1 and not visited[nr][nc]:
                q.append((nr, nc))
                visited[nr][nc] = visited[r][c] + 1


T = int(input())
for tc in range(1, T + 1):
    N = int(input()) #미로의 크기 N * N
    # 0 : 통로    1 : 벽   2 : 출발   3 : 도착
    graph = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for i in range(N)]
    fr, fc = 0, 0 # 시작위치
    answer = 0
    #시작위치 구하기
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 2:
                fr, fc = i, j
    bfs(fr, fc)
    print(f"#{tc} {answer}")
   