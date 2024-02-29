def func():
    sold_bread = 0
    for i in arr:
        made_bread = (i // M) * K
        sold_bread += 1
        remain = made_bread - sold_bread
        if remain < 0:
            return "Impossible"
    return "Possible"

T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    print(f"#{tc} {func()}")