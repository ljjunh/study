def binary(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    if n % 2 == 0:
        return binary(n // 2) + "0"
    else:
        return binary(n // 2) + "1"
N = int(input())
print(binary(N))