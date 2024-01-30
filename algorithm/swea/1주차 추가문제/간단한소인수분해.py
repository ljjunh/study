T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    arr = [2, 3, 5, 7, 11]
    arr2 = [0] * 5
    i = 0
    while n > 1:
        if n % arr[i] == 0:
            n = n / arr[i]
            arr2[i] += 1
        else:
            i += 1
    a, b, c, d, e = arr2
    print(f"#{tc}", a, b, c, d, e)        
