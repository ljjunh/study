from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = deque(list(range(1, n+1)))
res = []
while arr:
    for _ in range(m-1):
        arr.append(arr.popleft())
    res.append(str(arr.popleft()))
print("<", ", ".join(res), ">", sep = "")