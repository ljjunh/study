a, b = map(int, input().split())
n = int(input()) 
arr = list(map(int, input().split()))
arr = arr[::-1]
temp = 0
for i in range(len(arr)):
    temp += arr[i] * (a ** i)
res = []
while temp > 0:
    res.append(temp % b)
    temp = temp // b
res = res[::-1]
print(*res)