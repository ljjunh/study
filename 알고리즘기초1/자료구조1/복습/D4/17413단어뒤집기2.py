s = input() + " "
state = False
stack = []
res = ""
for i in s:
    if i == " " and state == False:
        while stack:
            res += stack.pop()
        res += i
    elif i == "<":
        state = True
        while stack:
            res += stack.pop()
        stack.append(i)
    elif i == ">":
        stack.append(i)
        while stack:
            res += stack.pop(0)
        state = False
    else:
        stack.append(i)
print(res)