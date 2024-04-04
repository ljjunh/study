def dfs(x, y, cnt):
    global visited, ans
    ans = max(ans, cnt)  # 최대값 구하는거니까 재귀할때마다 최대값 교체
    for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        nx, ny = x + dx, y + dy
        # 4방향, 범위 내, 중복 값x
        if 0 <= nx < N and 0 <= ny < M and not visited[ord(graph[nx][ny])]:
            visited[ord(graph[nx][ny])] = 1  # 갈수있을대까지 방문처리하면서 방문
            dfs(nx, ny, cnt + 1)
            visited[ord(graph[nx][ny])] = 0  # 갔다와서 다시 0으로 초기화
            # 초기화 안하면 다른 루트로 가는거 확인 못함


N, M = map(int, input().split())
graph = list(input() for _ in range(N))
visited = [0] * 91  # 아스키Z : 90 이고 idx는 0부터 시작하니까 90 + 1
visited[ord(graph[0][0])] = 1  # 첫번째 좌표 방문처리
ans = 1  # 첫번째좌표 정답에 추가
dfs(0, 0, 1)  # [0], [0], ans
print(ans)
