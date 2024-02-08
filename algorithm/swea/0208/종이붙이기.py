T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [0] * 301
    arr[10] = 1
    arr[20] = 3
    for i in range(30, 301, 10):
        arr[i] = arr[i-10] + arr[i-20] * 2
    print(f"#{tc} {arr[n]}")
