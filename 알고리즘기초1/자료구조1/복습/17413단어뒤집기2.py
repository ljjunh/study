string = input()+" "
stack = []
temp = False
for i in string:
    if i == " " and temp == False:
        while stack:
            print(stack.pop(), end = "")
        print(" ", end = "")
    elif i == "<":
        temp = True
        while stack:
            print(stack.pop(), end = "")
        stack.append(i)
    elif i == ">":
        stack.append(i)
        while stack:
            print(stack.pop(0), end = "")
        temp = False
    else:
        stack.append(i)