T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    wi = list(map(int, input().split()))
    ti = list(map(int, input().split()))
    wi.sort(reverse=True)
    ti.sort(reverse=True)
    ans = 0
    t = 0
    w = 0
    while True:
        if ti[t] >= wi[w]:
            ans += wi[w]
            t += 1
            w += 1
        else:
            w += 1
        if t == M or w == N:
            break
    print(f"#{tc} {ans}")
        
        