import sys

input = sys.stdin.readline
sys.setrecursionlimit(1000000)


def checker(idx, num):
    _num = arr[idx][0]
    _strike = arr[idx][1]
    _ball = arr[idx][2]

    strike = 0
    ball = 0

    _A = _num // 100
    _B = (_num - (_A * 100)) // 10
    _C = _num % 10

    A = num // 100
    B = (num - (A * 100)) // 10
    C = num % 10

    if A == 0 or B == 0 or C == 0:
        return False

    if A == B or A == C or B == C:
        return False

    if A == _A:
        strike += 1
    if B == _B:
        strike += 1
    if C == _C:
        strike += 1

    if A == _B or A == _C:
        ball += 1
    if B == _A or B == _C:
        ball += 1
    if C == _A or C == _B:
        ball += 1

    if strike == _strike and ball == _ball:
        return True
    return False


def recur(idx, num):
    global ans

    if idx == n:
        ans += 1

        recur(0, num + 1)
        return

    if num == 1000:
        return

    if checker(idx, num):
        recur(idx + 1, num)
    else:
        recur(0, num + 1)


input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
ans = 0
recur(0, 100)
print(ans)
