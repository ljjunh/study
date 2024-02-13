T = int(input())
 
 
# r : 내가 r번째 행에 퀸을 놓을지 말지 정하고 있다
# remain : 놓을수 있는 남은 퀸의 개수
def bk(r, remain):
    global cnt
 
    # 1. 종료 조건
    if remain == 0 and r == N:
        # 정답 구하는 코드, 재귀 종료
        cnt += 1
        return
 
    # 2. 재귀 호출
    # r번째 행에 대해서 퀸을 놓을수 있는지 판단
    # 놓을수 있다면 놓아보고, r+1번째 행으로 퀸을 놓으러 간다
 
    # 현재 r번째 행에서 c번 열(0 ~ N-1)에다가 놓아보겠다.
    for c in range(N):
        # 현재 r,c 위치에 퀸을 놓을수 있는가? 검사
        # 이전에 내가 놓은 퀸중에 공격 가능한 위치에 있다면 고려하지않고 다음 위치 탐색
        can_place = True
 
        # 세로(상)에 내가 이전에 놓았던 퀸이 있는지 검사
        # 이전에 놓은 퀸은 0 ~ r-1 범위에 있을테니 거기까지만 검사
        for j in range(r):
            if board[j][c] == 1:
                can_place = False
                break
 
        for j in range(1, r + 1):
            # 대각선(좌상)에 내가 이전에 놓았던 퀸이 있는지 검사
            if r - j >= 0 and c - j >= 0 and board[r - j][c - j] == 1:
                # 대각선 좌상으로 j만큼 가다가 퀸을 찾으면 r,c는 놓을수 없음
                can_place = False
                break
 
            # 대각선(우상)에 내가 이전에 놓았던 퀸이 있는지 검사
            if r - j >= 0 and c + j < N and board[r - j][c + j] == 1:
                # 대각선 우상으로 j만큼 가다가 퀸을 찾으면 r,c는 놓을수 없음
                can_place = False
                break
 
        if can_place:
            # 이전에 내가 퀸을 공격할수 있는 위치에 놓은적이 없으면 r,c에 놓고
            # 다음 r+1번째 행에 퀸을 놓으러 가자
            board[r][c] = 1
            bk(r + 1, remain - 1)
            # r,c 에대해서 진행이 끝나고 나면 r,c에는 놓은적이 없다라고
            # 다시 되돌리는 과정이 필요하다 ( r,c+1 도 판단을 해야 하기 때문에)
            board[r][c] = 0
 
 
for tc in range(1, T + 1):
    N = int(input())
 
    # 체스 판
    board = [[0] * N for _ in range(N)]
 
    # 퀸을 놓을수 있는 경우의 수
    cnt = 0
 
    bk(0, N)
 
    print(f"#{tc} {cnt}")