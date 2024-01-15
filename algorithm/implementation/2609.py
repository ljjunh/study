n, m = map(int, input().split())
if n < m:
    n, m = m, n


def gcd(n, m):
    while m > 0:
        n, m = m, n % m
    return n


def lcm(n, m):
    return n * m // gcd(n, m)


print(gcd(n, m))
print(lcm(n, m))
