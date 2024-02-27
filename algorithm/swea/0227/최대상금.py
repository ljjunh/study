def dfs(n):
    global ans
    if n == M:
        ans = max(ans, int("".join(map(str,arr))))
        return

    for i in range(len_arr - 1):
        for j in range(i+1, len_arr):
            arr[i], arr[j] = arr[j], arr[i]
            chk = int("".join(map(str,arr)))
            if (n, chk) not in visited:
                dfs(n+1)
                visited.append((n, chk))
            arr[i], arr[j] = arr[j], arr[i] 

T = int(input())
for tc in range(1, T + 1):
    N, M = input().split()
    M = int(M)
    arr = []
    for i in N:
        arr.append(int(i))
    len_arr = len(arr)
    ans = 0
    visited = []
    dfs(0)
    print(f'#{tc} {ans}')