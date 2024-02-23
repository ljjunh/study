T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    arr = [[0] * n for _ in range(n)]
    lt = 0
    rt = 0
    num = 1
        #우하좌상
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    d = 0
    while num <= n*n:
        if d == 0 and (rt == n-1 or arr[lt][rt+1] != 0):
            d += 1
        elif d == 1 and (lt == n-1 or arr[lt+1][rt] != 0):
            d += 1
        elif d == 2 and (rt == 0 or arr[lt][rt-1] != 0):
            d += 1
        elif d == 3 and (lt == 1 or arr[lt-1][rt] != 0):
            d = 0
        
        arr[lt][rt] += num
        lt += dx[d]
        rt += dy[d]
        num += 1
    print(f"#{tc}")
    for i in range(n):  
        print(" ".join(map(str, arr[i])))