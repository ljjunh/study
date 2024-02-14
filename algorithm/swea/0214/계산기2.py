icp = {"+": 1, "*": 2}
for tc in range(1, 11):
    n = int(input())
    s = input()
    postfix = ""
    stack = []

    for i in range(n):
        if s[i] not in icp:
            postfix += s[i]
        else:
            while stack and icp[stack[-1]] >= icp[s[i]]:
                postfix += stack.pop()
            stack.append(s[i])
    while stack:
        postfix += stack.pop()

    stack2 = []
    for i in postfix:
        if i not in icp:
            stack2.append(int(i)) 
        else:
            a = stack2.pop()
            b = stack2.pop()
            result = 0
            if i == "+":
                result = b + a
            elif i == "*":
                result = b * a
            stack2.append(result)
    print(f"#{tc} {stack2[-1]}")