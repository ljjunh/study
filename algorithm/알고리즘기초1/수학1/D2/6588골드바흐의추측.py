import sys
input = sys.stdin.readline
num = 1000001
arr = [1] * num
for i in range(3, int(num ** 0.5)+1, 2):
    if arr[i]:
        for j in range(i*2, num, i):
            arr[j] = 0

while True:
    n = int(input())
    if n == 0:
        break
    for i in range(3, n//2 + 1, 2):
        if arr[i] and arr[n-i]:
            print(f"{n} = {i} + {n-i}")
            break
    else:
        print("Goldbach's conjecture is wrong.")
