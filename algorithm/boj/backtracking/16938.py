import sys
input = sys.stdin.readline
# 2문제 이상의 부분집합
# 난이도 합은 L <= 난이도합 <= R
# 어려운문제, 쉬운문체 차이 >= X
def recur(n, lst, use):
    global ans
    if n == N:
        if use >= 2:
            lst.sort()
            if L <= sum(lst) <= R and abs(lst[0]-lst[-1]) >= X:
                ans += 1
        return
    recur(n+1, lst+[arr[n]],use+1)
    recur(n+1, lst, use)
N, L, R, X = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0
recur(0, [], 0)
print(ans)