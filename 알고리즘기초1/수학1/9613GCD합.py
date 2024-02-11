def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

t = int(input())
for i in range(t):
    res = 0
    arr = list(map(int, input().split()))
    for j in range(1, len(arr)-1):
        for k in range(j+1, len(arr)):
            res += gcd(arr[k], arr[j])
    print(res)