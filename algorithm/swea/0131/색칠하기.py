T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    result = 0
    arr = [[0] * 10 for _ in range(10)]
    for i in range(n):
        a, b, c, d, e = map(int, input().split())
        for j in range(a, c + 1):
            for k in range(b, d + 1):
                arr[j][k] += e
                if arr[j][k] == 3:
                    result += 1
    print(f"#{tc} {result}")