# 첫줄은 무조건 화이트
# N+1~ M-1중에 블루가 제일 많은거 찾고 그 윗줄 아랫줄 비교해서
# 윗줄에 화이트가 많으면 그 위로 전부 화이트
# 윗줄에 블루가 많으면 거기까지 블루 하고 다시 탐색
# 아랫줄도 똑같이
# 마지막줄은 무조건 레드
# 만약 이게 정답이 아니면
# 1행부터 가운데-1까지 w,b개수 새서 많은걸로 재할당..
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    # 첫줄, 마지막줄
    cnt = 0
    cnt += arr[0].count("B")
    cnt += arr[0].count("R")
    cnt += arr[-1].count("W")
    cnt += arr[-1].count("B")
    
    # 가운뎃줄
    max_blue = 0
    blue_line = 0 # 블루로 칠할 행 번호
    for i in range(1, N - 1):
        temp = arr[i].count("B")
        if max_blue < temp:
            max_blue = temp
            blue_line = i
    cnt += arr[blue_line].count("W")
    cnt += arr[blue_line].count("R")

    # 1행 ~ 가운데-1행
    x = 0
    for i in range(1, blue_line):
        tmp_w = arr[i].count("W")
        tmp_b = arr[i].count("B")
        tmp_r = arr[i].count("R")
        if state == "white" and tmp_w > tmp_b:
            #만약 2쨰줄에 화이트가 많으면
            cnt += tmp_b + tmp_r
        else: # 블루가 더 많다면 아래 행마다 비교해야함
            x = i
  
    for _ in range(blue_line-x):
        for i in range(x, blue_line):
            # i부터 블루라인 전까지 경우의 수 전부해야되나...
            tmp_w = arr[i].count("W")
            tmp_b = arr[i].count("B")
            tmp_r = arr[i].count("R")
            


    # 가운데+1행 ~ N-1행
    state = "blue"
    for i in range(blue_line + 1, N - 1):
        tmp_w = arr[i].count("W")
        tmp_b = arr[i].count("B")
        tmp_r = arr[i].count("R")
        if state == "blue" and tmp_b > tmp_r:
            cnt += tmp_w + tmp_r
        else:
            cnt += tmp_b + tmp_w
            state = "red"
    print(cnt)