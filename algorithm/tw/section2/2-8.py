import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

m = int(input())

for i in range(m):
    a, b, c = map(int, input().split())
    if b == 0:
        for j in range(c):
            arr[a-1].append(arr[a-1][0])
            arr[a-1].pop(0)
    elif b == 1:
        for j in range(c):
            arr[a-1].insert(0, arr[a-1][-1])
            arr[a-1].pop()
res = 0
for i in range(n):
    if i == len(arr) // 2:
        res += arr[i][n // 2]
    elif i % 2 == 1:
        res += sum(arr[i]) - arr[i][0] - arr[i][-1]
    else:
        for j in arr[i]:
            res += j
print(res)


    