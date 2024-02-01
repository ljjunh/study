def selectionSort(arr, n):
    for i in range(n - 1):
        min_idx = i
        for j in range(i+1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    selectionSort(arr, n)
    print(f"#{tc}", *arr)