def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


a, b = map(int, input().split())
res = gcd(a, b)
print(res)
print(res * a // res * b // res)