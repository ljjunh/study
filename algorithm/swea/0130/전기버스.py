T = int(input())
for i in range(1, T + 1):
    k, n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    now = 0 # 현재위치
    cnt = 0 

    # 종점 도착할때까지 반복
    while now + k < n:
        # k범위 안에서 현재위치 조정하면서 이동
        for j in range(k, 0, -1):
            # 가다가 충전소 만나면 
            if(now + j) in arr:
                now += j
                cnt += 1
                break
        else: # 끝까지 갈 수 없을 경우
            cnt = 0
            break
    print(f"#{i} {cnt}")