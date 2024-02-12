import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [i for i in range(1, n+1)]
que = []
num = 0
for i in range(n):
    num += m - 1
    if num >= len(arr):
        num = num % len(arr)
    que.append(arr.pop(num))
print(str(que).replace("[", "<").replace("]", ">"))