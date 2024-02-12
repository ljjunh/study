n, m = map(int, input().split())
arr = [True for _ in range(m+1)]
arr[1] = False
for i in range(2, int(m ** 0.5) + 1):
    j = 2
    while i * j <= m:
        arr[i*j] = False
        j += 1
for i in range(n, m+1):
    if arr[i] == True:
        print(i)
