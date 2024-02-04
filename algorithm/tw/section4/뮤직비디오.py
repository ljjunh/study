n, m = map(int, input().split())
arr = list(map(int, input().split()))
lt = max(arr)
rt = sum(arr)
res = 0
while lt <= rt:
    mid = (lt + rt) // 2
    total = 0
    cnt = 1
    for i in arr:
        if total + i > mid:
            cnt += 1
            total = 0
        total += i
    
    if cnt <= m:
        res = mid
        rt = mid - 1
    else:
        lt = mid + 1
print(res)

