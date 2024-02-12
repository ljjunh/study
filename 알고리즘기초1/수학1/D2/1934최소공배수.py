def gcd(a, b):
    if b == 0:
        return a
    return (gcd(b, a % b))

T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    print(n * m // gcd(n, m))