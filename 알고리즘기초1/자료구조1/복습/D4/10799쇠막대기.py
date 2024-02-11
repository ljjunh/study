s = input()
stack = []
cnt = 0
state = False
for i in s:
    if i == "(":
        stack.append(i)
        state = True
    elif i == ")" and state == True:
        stack.pop()
        cnt += len(stack)
        state = False
    else:
        stack.pop()
        cnt += 1
print(cnt)
