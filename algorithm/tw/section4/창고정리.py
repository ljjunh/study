n = int(input())
arr = list(map(int, input().split()))
m = int(input())
for i in range(m):
    arr[arr.index(max(arr))] -= 1
    arr[arr.index(min(arr))] += 1
print(max(arr) - min(arr))
