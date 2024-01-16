N = int(input())
for _ in range(N):
    ps = input()
    stack = []
    for i in ps:
        if i == "(":
            stack.append("(")
        elif i == ")":
            if len(stack) == 0:
                stack.append(")")
                break
            else:
                stack.pop()
    if len(stack) == 0:
        print("YES")
    else:
        print("NO")
            
