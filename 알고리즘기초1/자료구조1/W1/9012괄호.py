T = int(input())
for _ in range(T):
    s = input()
    stack = []
    for i in s:
        if i == "(":
            stack.append(i)
        elif i == ")" and len(stack) == 0:
            print("NO")
            break
        else:
            stack.pop()
    else:
        if stack:
            print("NO")
        else:
            print("YES")