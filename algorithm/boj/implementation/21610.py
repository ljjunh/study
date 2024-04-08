N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
clst1 = [(N - 1, 0), (N - 1, 1), (N - 2, 0), (N - 2, 1)]  # 구름초기위치

di, dj = [0, 0, -1, -1, -1, 0, 1, 1, 1], [0, -1, -1, 0, 1, 1, 1, 0, -1]
for _ in range(M):  # M번 입력받아서 반복처리
    D, S = map(int, input().split())
    # [1]구름이동 [2]물증가 [3]구름사라짐(clst2에 좌표저장)
    clst2 = []  # 이동할 구름의 위치(좌표)저장
    for ci, cj in clst1:
        ni, nj = (ci + di[D] * S + N) % N, (
            cj + dj[D] * S + N
        ) % N  # 양쪽끝이 연결되어 있으므로..
        arr[ni][nj] += 1  # 구름이 있는 칸 물 증가
        clst2.append((ni, nj))  # 물 증가한 칸 체크

    # 물복사 버그
    v = [[0] * N for _ in range(N)]
    for ci, cj in clst2:
        v[ci][cj] = 1
        for dii, djj in ((-1, -1), (-1, 1), (1, -1), (1, 1)):
            ni, nj = ci + dii, cj + djj
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] > 0:
                arr[ci][cj] += 1  # 대각선에 물이 있는 만큼 증가

    # [3] 전체순회 물>=2인자리 구름발생(물-=2), 단 clst2위치 제외
    clst1 = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] >= 2 and v[i][j] == 0:
                arr[i][j] -= 2
                clst1.append((i, j))
ans = 0
for lst in arr:
    ans += sum(lst)
print(ans)
