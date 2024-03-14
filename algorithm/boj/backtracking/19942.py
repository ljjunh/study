def recur(n, a, b, c, d, price, use):
    global ans, ans_lst                                                                      
    if n == N:
        if a < min_arr[0] or b < min_arr[1] or c < min_arr[2] or d < min_arr[3]:
            return
        if ans > price:
            ans = price
            ans_lst = use
        return
    recur(n+1, a+arr[n][0], b+arr[n][1], c+arr[n][2], d+arr[n][3], price+arr[n][4], use + [n+1])
    recur(n+1, a, b, c, d, price, use)

N = int(input())
min_arr = list(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 2147000000
ans_lst = []
recur(0, 0, 0, 0, 0, 0, [])
if ans == 2147000000 and ans_lst == []:
    print(-1)
else:
    print(ans)
    print(*ans_lst)
# 2
# 0 0 0 10
# 0 0 0 10 1
# 0 0 0 5 0