N = int(input())
dict = {}
for i in range(N):
    dict[input()] = 1
for i in range(N-1):
    dict[input()] = 0
for key, val in dict.items():
    if val == 1:
        print(key)
        break