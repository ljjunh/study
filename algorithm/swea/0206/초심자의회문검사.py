T = int(input())
for tc in range(1, T + 1):
    cnt = 0
    arr = list(input())
    for i in range(len(arr)//2):
        if arr[i] != arr[-i-1]:
            cnt += 1
    if cnt != 0:
        print(f"#{tc} 0")
    else:
        print(f"#{tc} 1")