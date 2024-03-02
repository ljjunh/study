import sys
input = sys.stdin.readline
arr = [list(map(int, input().split())) for _ in range(5)]
temp = [list(map(int, input().split())) for _ in range(5)]
cnt = 0
for i in range(5):
    for j in range(5):
        cnt += 1
        for k in range(5):
            for l in range(5):
                if arr[k][l] == temp[i][j]:
                    arr[k][l] = 0
                l_dia = 0
                r_dia = 0
                ans = 0
                for m in range(5):
                    if arr[m][m] == 0:
                        l_dia += 1
                    if arr[m][5-m-1] == 0:
                        r_dia += 1
                    if l_dia == 5:
                        ans += 1
                    if r_dia == 5:
                        ans += 1
                    r_cnt = 0
                    c_cnt = 0
                    for n in range(5):
                        if arr[m][n] == 0:
                            r_cnt += 1
                        if arr[n][m] == 0:
                            c_cnt += 1
                        if r_cnt == 5:
                            ans += 1
                        if c_cnt == 5:
                            ans += 1
                        if ans >= 3:
                            print(cnt)
                            exit()
