T = int(input())
for tc in range(1, T + 1):
    string = input()
    stack = []
    cnt = 0
    for i in string:
        if len(stack) == 0 and (i == "}" or i == ")"):
            cnt += 1
            break
        elif i == "{" or i == "(":
            stack.append(i)
        elif i == "}":
            if stack[-1] == "(":
                cnt += 1
                break
            else:
                stack.pop()
        elif i == ")":
            if stack[-1] == "{":
                cnt += 1
                break
            else:
                stack.pop()
    if cnt > 0 or len(stack) > 0:
        print(f"#{tc} 0")
    else:
        print(f"#{tc} 1") 