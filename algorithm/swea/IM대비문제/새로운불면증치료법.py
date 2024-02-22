T = int(input())
for tc in range(1, T + 1):
    n = input()
    n_set = set(map(int, n))
    op = 2
    cnt = 1
    while n_set != {0,1,2,3,4,5,6,7,8,9}:
        temp = int(n) * op
        op += 1
        cnt += 1
        for i in str(temp):
            n_set.add(int(i))
    print(f"#{tc} {int(n) * cnt}")