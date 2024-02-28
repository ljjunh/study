T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [tuple(map(int, input().split())) for _ in range(N)]
    arr.sort(key = lambda x : (x[1], x[0]))
    temp = []
    for i in arr:
        if not temp:
            temp.append(i)
        elif temp[-1][1] <= i[0]:
            temp.append(i)
    print(f"#{tc} {len(temp)}")