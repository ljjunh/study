T = 10
for tc in range(1, T + 1):
    int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    lt = 0
    rt = 0
    for i in range(100):
        for j in range(100):
            if arr[i][j] == 2:
                lt = i
                rt = j
    d = 0
    while lt > 0:  # 맨 위에 도달할 때까지 반복
        if rt - 1 >= 0 and arr[lt][rt - 1] == 1 and d != 2:  # 왼쪽으로 이동 가능하면, 왔던곳 다시 못가게 d != 2
            rt -= 1
            d = 1  # 왼쪽으로 이동
        elif rt + 1 < 100 and arr[lt][rt + 1] == 1 and d != 1:  # 오른쪽으로 이동 가능하면, 왔던곳 다시 못가게 d != 1
            rt += 1
            d = 2  # 오른쪽으로 이동
        else:  # 위로 이동
            lt -= 1
            d = 0  # 위로 이동
    print(f"#{tc} {rt}")
        