T = int(input())
for tc in range(1, T + 1):
    arr = [[""] * 15 for _ in range(15)]
    
    for i in range(5):
        s = input().rstrip()
        for j in range(15):
            if j <= len(s) - 1:
                arr[i][j] = s[j]
    print(f"#{tc} ", end = "")
    for i in range(15):
        for j in range(15):
            if arr[j][i] != "":
                print(arr[j][i], end = "")
    print()