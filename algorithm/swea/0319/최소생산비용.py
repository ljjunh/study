def recur(n, sm):
    global ans
    if n == N:
        ans = min(ans, sm)
        return
    # 생산비용이 이전 최소값보다 커지면 리턴
    if sm > ans:
        return
    
    for i in range(N):
        if visited[i]:
            continue
        visited[i] = 1
        recur(n+1, sm + arr[n][i]) # 한줄에 하나씩 고르기
        visited[i] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 2147000000
    visited = [0] * N
    recur(0, 0)
    print(f"#{tc} {ans}")