n = int(input())
for i in range(n):
    stack = 0
    s = input()
    for j in s:
        if j == "(":
            stack += 1
        else:
            if stack > 0:
                stack -= 1
            else:
                print("NO")
                break
    else:
        if stack == 0:
            print("YES")
        else:
            print("NO")