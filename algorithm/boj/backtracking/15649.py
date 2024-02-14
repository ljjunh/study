import sys
input = sys.stdin.readline

def dfs(n, lst):
    if n == M: # M개의 수열을 완성하면
        ans.append(lst) # 정답 리스트에 수열을 추가
        return
    for i in range(1, N + 1):
        if v[i] == 0: # 방문하지 않은 숫자인 경우
            v[i] = 1 # 재방문 막기 위해서 1을 넣어놓으면 
            dfs(n + 1, lst + [i]) # 여기서 n+1로 재귀호출을 했을때도 전꺼는 1이여서 다음으로 넘어감
            v[i] = 0


N, M = map(int, input().split())
ans = []
v = [0] * (N + 1)
dfs(0, [])
for i in ans:
    print(*i)