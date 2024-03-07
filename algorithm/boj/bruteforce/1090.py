N = int(input())
arr = []
arr_x = []
arr_y = []
ans = [-1] * N
for _ in range(N):
    x, y = map(int, input().split())
    arr_x.append(x)
    arr_y.append(y)
    arr.append([x, y])

for i in arr_x:
    for j in arr_y:
        temp = []
        for dx, dy in arr:
            temp.append(abs(dx-i) + abs(dy-j))
        temp.sort()
        cnt = 0
        for k in range(len(temp)):
            cnt += temp[k]
            if ans[k] == -1:
                ans[k] = cnt
            else:
                ans[k] = min(ans[k], cnt)
print(*ans)
