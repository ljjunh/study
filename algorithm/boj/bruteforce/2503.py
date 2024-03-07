import sys

input = sys.stdin.readline
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0
for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            if a == b or b == c or c == a:
                continue
            cnt = 0
            for i in arr:
                num = i[0]
                strike = i[1]
                ball = i[2]
                strike_cnt = 0
                ball_cnt = 0
                if a == num // 100:
                    strike_cnt += 1
                elif b == num // 100 or c == num // 100:
                    ball_cnt += 1
                if b == (num // 10) - (num // 100) * 10:
                    strike_cnt += 1
                elif (
                    a == (num // 10) - (num // 100) * 10
                    or c == (num // 10) - (num // 100) * 10
                ):
                    ball_cnt += 1
                if c == num % 10:
                    strike_cnt += 1
                elif a == num % 10 or b == num % 10:
                    ball_cnt += 1
                if strike_cnt == strike and ball_cnt == ball:
                    cnt += 1
            if cnt == N:
                ans += 1
print(ans)
