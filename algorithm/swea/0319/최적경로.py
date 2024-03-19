def recur(n, lst, sm):
    global ans
    # 최단경로니까 거리 합이 기존 ans보다 커지면 패스
    if sm >= ans:
        return
    
    if n == N:
        # 전부 돌고 나면 마지막고객과 집의 거리 더해주기
        sm += abs(lst[-1][0] - home[0]) + abs(lst[-1][1] - home[1])  
        ans = min(ans, sm)
        return
    
    for i in range(N):
        if visited[i]:
            continue
        visited[i] = 1  # 재방문 막기
        recur(
            n + 1, # 선택한 개수 
            lst + [arr[i]], # 거리 계산을 위해 누적
            sm + abs(lst[-1][0] - arr[i][0]) + abs(lst[-1][1] - arr[i][1]), # 거리 누적
        )
        visited[i] = 0  # 재귀 끝나고 나오면 다시 초기화


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    temp = list(map(int, input().split()))
    company = (temp[0], temp[1])
    home = (temp[2], temp[3])
    arr = []
    visited = [0] * N
    ans = 2147000000
    for i in range(4, N * 2 + 4, 2):
        arr.append((temp[i], temp[i + 1]))  # 회사랑 집 빼고 고개만 입력받기
    recur(0, [company], 0)
    print(f"#{tc} {ans}")
