def recur(n, lst, s):
    if n == M:
        print(*lst)
        return
    prev = 0
    for i in range(s, N):
        if prev != arr[i]:
            prev = arr[i]
            recur(n + 1, lst + [arr[i]], i)

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
recur(0, [], 0)
