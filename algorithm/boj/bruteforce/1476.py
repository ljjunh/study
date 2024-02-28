a, b, c = map(int, input().split())
E = S = M = year = 1
while True:
    if E == a and S == b and M == c:
        print(year)
        break
    year += 1
    E += 1
    S += 1
    M += 1
    if E == 16:
        E = 1
    if S == 29:
        S = 1
    if M == 20:
        M = 1