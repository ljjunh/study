T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    
    min_num = N * M
    for i in range(N - 2):
        for j in range(i + 1, N - 1):
            cnt = 0
            for k in range(i + 1):
                cnt += arr[k].count("B")
                cnt += arr[k].count("R")
            for k in range(i + 1, j + 1):
                cnt += arr[k].count("W")
                cnt += arr[k].count("R")
            for k in range(j + 1, N):
                cnt += arr[k].count("W")
                cnt += arr[k].count("B")
            if min_num > cnt:
                min_num = cnt
    print(f"#{tc} {min_num}")