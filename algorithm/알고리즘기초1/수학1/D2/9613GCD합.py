def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

for _ in range(int(input())):
    arr = list(map(int, input().split()))
    cnt = 0
    for i in range(1, arr[0]):
        for j in range(i+1, arr[0]+1):
            cnt += gcd(arr[i], arr[j])
    print(cnt)
