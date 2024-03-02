L = int(input())
N = int(input())
arr = [0] * (L + 1)
ans = 0
res = 0
for i in range(1, N+1):
    s, e = map(int, input().split())
    if e - s > ans:
        ans = e - s
        res = i
    for j in range(s, e + 1):
        if arr[j] == 0:
            arr[j] = i
cnt = (0,0)
for i in range(1, N + 1):
    if cnt[1] < arr.count(i):
        cnt = (i, arr.count(i))
print(res)
print(cnt[0])