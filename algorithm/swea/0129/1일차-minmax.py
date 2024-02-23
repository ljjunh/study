T = int(input())
for i in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    max_num = 0
    min_num = 2147000000
    for j in arr:
        if j > max_num:
            max_num = j
        if j < min_num:
            min_num = j
    print(f"#{i + 1} {max_num - min_num}")