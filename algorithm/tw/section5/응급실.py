from collections import deque
N, M = map(int, input().split())
q = [(i, val) for i, val in enumerate(list(map(int, input().split())))]
q = deque(q)
cnt = 0
while True:
    cur = q.popleft()
    if any(cur[1] < x[1] for x in q):
        q.append(cur)
    else:
        cnt += 1
        if cur[0] == M:
            print(cnt)
            break