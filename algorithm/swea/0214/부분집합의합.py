def dfs(n, sm, cnt):
    global ans
    # 가지치기 : 가능한 모든 경우 처리하고 정답이 나오면, 가장 마지막에 고민
    if sm > K: # 이미 초과
        return
    # 종료조건
    if n == N:
        if sm == K and cnt == CNT:
            ans += 1
        return
    
    # 사용하는 경우
    dfs(n + 1, sm + lst[n], cnt + 1)
    # 사용하지 않는 경우
    dfs(n + 1, sm, cnt)
    
T = int(input())
for tc in range(1, T + 1):
    CNT, K = map(int, input().split())
    lst = [n for n in range(1, 13)]
    N = 12
    ans = 0
    dfs(0, 0, 0)
    print(f"#{tc} {ans}")