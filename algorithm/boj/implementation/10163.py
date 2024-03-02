import sys
input = sys.stdin.readline
N = int(input())
arr = [[0] * 1001 for _ in range(1001)]
for i in range(1, N + 1):
    x, y, w, h = map(int, input().split())
    for j in range(x, x+w):
        for k in range(y, y+h):
            arr[j][k] = i
cnt = [0] * (N + 1)
for i in arr:
    for j in i:
        cnt[j] += 1
for i in range(1, N + 1):
    print(cnt[i])