N = int(input())
arr = [[0] * 100 for _ in range(100)]
for i in range(N):
    a, b = map(int, input().split())
    for i in range(b, b + 10):
        for j in range(a, a + 10):
            arr[i][j] += 1
cnt = 0
for i in arr:
    for j in i:
        if j >= 1:
            cnt += 1
print(cnt)