T = int(input())
for tc in range(1, T + 1):
    og = list(map(int, input()))
    k = 0
    cnt = 0
    temp = len(og)
    arr = [0] * temp

    while og != arr:
        if arr[k] != og[k]:
            cnt += 1
            for i in range(k,temp):
                arr[i] = 1 if arr[i] == 0 else 0
        k += 1
    
    print(f"#{tc} {cnt}")