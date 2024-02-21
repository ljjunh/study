def enq(idx):
    global hq, last
    last += 1
    hq[last] = idx

    c = last
    p = c // 2

    while p and hq[p] > hq[c]:
        hq[p], hq[c] = hq[c], hq[p]
        c = p
        p = c // 2


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    hq = [0] * (N + 1)
    last = 0
    res = 0

    for i in arr:
        enq(i)

    while last > 0:
        res += hq[last // 2]
        last = last // 2
    print(f"#{tc} {res}")
