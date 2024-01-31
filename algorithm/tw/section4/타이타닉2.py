n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
cnt = 0
lt = 0
rt = n -1
while lt <= rt:
    if arr[lt] + arr[rt] <= m:
        lt += 1
        rt -= 1
        cnt += 1
    else:
        rt -= 1
        cnt += 1
print(cnt)