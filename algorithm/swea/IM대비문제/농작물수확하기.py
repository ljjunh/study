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
            answer += sum(arr[i][i - N//2 : -(i-N//2)])
    print(f"#{tc} {answer}")       