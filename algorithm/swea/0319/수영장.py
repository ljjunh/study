def recur(n, sm):
    global ans
    if sm >= ans:
        return
    
    if n >= 12:
        ans = min(ans, sm)
        return
    
    recur(n+1, sm + price[0] * plan[n])
    recur(n+1, sm + price[1])
    recur(n+3, sm + price[2])
    recur(n+12, sm + price[3])

T = int(input())
for tc in range(1, T + 1):
    price = list(map(int, input().split()))
    plan = list(map(int, input().split()))
    ans = 2147000000
    recur(0, 0)
    print(f"#{tc} {ans}")