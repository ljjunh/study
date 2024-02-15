from collections import deque
for t in range(10):
    t = int(input())
    q = deque(list(map(int, input().split())))
    i = 1
    while True:
        if i > 5:
            i = 1
        q.append(q.popleft() - i)
        i += 1
        if q[-1] <= 0:
            print(f"#{t}", end =" ")
            for i in range(len(q)):
                if q[i] < 0:
                    q[i] = 0
                print(q[i], end = " ")
            print()
            break


