for tc in range(1, 11):
    n = int(input())
    s = input()
    stack = []
    op = []
    for i in s:
        if i != "+":
            stack.append(int(i))
        while op:
            stack.append(op.pop())
        if i == "+":
            op.append(i)
    res = []
    for i in stack:
        if i == "+":
            res.append(res.pop() + res.pop())
        else:
            res.append(i)
    print(f"#{tc} {res[-1]}")
        

