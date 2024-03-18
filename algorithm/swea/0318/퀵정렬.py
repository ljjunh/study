def quick_sort(arr, s, e):
    if s >= e:
        return
    pivot = s
    left = s + 1
    right = e

    while left <= right:
        while left <= e and arr[left] <= arr[pivot]:
            left += 1
        while right > s and arr[right] >= arr[pivot]:
            right -= 1
        if left > right:
            arr[right], arr[pivot] = arr[pivot] , arr[right]
        else:
            arr[left], arr[right] = arr[right], arr[left]
    
    quick_sort(arr, s, right-1)
    quick_sort(arr, right+1, e)

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    quick_sort(arr, 0, N-1)
    print(f"#{tc} {arr[N//2]}")