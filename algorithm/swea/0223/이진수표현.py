T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    for i in range(N):
        if M & 1 == 0:
            print(f"#{tc} OFF")
            break
        M = M >> 1
    else:
        print(f"#{tc} ON")