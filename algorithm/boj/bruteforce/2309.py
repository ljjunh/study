arr = [int(input()) for _ in range(9)]
sum_arr = sum(arr)
arr.sort()
for i in range(8):
    for j in range(i+1, 9):
        if arr[i] + arr[j] == sum_arr - 100:
            for k in range(9):
                if i == k or j == k:
                    continue
                print(arr[k])
            exit()