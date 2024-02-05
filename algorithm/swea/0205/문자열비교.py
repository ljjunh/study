T = int(input())
for tc in range(1, T + 1):
    arr1 = input()
    arr2 = input()
    
    lt = 0
    rt = len(arr1) -1
    res = 0
    while rt < len(arr2):
        if arr2[lt:rt+1] == arr1:
            res += 1
            break
        elif arr2[lt:rt+1] != arr2:
            lt += 1
            rt += 1
    print(f"#{tc} {res}")
    