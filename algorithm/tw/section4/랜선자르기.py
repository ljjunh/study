import sys
input = sys.stdin.readline
n, m = map(int,input().split())
arr = sorted([int(input()) for _ in range(n)])
lt = 1
rt = max(arr)
while lt <= rt:
    mid = (lt + rt) // 2
    cnt = 0
    for i in arr:
        cnt += i // mid
    if cnt >= m:
        lt = mid + 1
    else:
        rt = mid - 1
print(rt)
    