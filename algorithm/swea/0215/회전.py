from collections import deque
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    deq = deque(list(map(int, input().split())))
    for i in range(M):
        deq.append(deq.popleft())
    print(f"#{tc} {deq[0]}")