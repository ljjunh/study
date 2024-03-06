N = int(input())
ans = 0
for A in range(0, N + 1):
    for B in range(0, N + 1):
        for C in range(0, N + 1):
            if A + B + C == N:
                if A != 0 and B != 0 and C != 0:
                    if A % 2 == 0:
                        if C - B >= 2:
                            ans += 1
print(ans) 
    