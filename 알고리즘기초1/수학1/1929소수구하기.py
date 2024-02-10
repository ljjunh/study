def ss(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    print(n)
n, m = map(int, input().split())
for i in range(n, m+1):
    ss(i)