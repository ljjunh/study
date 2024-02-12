import sys
input = sys.stdin.readline
arr = [1] * 1000001
for i in range(2, int(1000001 ** 0.5)+1):
    if arr[i]:
        for j in range(i * 2, 1000001, i):
            arr[j] = 0

T = int(input())
for i in range(T):
    cnt = 0
    n = int(input())
    for i in range(2, n//2 + 1):
        if arr[i] and arr[n-i]:
            cnt += 1
    print(cnt)