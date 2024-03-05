from collections import deque
string = input() + " "
stack = deque([])
for i in string:
    if i == " " and ">" not in stack and "<" not in stack:
        while stack:
            print(stack.pop(), end = "")
        print(" ", end = "")
    elif i == ">":
        stack.append(i)
        while stack:
            print(stack.popleft(), end = "")
    elif i == "<":
        while stack:
            print(stack.pop(), end = "")
        stack.append(i)
    else:
        stack.append(i)