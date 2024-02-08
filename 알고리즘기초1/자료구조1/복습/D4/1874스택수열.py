import sys
input = sys.stdin.readline
n = int(input())
stack = []
op = []
cnt = 1
for i in range(n):
    num= int(input())
    while cnt <= num:
        stack.append(cnt)
        op.append("+")
        cnt += 1
    if stack[-1] == num:
        stack.pop()
        op.append("-")
    else:
        print("NO")
        break
else:
    for i in op:
        print(i)