arr = [15, 30, 50, 10]

arr.sort()
sm = 0
for i in range(len(arr)):
    sm += arr[i] * (len(arr) - i -1)
print(sm)
