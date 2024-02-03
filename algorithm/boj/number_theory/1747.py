n = int(input())
arr = [0] * 10000001
for i in range(2, len(arr)):
    arr[i] = i

for i in range(2, int(len(arr) ** 0.5)+1):
    if arr[i] == 0:
        continue
    for j in range(i+i, len(arr), i):
        arr[j] = 0

for i in range(2, len(arr)):
    if arr[i] == 0:
        continue
    if arr[i] < n:
        continue
    temp = list(str(arr[i]))
    temp2 = 0
    for j in range(len(temp) // 2):
        if temp[j] != temp[-j-1]:
            temp2 += 1
    if temp2 == 0:
        print(arr[i])
        break
