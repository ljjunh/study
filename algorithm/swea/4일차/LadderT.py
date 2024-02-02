T = 10
N = 100
for tc in range(1, T + 1):
    input() # 쓸데없는 입력 처리 저장x

    ladder = [list(map(int, input().split())) for _ in range(N)]
    
    # 끝에서부터 거슬러 올라올 거니까
    r = 99
    c = -1

    # 도착지점부터 찾기
    for i in range(N):
        if ladder[r][i] == 2:
            c = i
    #   좌  우  상 순서로 탐색
    dr = [0, 0, -1]
    dc = [-1, 1, 0]

    while r > 0:
        # 현재 위치에서 좌, 우를 먼저 보고 사다리가 있으면 좌, 우 부터 간다
        # 좌, 우로 움직일 수 없으면 위로 간다
        for d in range(3):
            nr = r + dr[d]
            nc = c + dc[d]
            # 다음 위치가 움직일 수 있는 위치인가 확인
            if 0 < nr < N and 0 < nc < N and ladder[nr][nc] == 1:
                # 갈 수 있는 위치면 현재위치를 다음갈곳으로 갱신
                r = nr
                c = nc
                # 내가 왔던 길은 다시 가지 않도록 0으로 바꾸면 다시 안감
                ladder[r][c] = 0
                # 다음 방향은 탐색하지 않도록 break
                break
    print(f"#{tc} {c}")



