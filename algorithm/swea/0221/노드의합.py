T = int(input())
for tc in range(1, T + 1):
    N, M, L = map(int, input().split())
    arr = [0] * (N + 1)
    for i in range(M):
        a, b = map(int, input().split())
        arr[a] = b
    for i in range(N, 1, -1):
        arr[i//2] += arr[i]
    print(f"#{tc} {arr[L]}")