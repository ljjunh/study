T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    res = 0
    for i in range(n):
        for j in range(n):
            temp = 0
            if i+m-1 < n and j+m-1 < n:
                for k in range(m):
                    for c in range(m):
                        temp += arr[i+k][j+c]
            if temp > res:
                res = temp
    print(f"#{tc} {res}")             