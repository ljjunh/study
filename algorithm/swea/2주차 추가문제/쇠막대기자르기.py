T = int(input())
for tc in range(1, T + 1):
    arr = input()
    stack = []
    cnt = 0
    temp = False
    for i in arr:
        if i == "(":
            stack.append(i)
            temp = True
        elif i == ")":
            if temp == True:
                stack.pop()
                cnt += len(stack)
                temp = False
            else:
                stack.pop()
                cnt += 1 
    print(f"#{tc} {cnt}")