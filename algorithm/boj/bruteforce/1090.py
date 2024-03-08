# 어차피 모일때 최단거리는 x,y조합중에 하나임
N = int(input())
arr = []
arr_x = []
arr_y = []
ans = [-1] * N
# 입력받기
for _ in range(N):
    x, y = map(int ,input().split())
    arr_x.append(x)
    arr_y.append(y)
    arr.append((x,y))
    
for x in arr_x:
    for y in arr_y:
        temp = []
        for dx, dy in arr:
            temp.append(abs(dx-x) + abs(dy-y))
        temp.sort()

        cnt = 0
        for i in range(len(temp)):
            cnt += temp[i]
            if ans[i] == -1:
                ans[i] = cnt
            else:
                ans[i] = min(ans[i], cnt)
print(*ans)

