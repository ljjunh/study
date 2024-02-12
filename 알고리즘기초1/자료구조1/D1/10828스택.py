import sys
input = sys.stdin.readline
n = int(input())
arr = []
for i in range(n):
    order = input().split()
    if order[0] == "push":
        arr.append(order[1])
    elif order[0] == "pop":
        if len(arr) > 0:
            print(arr.pop())
        else:
            print(-1)
    elif order[0] == "size":
        print(len(arr))
    elif order[0] == "empty":
        if len(arr) == 0:
            print(1)
        else:
            print(0)
    elif order[0] == "top":
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[-1])