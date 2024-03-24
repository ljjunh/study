def recur(n):
    global ans
    if n == N:
        ans += 1
        return
    for i in range(N):
        if not visited1[i] and not visited2[n-i] and not visited3[n+i]:
            visited1[i] = 1
            visited2[n-i] = 1
            visited3[n+i] = 1
            recur(n+1)
            visited1[i] = 0
            visited2[n-i] = 0
            visited3[n+i] = 0


N = int(input())
visited1 = [0] * N
visited2 = [0] * (N * 2)
visited3 = [0] * (N * 2)
ans = 0
recur(0)
print(ans)