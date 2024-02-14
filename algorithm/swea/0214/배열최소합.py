def backtracking(r, n, now_sum, v):
    global min_sum
    if r == n:
        if now_sum < min_sum:
            min_sum = now_sum
    elif now_sum > min_sum: 
        return
    else: 
        for i in range(n): 
            if not v[i]: # 방문안했으면 
                v[i] = 1 # 방문처리
                backtracking(r+1, n, now_sum + arr[r][i], v)
                v[i] = 0 # 초기화
                
T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    v = [0] * n
    min_sum = 2147000000
    
    #함수호출
    backtracking(0, n, 0, v)
    print(f'#{tc} {min_sum}')