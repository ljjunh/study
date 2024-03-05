n = int(input())
for i in range(n):
    s = input() + " "
    stack = []
    for j in s:
        if j == " ":
            while stack:
                print(stack.pop(), end = "")
            print(end = " ")        
        else:
            stack.append(j)
    print()