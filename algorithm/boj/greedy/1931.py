import sys
input = sys.stdin.readline
n = int(input())
arr = []
for i in range(n):
    arr.append(tuple(map(int, input().split())))
arr.sort(key=lambda x: (x[1], x[0]))
temp = []
for i in arr:
    if len(temp) == 0:
        temp.append(i)
    elif temp[-1][1] <= i[0]:
        temp.append(i)
print(len(temp))
