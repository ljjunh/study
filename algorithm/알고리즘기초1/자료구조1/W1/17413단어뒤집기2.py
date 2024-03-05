s = input() + " "
stack = []
state = False
answer = ""
for i in s:
    if i == " " and state == False:# 공백을 만나고 <>태그안이 아닐 때
        while stack:
            answer += stack.pop()
        answer += i
    elif i == "<":
        while stack:
            answer += stack.pop()
        state = True
        answer += i
    elif i == ">":
        while stack:
            answer += stack.pop(0)
        state = False
        answer += i
    else:
        stack.append(i)
print(answer)    