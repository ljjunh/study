def func(y):
    cnt = 0
    is_red = False
    for i in range(N):
        #1. red자성체 발견
        if arr[i][y] == 1:
            is_red = True
        # 2. 이전에 red자성체를 발견했고, 현재 blue 자성체를 발견하면 cnt += 1
        elif is_red and arr[i][y] == 2:
            cnt += 1
            is_red = False
    return cnt


for tc in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        ans += func(i)
    print(f"#{tc} {ans}")