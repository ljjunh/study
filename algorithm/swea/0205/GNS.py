nums = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
T = int(input())
for tc in range(1, T + 1):
    n, m = input().split()
    arr = list(input().split())
    temp = []
    for i in range(int(m)):
        temp.append(nums.index(arr[i]))
    temp.sort()
    print(n)
    for i in temp:
        print(nums[i], end = " ")
