T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [0] * 5001
    for i in range(N):
        A, B = map(int, input().split())
        for j in range(A, B + 1):
            arr[j] += 1
    P = int(input())
    res = []
    for i in range(P):
        res.append(arr[int(input())])
    print(f"#{tc}", *res)
