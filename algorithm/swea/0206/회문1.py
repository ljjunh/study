T = 10
for tc in range(1, T + 1):
    n = int(input())
    arr = [list(input()) for _ in range(8)]
    cnt = 0
    for i in range(8): # i = 0~7
        for j in range(n-1, 8): # j = 3~7
            temp = arr[i][j-n+1:j+1]
            if temp == temp[::-1]:
                cnt += 1
    arr2 = []
    for i in range(8):
        a = []
        for j in range(8):
            a.append(arr[j][i])
        arr2.append(a)
    for i in range(8): # i = 0~7
        for j in range(n-1, 8): # j = 3~7
            temp = arr2[i][j-n+1:j+1]
            if temp == temp[::-1]:
                cnt += 1
    print(f"#{tc} {cnt}")