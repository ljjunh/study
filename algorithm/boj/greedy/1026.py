N = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
temp_arr2 = arr2
sum = 0
arr1.sort()
for i in range(N):
    sum += min(arr1) * max(temp_arr2)
    arr1.remove(min(arr1))
    arr2.remove(max(temp_arr2))
print(sum)