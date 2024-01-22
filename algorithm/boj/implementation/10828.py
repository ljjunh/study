import sys
import re
input = sys.stdin.readline
N = int(input())
arr = []
for _ in range(N):
    order = input()
    if "push" in order:
        num = int(re.sub(r'[^0-9]','',order))
        arr.append(num)
    elif "pop" in order:
        if len(arr) <= 0:
            print(-1)
        else:
            print(arr.pop())
    elif "size" in order:
        print(len(arr))
    elif "empty" in order:
        if len(arr) > 0:
            print(0)
        else:
            print(1)
    elif "top" in order:
        if len(arr) > 0:
            print(arr[-1])
        else:
            print(-1)