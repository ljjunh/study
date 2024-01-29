import sys
input = sys.stdin.readline
arr = [list(map(int, input().split())) for _ in range(9)]
res = 0
for i in range(9):
    cnt1 = [0] * 10
    cnt2 = [0] * 10
    for j in range(9):
        cnt1[arr[i][j]] = 1
        cnt2[arr[j][i]] = 1
    if sum(cnt1) != 9 or sum(cnt2) != 9:
        res += 1
for i in range(3):
    for j in range(3):
        cnt3 = [0] * 10
        for k in range(3):
            for s in range(3):
                cnt3[arr[i*3+k][j*3+s]] = 1
        if sum(cnt3) != 9:
            res += 1
if res > 0:
    print("NO")
elif res == 0:
    print("YES")