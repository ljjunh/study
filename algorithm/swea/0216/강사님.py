# 상하좌우
dr = [-1, 1, 0, 0] 
dc = [0, 0, -1, 1]

n = 7
maze = [[0,0,0,0,0,0,0],
        [0,1,1,1,1,1,0],
        [0,1,0,1,0,1,0],
        [0,0,0,1,0,0,0],
        [1,0,1,1,1,0,1],
        [1,0,1,99,0,0,0],
        [0,0,1,1,1,0,1],
        ]

# (r, c)가 유효한 인덱스인지 판별해주는 함수
def is_valid(r, c):
    return 0<= r < n and 0 <= c < n

# 탐색을 시작할 위치(sr, sc)
def bfs(sr, sc):
    # 중복체크 배열
    visited = [[0] * n for _ in range(n)]
    
    # 큐 생성
    q = []
    # 시작 위치 추가
    q.append((sr, sc))
    visited[sr][sc] = 1 # 재방문 막기
    
    # 미로를 탈출할 때까지 반복
    while q:
        # 큐에서 위치 하나 뽑아 오기
        r, c = q.pop(0)
        # (r, c)가 도착점인가?
        if maze[r][c] == 99:
            print(f"탈출 : ({r},{c}), 거리 : {visited[r][c]}")
            break
        # 이(r,c)의 상하좌우를 탐색하며 갈 수 있는 곳은 큐에 추가
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            #(nr, nc)가 탐색 가능한 위치인지 판별
            # 배열의 범위(유효한 인덱스)
            # 벽이 아님
            # 방문한 적이 없어야 함
            if is_valid(nr, nc) and maze[nr][nc] != 1 and not visited[nr][nc]:
                # (nr, nc)는 방문해야 할 위치
                q.append((nr, nc))
                visited[nr][nc] = visited[r][c] + 1

bfs(0,0)
