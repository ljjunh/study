import sys
input = sys.stdin.readline
n = int(input())
stack = []
operator = []
cnt = 1
temp = 0
for i in range(n):
    num = int(input())
    while cnt <= num:
        stack.append(cnt)
        operator.append("+")
        cnt += 1
    if stack[-1] == num:
        stack.pop()
        operator.append("-")
    else:
        print("NO")
        temp += 1
        break
if temp == 0:
    for i in operator:
        print(i)