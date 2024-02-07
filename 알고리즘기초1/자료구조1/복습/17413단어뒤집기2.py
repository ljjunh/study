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
        print(" ")
        stack.append(i)
    elif i == ">":
        while stack:
            print(*stack, end = "")
    else:
        stack.append(i)
    