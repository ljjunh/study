T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    res = []
    for _ in range(5):
        max_num = 0
        min_num = 100
        for j in arr:
            if max_num < j:
                max_num = j
            if min_num > j:
                min_num = j
        res.append(max_num)
        arr.pop()
        res.append(min_num)
        arr.pop(0)
    print(f"#{tc}", *res)