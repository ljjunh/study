import sys
input = sys.stdin.readline
n = 1000001
arr = [1] * n
for i in range(3, int(n ** 0.5) + 1, 2):
    if arr[i]:
        for j in range(i * 2, n, i):
            arr[j] = 0
while True:
    k = int(input())
    if k == 0:
        break
    for i in range(3, int(k / 2) + 1, 2):
        if arr[i] and arr[k - i]:
            print(f"{k} = {i} + {k - i}")
            break
    else:
        print("Goldbach's conjecture is wrong.")