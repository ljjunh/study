N, K = map(int, input().split())
arr = list(map(int, input()))
stack = []
for i in arr:
    while stack and K > 0 and stack[-1] < i:
        stack.pop()
        K -= 1
    stack.append(i)
if K != 0:
    print(*stack[:-K], sep = "")
else:
    print(*stack, sep = "")