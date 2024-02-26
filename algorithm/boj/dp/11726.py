def fibo(n):
    result = []
    a, b = 1, 1
    for i in range(n):
        result.append(a)
        a, b = b, a + b
    return result[-1]
n = int(input())
print(fibo(n+1) % 10007)