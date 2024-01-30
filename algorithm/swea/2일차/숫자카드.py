T = int(input())
for i in range(1, T + 1):
    n = int(input())
    arr = list(input().rstrip())
    max_num = 0
    for j in arr:
        if int(j) > max_num:
            max_num = int(j)
    temp = [0] * (max_num + 1)
    for k in arr:
        temp[int(k)] += 1
    count = 0
    idx = 0
    for m in range(len(temp)):
        if temp[m] >= count:
            count = temp[m]
            idx = m
    print(f"#{i} {idx} {count}")
