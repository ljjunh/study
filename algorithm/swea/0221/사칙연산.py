import math
for tc in range(1, 11):
    N = int(input())
    arr = [[] for _ in range(N + 1)]
    left = [0] * (N + 1)
    right = [0] * (N + 1)
    for i in range(N):
        s = input().split()
        if len(s) == 4:
            arr[int(s[0])] = s[1]
            left[int(s[0])] = int(s[2])
            right[int(s[0])] = int(s[3])   
        elif len(s) == 2:
            arr[int(s[0])] = int(s[1])

    for i in range(N, 0, -1):
        if arr[i] == "-":
            arr[i] = arr[left[i]] - arr[right[i]]
        elif arr[i] == "+":
            arr[i] = arr[left[i]] + arr[right[i]]
        elif arr[i] == "*":
            arr[i] = arr[left[i]] * arr[right[i]]
        elif arr[i] == "/":
            arr[i] = arr[left[i]] / arr[right[i]]
            
    print(f"#{tc} {math.trunc(arr[1])}")
        
