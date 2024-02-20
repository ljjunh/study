def in_order(T):
    if T:
        in_order(left[T])
        arr.append(T)
        in_order(right[T])

for tc in range(1, 11):
    N = int(input())
    num = [[] for _ in range(N + 1)]
    alpha = [] * (N + 1)
    alpha.append(0)
    left =[0] * (N + 1) 
    right = [0] * (N + 1)
    arr = []

    for i in range(1, N + 1):
        s = list(input().split())
        for j in range(1, len(s)):
            if j == 1:
                alpha.append(s[j])
            else:
                num[int(i)].append(int(s[j]))
    
    for i in range(1, N + 1):
        while num[i]:
            if left[i] == 0:
                left[i] = num[i].pop(0)
            else:
                right[i] = num[i].pop(0)
    in_order(1)
    print(f"#{tc}", end = " ")
    for i in arr:
        print(alpha[i], end = "")
    print()