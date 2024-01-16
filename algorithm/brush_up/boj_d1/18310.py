n = int(input())
home = sorted(list(map(int, input().split())))
result = 0
if len(home) % 2 == 0:
    result = len(home) // 2 - 1
    print(home[result])
else:
    result = len(home) // 2
    print(home[result])