arr = [1] * 1001
arr[0] = 0
arr[1] = 0
for i in range(2, int(1001 ** 0.5)+1):
    for j in range(i * 2, 1001, i):
        arr[j] = 0
n = int(input())
temp = list(map(int, input().split()))
cnt = 0
for i in temp:
    if arr[i] == 1:
        cnt += 1
print(cnt)