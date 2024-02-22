from collections import deque
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    ai = list(map(int, input().split()))
    bj = list(map(int, input().split()))
    if N < M:
        N, M = M, N
    if len(ai) < len(bj):
        ai, bj = bj, ai
    ai = deque(ai)
    answer = 0
    for i in range(N - M + 1):
        temp = 0
        for j in range(M):
            temp += ai[j] * bj[j]
        ai.popleft()
        if answer < temp:
            answer = temp
    print(f"#{tc} {answer}")

