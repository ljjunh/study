from collections import deque
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(sr, sc):
    global visited, graph, answer
    visited[sr][sc] = 1
    q = deque([(sr, sc)])
    while q:
        r, c = q.popleft()
        if graph[r][c] == 3:
            answer = 1
            return
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr <= 16 and 0 <= nc <= 16 and graph[nr][nc] != 1 and not visited[nr][nc]:
                q.append((nr, nc))
                visited[nr][nc] = visited[r][c] + 1



for _ in range(1, 11):
    tc = int(input())
    graph = [list(map(int, input())) for _ in range(16)]
    visited = [[0] * 16 for _ in range(16)]
    answer = 0
    bfs(1, 1)

    print(f"#{tc} {answer}")