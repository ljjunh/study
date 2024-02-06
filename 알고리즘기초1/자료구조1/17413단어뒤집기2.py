string = input() + " "
stack = []
for i in string:
    stack.append(i)
    if i == " ":
        while stack:
            print(stack.pop(), end = "")
    
