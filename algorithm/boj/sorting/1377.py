N = int(input())
arr = [(int(input()), i) for i in range(N)]
arr = sorted(arr)
max = 0
for i in range(N):
    if arr[i][1] - i > max:
        max = arr[i][1] - i
print(max + 1)