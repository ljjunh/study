T = int(input())
for tc in range(1, T + 1):
    H, W = map(int, input().split())
    arr = [list(input()) for _ in range(H)]
    N = int(input())
    order = input()

    directions = ["^", "v", "<", ">"]
    di = None
    tank_row = tank_col = -1
    for i in range(H):
        for j in range(W):
            if arr[i][j] in directions:
                di = arr[i][j]
                tank_row, tank_col = i, j
                break
        if di:
            break

    for i in order:
        if i == "U":
            di = "^"
            if tank_row - 1 >= 0 and arr[tank_row - 1][tank_col] == ".":
                arr[tank_row][tank_col], arr[tank_row - 1][tank_col] = ".", "^"
                tank_row -= 1

        elif i == "D":
            di = "v"
            if tank_row + 1 < H and arr[tank_row + 1][tank_col] == ".":
                arr[tank_row][tank_col], arr[tank_row + 1][tank_col] = ".", "v"
                tank_row += 1


        elif i == "L":
            di = "<"
            if tank_col - 1 >= 0 and arr[tank_row][tank_col - 1] == ".":
                arr[tank_row][tank_col], arr[tank_row][tank_col - 1] = ".", "<"
                tank_col -= 1

        elif i == "R":
            di = ">"
            if tank_col + 1 < W and arr[tank_row][tank_col + 1] == ".":
                arr[tank_row][tank_col], arr[tank_row][tank_col + 1] = ".", ">"
                tank_col += 1

        elif i == "S":
            temp_row, temp_col = tank_row, tank_col
            while True:
                if di == "^":
                    temp_row -= 1
                elif di == "v":
                    temp_row += 1
                elif di == "<":
                    temp_col -= 1
                elif di == ">":
                    temp_col += 1

                if temp_row < 0 or temp_row >= H or temp_col < 0 or temp_col >= W:
                    break

                if arr[temp_row][temp_col] == "#":
                    break
                elif arr[temp_row][temp_col] == "*":
                    arr[temp_row][temp_col] = "."
                    break

    print(f"#{tc}", end=" ")
    for k in arr:
        print(*k, sep="")