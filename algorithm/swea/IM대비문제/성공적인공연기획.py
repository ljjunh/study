T = int(input())
for tc in range(1, T + 1):
    arr = list(map(int, input()))
    clap = 0
    cnt = 0
    for i in range(len(arr)):
        if clap < i:
            cnt += 1
            clap += 1
        if arr[i] != 0:
            clap += arr[i]
    print(f"#{tc} {cnt}")
        
