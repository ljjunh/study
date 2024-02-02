T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    arr_90 = []
    for i in range(n):
        temp = []
        for j in range(n-1, -1, -1):
            temp.append(arr[j][i])
        arr_90.append(temp)

    arr_180 = []
    for i in range(n-1, -1, -1):
        temp = []
        for j in range(n-1, -1, -1):
            temp.append(arr[i][j])
        arr_180.append(temp)

    arr_270 = []
    for i in range(n-1, -1, -1):
        temp = []
        for j in range(n):
            temp.append(arr[j][i])
        arr_270.append(temp)

    print(f"#{tc}")
    for i in range(n):
        print(*arr_90[i], sep ="", end = " ")
        print(*arr_180[i], sep = "", end = " ")
        print(*arr_270[i], sep = "", end = " ")
        print()