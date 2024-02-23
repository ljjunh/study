T = int(input())
arr = list(range(1, 13))
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    length = len(arr)
    cnt = 0
    for i in range(1, 1<<length):
        sum_num = 0
        tmp = 0
        for j in range(length):
            if i & (1<<j):
               sum_num += arr[j]
               tmp += 1
        if sum_num == m and tmp == n:
            cnt += 1
    print(f"#{tc} {cnt}")
