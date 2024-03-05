import sys
input = sys.stdin.readline
n = 1000001
arr = [1] * n
for i in range(2, int(n ** 0.5) + 1):
    if arr[i]:
        for j in range(i * 2, n, i):
            arr[j] = 0
T = int(input())
for _ in range(T):
    num = int(input())
    cnt = 0
    for i in range(2, num//2 + 1):
        if arr[i] and arr[num-i]:
            cnt += 1
    print(cnt)


