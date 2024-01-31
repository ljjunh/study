from collections import deque
n = int(input())
arr = list(map(int, input().split()))
arr = deque(arr)
res = []
ment = ""
while arr:
    if len(res) == 0:
        if arr[0] > arr[-1]:
            res.append(arr.pop())
            ment += "R"
        else:
            res.append(arr.popleft())
            ment += "L"
    if len(arr) == 1:
        if arr[0] > res[-1]:
            res.append(arr.pop())
            ment += "L"
            break
        else:
            break

    if arr[0] > arr[-1]:
        if arr[-1] > res[-1]:
            res.append(arr.pop())
            ment += "R"
        elif arr[0] > res[-1]:
            res.append(arr.popleft())
            ment += "L"
        else:
            break    
    else:
        if arr[0] > res[-1]:
            res.append(arr.popleft())
            ment += "L"
        elif arr[-1] > res[-1]:
            res.append(arr.pop())
            ment += "R"
        else:
            break
print(len(res))
print(ment)