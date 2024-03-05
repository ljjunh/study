def count(n, v):
    cnt = 0
    while n >= v:
        cnt += n//v
        n = n // v
    return cnt
n, m = map(int, input().split())
two = count(n, 2) - count(n-m, 2) - count(m, 2)
five = count(n, 5) - count(n-m, 5) - count(m, 5)
print(min(two, five))
