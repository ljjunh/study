T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    lt = 0
    rt = 0
    res =0
    temp = 0
    while True:
        if lt == n-1 and rt == n:
            break
        if rt > n - 1:
            lt += 1
            rt = 0
            temp = 0 
        if arr[lt][rt] == 0:
            rt += 1
            temp = 0
        elif arr[lt][rt] == 1:
            temp += 1
            if temp == m: 
                if rt == n-1:
                    res += 1
                elif arr[lt][rt+1] == 0:
                    res += 1
                elif arr[lt][rt+1] == 1:
                    rt += 1
            rt += 1
    print(f"#{tc} {res}")