T = int(input())
for i in range(1, T + 1):
    n = int(input())
    arr = list(map(int, input()))
    max_cnt = 0
    cnt = 0
    for j in arr:
        if j == 1:
            cnt += 1
        elif j == 0:
            cnt = 0
        if max_cnt < cnt:
            max_cnt = cnt
    print(f"#{i} {max_cnt}")

    