T = int(input())
for i in range(T):
    a, b = map(int, input().split())
    t1, t2 = a, b
    while a % b != 0:
        a, b = b, a % b
    print(t1 * t2 // b)