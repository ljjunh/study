def binary_search(arr, target, s, e):
    if s > e:
        return None
    mid = (s + e) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, s, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, e)


n, m = map(int, input().split())
arr = list(map(int,input().split()))
arr.sort()
result = binary_search(arr, m, 0, n - 1)
if result == None:
    pass
else:
    print(result + 1)