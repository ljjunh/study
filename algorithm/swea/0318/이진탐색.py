def binarySearch(s, e, target, chk):
    global ans
    if s > e:
        return
    mid = (s + e) // 2
    if A[mid] == target:
        ans += 1
        return
    elif A[mid] < target:
        if chk == 1:
            return
        return binarySearch(mid + 1, e, target, 1)
    else:
        if chk == 2:
            return
        return binarySearch(s, mid - 1, target, 2)

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = sorted(list(map(int, input().split())))
    ans = 0
    for i in B:
        binarySearch(0, N-1, i, 0)
    print(f"#{tc} {ans}")