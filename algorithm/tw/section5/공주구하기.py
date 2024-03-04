from collections import deque
N, K = map(int, input().split())
arr = deque(list(range(1, N + 1)))
i = 0
while len(arr) > 1:
    if i == K-1:
        arr.popleft()
        i = 0
    else:
        arr.append(arr.popleft())
        i += 1
print(arr[0])
