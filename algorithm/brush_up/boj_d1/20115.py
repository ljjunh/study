n = int(input())
drink = sorted(list(map(int, input().split())))
result = sum(drink[:-1]) / 2 + drink[-1]
print("%g"%result)