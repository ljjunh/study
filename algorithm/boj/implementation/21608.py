import sys
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N**2)]
arr = [[0] * N for _ in range(N)]
for lst in graph:
    max_cnt = max_emp = -1
    for i in range(N):
        for j in range(N):
            if arr[i][j] > 0:
                continue
            cnt = emp = 0
            # 빈자리가 아니면 다음반복으로
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nx, ny = i + dx, j + dy
                if 0 <= nx < N and 0 <= ny < N:
                    if arr[nx][ny] in lst:
                        cnt += 1
                    if arr[nx][ny] == 0:
                        emp += 1
            if max_cnt < cnt or max_cnt == cnt and max_emp < emp:
                # 좋아하는사람이 전보다 많으면 무조건 교체
                # 후보가 여러개면 빈칸의 수로 해야되니까
                # 전보다 emp가 더 많을때 교체
                # 3번조건은 max_emp < emp 더 클때만 교체되는거니까
                # 항상 행, 열 번호가 가장 작은게 들어감
                max_cnt, max_emp = cnt, emp
                ni, nj = i, j
    arr[ni][nj] = lst[0]
# 자리배치 끝난 뒤 만족도 합계 구하기
ans = 0
score = [0, 1, 10, 100, 1000]
tmp = [[] for _ in range((N**2)+1)]
for i in range(N**2):
    tmp[graph[i][0]] = graph[i][1:]

for i in range(N):
    for j in range(N):
        cnt = 0
        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nx, ny = i + dx, j + dy
            if 0 <= nx < N and 0 <= ny < N:
                if arr[nx][ny] in tmp[arr[i][j]]:
                    cnt += 1
        ans += score[cnt]
print(ans)                    