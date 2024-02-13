T = int(input())
for tc in range(1, T + 1):
    arr = list(input().split())
    stack = []
    state = 0
    for i in arr:
        if i not in "+-*/.":
            stack.append(int(i))
        elif i == ".":
            if len(stack) == 0: # 스택이 비어있는 경우
                state += 1
            if len(stack) >= 2:
                state += 1
        else:
            if len(stack) < 2: # 연산할 피연산자가 부족할 경우
                state += 1
            else:
                a = stack.pop()
                b = stack.pop()
                if i == "+":
                    stack.append(b + a)
                elif i == "/":
                    stack.append(b // a)
                elif i == "-":
                    stack.append(b - a)
                elif i == "*":
                    stack.append(b * a)
    if state == 0:
        print(f"#{tc} {stack.pop()}")
    else:
        print(f"#{tc} error")