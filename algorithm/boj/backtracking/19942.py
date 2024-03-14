import sys
input = sys.stdin.readline
def recur(idx, A, B, C, D, E):
    global ans, used, ans_used

    if a <= A and b <= B and c <= C and d <= D:
        if ans > E:
            ans = min(ans, E)
            ans_used = []
            for i in used:
                ans_used.append(i)
    if idx == N:
        return
    used.append(idx+1)
    recur(idx+1, A+arr[idx][0], B+arr[idx][1], C+arr[idx][2], D+arr[idx][3], E+arr[idx][4])
    used.pop()
    recur(idx+1, A, B, C, D, E)

N = int(input())
a, b, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 2147000000
used = []
ans_used = []
recur(0, 0, 0, 0, 0, 0)
ans_used.sort()
if ans_used:
    print(ans)
    print(*ans_used)
else:
    print(-1)

# 2
# 0 0 0 10
# 0 0 0 10 1
# 0 0 0 5 0