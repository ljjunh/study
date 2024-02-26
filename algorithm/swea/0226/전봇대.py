for tc in range(1, int(input())+1):
    N = int(input())
    arr = []
    cnt = 0
    for i in range(N):
        a, b = map(int, input().split())
        arr.append((a, b))
    arr.sort(key = lambda x : x[0], reverse = True )
     
    for i in range(N-1):
        for j in range(i+1, N):
            if arr[i][1] < arr[j][1]:
                cnt += 1
    print(f'#{tc}', cnt)