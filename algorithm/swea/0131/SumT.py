T = 10
for tc in range(1, T + 1):
    int(input()) # 필요없는 입력이 들어오면 저장하지 않고 입력만 받고 날리기
    N = 100
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 최댓값
    max_v = 0

    sum_dia1 = 0
    sum_dia2 = 0

    #행, 열, 대각선 최댓값 구하기
    for i in range(N):
        #행이 바뀔때마다 행의 합을 구하기
        sum_r = 0
        # 열이 바뀔때마다 열의 합을 구하기
        sum_c = 0

        sum_dia1 += arr[i][i]
        sum_dia2 += arr[i][N-1-i]
        for j in range(N):
            sum_r += arr[i][j]
            sum_c += arr[j][i]
        #최댓값 비교
        max_v = max(sum_r, sum_c, sum_dia1, sum_dia2)
    
    print(f"{tc} {max_v}")