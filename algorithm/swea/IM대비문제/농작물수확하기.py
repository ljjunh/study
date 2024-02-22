T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    answer = 0
    for i in range(N):
        if i == 0 or i == N:
            answer += arr[i][N//2]
        elif i == N // 2:
            answer += sum(arr[i])
        elif i < N // 2:
            answer += sum(arr[i][N//2 - i : N//2 + i + 1])
        elif i > N // 2:
            # 두번째 고쳐야함
            answer += sum(arr[i][i - N//2 : N//2 + i + 1 + N -i])
    print(answer)       
            #answer += arr[i][j]
            # 0번째 줄 : N // 2
            # 1번째 줄 : 가운데인덱스 - 1 ~ 가운데 인덱스 + 1
            # 2번째 줄 : 가운데 인덱스 -2 ~ 가운데 인덱스 + 2
            # n // 2번째 줄 : 전부
            # n //2번째 + 1 ~ 마지막 : 역순