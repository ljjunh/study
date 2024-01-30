import sys
input = sys.stdin.readline
n = int(input())
arr = []
for i in range(n):
    h, w = map(int, input().split())
    arr.append((h, w))
arr.sort(key = lambda x : -x[1])
temp = []
for i in arr:
    if len(temp) == 0:
        temp.append(i)
    elif temp[-1][0] <= i[0]:
        temp.append(i)
print(len(temp))