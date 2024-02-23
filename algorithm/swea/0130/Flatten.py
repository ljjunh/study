for tc in range(1, 11):
    n = int(input())
    arr = list(map(int, input().split()))
    for i in range(n):
        arr.sort()
        if arr[-1] - arr[0] <= 1:
            arr.sort()
            print(f"#{tc} {arr[-1] - arr[0]}")
            break
        arr[arr.index(arr[-1])] -= 1
        arr[arr.index(arr[0])] += 1
        if i == n - 1:
            arr.sort()
            print(f"#{tc} {arr[-1] - arr[0]}")

# for tc in range(1, 11):
#     n = int(input())
#     arr = list(map(int, input().split()))
#     for i in range(n):
#         if max(arr) - min(arr) <= 1:
#             print(f"#{tc} {max(arr) - min(arr)}")
#             break
#         arr[arr.index(max(arr))] -= 1
#         arr[arr.index(min(arr))] += 1
#         if i == n - 1:
#             print(f"#{tc} {max(arr) - min(arr)}")