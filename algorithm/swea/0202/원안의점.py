T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    cnt = 0
    for i in range(n, -n-1, -1):
        for j in range(n, -n-1, -1):
            if (i ** 2) + (j ** 2) <= n**2:
                cnt += 1
    print(f"#{tc} {cnt}")