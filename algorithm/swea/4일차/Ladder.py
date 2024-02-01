T = 10
for tc in range(1, T + 1):
    int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    lt = 0
    rt = 0
    for i in range(100):
        for j in range(100):
            if arr[i][j] == 2:
                lt = i
                rt = j
    dx = [-1, 0, 0]
    dy = [0, -1, 1]
    d = 0
    while True:
        if lt == 0:  # 출발 지점에 도달했을 때
            print("#{} {}".format(tc, rt))  # 출발 지점의 열 인덱스를 출력합니다.
            break

        # 이동할 위치 계산
        nx = lt + dx[d]
        ny = rt + dy[d]

        # 다음 위치가 유효한 범위 내에 있고, 이동할 수 있는 경우
        if 0 <= nx < 100 and 0 <= ny < 100 and arr[nx][ny] == 1:
            if d == 0:  # 현재 위쪽으로 이동 중
                if ny > 0 and arr[nx][ny - 1] == 1:  # 왼쪽으로 이동할 수 있는 경우
                    d = 1
                else:  # 왼쪽으로 이동할 수 없는 경우
                    d = 2
            elif d == 1:  # 현재 왼쪽으로 이동 중
                d = 0  # 위로 이동
            elif d == 2:  # 현재 오른쪽으로 이동 중
                d = 0  # 위로 이동

        # 다음 위치로 이동
        lt = nx
        rt = ny   