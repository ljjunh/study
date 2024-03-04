from collections import deque
s = input()
T = int(input())
for tc in range(1, T + 1):
    arr = input()
    dq = deque(s)
    for i in arr:
        if i in dq:
            if i != dq.popleft():
                print(f"#{tc} NO")
                break
    else:
        if not dq:
            print(f"#{tc} YES")
        else:
            print(f"#{tc} NO")
            