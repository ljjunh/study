def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

n, s = map(int, input().split())
arr = list(map(int, input().split()))

for i in range(n):
    arr[i] = abs(arr[i] - s)
res = arr[0]
for i in range(1, n):
    res = gcd(res, arr[i])
print(res)
