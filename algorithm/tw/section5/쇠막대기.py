arr = list(input())
stack = []
ans = 0
for i in arr:
    if i == ")" and x == "(":
        stack.pop()
        ans += len(stack)
    elif i == ")":
        stack.pop()
        ans += 1
    else:
        stack.append(i)
    x = i
print(ans)
