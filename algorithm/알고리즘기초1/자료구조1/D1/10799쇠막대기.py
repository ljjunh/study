string = input()
stack = []
res = 0
for i in range(len(string)):
    if string[i] == "(":
        stack.append(i)
    elif string[i] == ")":
        if stack[-1] == i-1:
            stack.pop()
            res += len(stack)
        else:
            stack.pop()
            res += 1
print(res)