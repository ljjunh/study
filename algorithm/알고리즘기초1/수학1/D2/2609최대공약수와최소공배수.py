def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

n, m = map(int, input().split())
res = gcd(n, m)
print(res)
print(res * (n // res) * (m // res))