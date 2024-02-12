# 스택 사용
# n = int(input())
# for i in range(n):
#     arr = input()
#     stack = []
#     for i in arr:
#         if i == "(":
#             stack.append(i)
#         else:
#             if len(stack) != 0:
#                 if stack[-1] == "(":
#                     stack.pop()
#             elif len(stack) == 0:
#                     stack.append(i)
#                     break
#     if len(stack) > 0:
#         print("NO")
#     else:
#         print("YES")
        
n = int(input())
for i in range(n):
    arr = input()
    cnt = 0
    for i in arr:
        if i == "(":
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0:
            print("NO")
            break
    if cnt == 0:
        print("YES")
    elif cnt > 0:
        print("NO")
