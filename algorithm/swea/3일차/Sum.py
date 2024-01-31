T = 10
for tc in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    row_sum = 0
    col_sum = 0
    # 행 최댓값
    for i in range(100):
        temp = 0
        for j in range(100):
            temp += arr[i][j]
        if temp > row_sum:
            row_sum = temp

    # 열 최댓값
    for i in range(100):
        temp = 0
        for j in range(100):
            temp += arr[j][i]
        if temp > col_sum:
            col_sum = temp

    dia_1 = 0 # 왼쪽 대각선
    dia_2 = 0 # 오른쪽 대각선
    for i in range(100):
        dia_1 += arr[i][i]
    for i in range(100):
        dia_2 += arr[i][100-i-1]
    
    res = [row_sum, col_sum, dia_1, dia_2]
    result = 0
    for i in res:
        if i > result:
            result = i
    print(f"#{tc} {result}")