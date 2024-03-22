dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T + 1):
    R, C = map(int, input().split())
    arr = [list(input()) for _ in range(R)]
    if "@" not in arr:
        print(f"#{tc} {"NO"}")
        continue
    memory = 0
    x = y = 0
    d = 3 # 기본적으로 오른쪽으로 가게 셋팅
    while True:
        if arr[x][y] == "@":
            print(f"#{tc} {'YES'}")
            break
        # 무한루프 돌때도 NO찍고 끝내줘야됨
        if arr[x][y].isdecimal():
            memory += int(arr[x][y])
        elif arr[x][y] == "+":
            if memory == 15:
                memory = 0
            else:
                memory += 1
        elif arr[x][y] == "-":
            if memory == 0:
                memory = 15
            else:
                memory -= 1
        elif arr[x][y] == "<":
            d = 2
        elif arr[x][y] == ">":
            d = 3
        elif arr[x][y] == "^":
            d = 0
        elif arr[x][y] == "v":
            d = 1
        elif arr[x][y] == "_":
            if memory == 0:
                d = 3
            else:
                d = 2
        elif arr[x][y] == "|":
            if memory == 0:
                d = 1
            else:
                d = 0
        elif arr[x][y] == "?":
            #4방향중 랜덤
            pass
        elif arr[x][y] == ".":
            print(f"#{tc} {'NO'}")
            break
        x += dx[d]
        y += dy[d]
   