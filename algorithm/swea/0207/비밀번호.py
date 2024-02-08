T = 10
for tc in range(1, T + 1):
    n, arr = map(str, input().split())
    stack = []
    i = 0
    while i < len(arr):
        if len(stack) == 0:
            stack.append(arr[i])
            i += 1
        elif stack[-1] == arr[i]:
            stack.pop()
            i += 1
        else:
            stack.append(arr[i])
            i += 1
    res = ""
    for i in stack:
        res += i
    print(f"#{tc} {res}")
