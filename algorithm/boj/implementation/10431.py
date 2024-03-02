P = int(input())
for _ in range(P):
    arr = list(map(int, input().split()))
    cnt = 0
    temp = []
    for i in range(1, 21):
        temp.append(arr[i])
        for j in temp:
            if arr[i] < j:
                cnt += 1
    print(arr[0], cnt)
