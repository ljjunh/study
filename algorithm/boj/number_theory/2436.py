def func_gcd(a, b):
    while a % b != 0:
        tmp = a % b
        a = b
        b = tmp
    return b
def func_lcm(a, b):
    return a * b // gcd
gcd, lcm = map(int, input().split())
ab = gcd * lcm
a = b = 0
for i in range(gcd, int(ab ** 0.5)+1, gcd):
        if func_gcd(i, ab//i) == gcd:
            if func_lcm(i, ab//i) == lcm:
                a = i
                b = ab//i
print(a, b)
