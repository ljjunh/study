from collections import deque
n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
arr = deque(arr)
cnt = 0
while arr:
    if len(arr) == 1: #요소가 1개일때 아래로 넘어가지 않게 하려고
        cnt+= 1
        break
    if arr[0] + arr[-1] <= m:
        cnt += 1
        arr.popleft()
        arr.pop()
    else:
        arr.pop()
        cnt += 1
print(cnt)