# n = int(input())
# for i in range(n):
#     arr = list(input().split())
#     for i in arr:
#         print(i[::-1], end = " ")
#     print()

n = int(input())
for i in range(n):
    arr = input() + " "
    stack = []
    for i in arr:
        if i != " ":
            stack.append(i)
        else:
            while stack:
                print(stack.pop(), end = "")
            print(end = " ")
            

