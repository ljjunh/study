from collections import deque
n, k = map(int, input().split())
arr = [i for i in range(1, n+1)]
cnt = 0
res = []
while arr:
    cnt += k - 1
    if cnt >= len(arr):
        cnt = cnt % len(arr)
    res.append(arr.pop(cnt))
print(str(res).replace("[", "<").replace("]", ">"))