n, m = map(int, input().split())
cnt = 0
arr = list(map(int, str(n)))
stack = []
for i in arr:
    while stack and stack[-1] < i and m > 0:
        stack.pop()
        m -= 1
    stack.append(i)
if m != 0:
    print(*stack[:-m], sep = "")
else:
    print(*stack, sep = "")