n = int(input())
for _ in range(n):
    s = input()+ " "
    stack = []
    res = ""
    for i in s:
        if i == " ":
            while stack:
                res += stack.pop()
            res += i
        else:
            stack.append(i)
    print(res)