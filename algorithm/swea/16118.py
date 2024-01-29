T = int(input())
for i in range(T):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    max_arr = 0
    min_arr = 2147000000
    for j in range(n - m + 1):
        temp = sum(arr[j:j+m])
        if temp < min_arr:
            min_arr = temp
        if temp > max_arr:
            max_arr = temp
    print(f"#{i + 1} {max_arr - min_arr}")