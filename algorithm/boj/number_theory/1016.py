n, m = map(int, input().split())
arr = list(range(n, m+1))
for i in range(2, int(m ** 0.5) + 1):
    a = i * i
    for j in range(m):
        if arr[j] % a == 0:
            arr[j] = 0
cnt = 0
for i in arr:
    if i != 0:
        cnt += 1
print(cnt)
