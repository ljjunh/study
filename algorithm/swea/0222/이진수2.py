T = int(input())
for tc in range(1, T + 1):
    n = float(input()) 
    res = ""
    base = 2
    ex = -1
    i = 1
    while n != 0 and i < 13:
        if n >= base ** ex:
            res += "1"
            n -= base ** ex
        else:
            res += "0"
        ex -= 1
        i += 1
    if n != 0:
        print(f"#{tc} overflow")
    else:
        print(f"#{tc} {res}")
    