def binary_search(start, end, target):
    cnt = 0
    while start <= end:
        mid = int((start + end)/2)
        if mid == target:
            return cnt
        elif mid > target:
            cnt += 1
            end = mid
        else:
            cnt += 1
            start = mid


T = int(input())
for tc in range(1, T + 1):
    end, a, b = map(int, input().split())
    cnt = 0
    temp1 = binary_search(1, end, a)
    temp2 = binary_search(1, end, b)
    if temp1 == temp2:
        print(f"#{tc} 0")
    elif temp1 < temp2:
        print(f"#{tc} A")
    else:
        print(f"#{tc} B")