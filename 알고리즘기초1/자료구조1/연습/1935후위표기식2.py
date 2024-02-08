import sys
input = sys.stdin.readline
n = int(input())
arr = input()
nums = [int(input()) for _ in range(n)]
alpha = [i for i in arr if i.isalpha()]
stack = []
for i in arr:
    if i.isalpha():
        stack.append(nums[ord(i)-65])
    else:
        if i == "+":
            stack.append(stack.pop() + stack.pop())
        elif i == "-":
            temp1 = stack.pop()
            temp2 = stack.pop()
            stack.append(temp2 - temp1)
        elif i == "*":
            temp1 = stack.pop()
            temp2 = stack.pop()
            stack.append(temp2 * temp1)
        elif i == "/":
            temp1 = stack.pop()
            temp2 = stack.pop()
            stack.append(temp2 / temp1)
res = 0
for i in stack:
    res += i
print(f"{res:.2f}")
