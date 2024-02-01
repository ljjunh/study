n, m = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
    
for i in range(n-1, 0, -1):
    idx = arr.index(max(arr[:i+1]))
    if idx != i:
        arr[idx], arr[i] = arr[i], arr[idx]
        cnt += 1
        if cnt == m:
            print(arr[idx], arr[i])
            exit()
print(-1)
        