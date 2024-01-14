from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
que = deque()
for i in range(n):
    order = list(input().split())
    if order[0] == "push":
        que.append(int(order[1]))
    elif order[0] == "pop":
        if len(que) == 0:
            print(-1)
        else:
            print(que.popleft())
    elif order[0] == "size":
        print(len(que))
    elif order[0] == "empty":
        if len(que) == 0:
            print(1)
        else:
            print(0)
    elif order[0] == "front":
        if len(que) == 0:
            print(-1)
        else:
            print(que[0])
    elif order[0] == "back":
        if len(que) == 0:
            print(-1)
        else:
            print(que[-1])