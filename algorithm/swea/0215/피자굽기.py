from collections import deque

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    q = deque([[] for _ in range(N)])
    temp = deque([[] for _ in range(M - N)])
    for i in range(N):
        q[i].append(arr[i])
        q[i].append(i + 1)
    for i in range(M - N):
        temp[i].append(arr[N + i])
        temp[i].append(N + i + 1)

    while len(q) > 1:
        q[0][0] = q[0][0] // 2
        if q[0][0] == 0:
            q.popleft()
            if temp:
                q.appendleft(temp.popleft())
        else:
            q.append(q.popleft())
    print(f"#{tc} {q[0][1]}")
