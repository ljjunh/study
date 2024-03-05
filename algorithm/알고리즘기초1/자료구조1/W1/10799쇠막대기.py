s = input()
stack = []
top = ""
cnt = 0
for i in s:
    if i == "(":
        stack.append(i)
        top = i
    elif i == ")" and top == "(":
        stack.pop()
        cnt += len(stack)
        top = i
    elif i == ")" and top == ")":
        stack.pop()
        cnt += 1
        top = i
print(cnt)
