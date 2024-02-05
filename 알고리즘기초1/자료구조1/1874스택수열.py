n = int(input())
arr = [int(input()) for _ in range(n)]
print(arr)
nums = list(range(1, n+1))
stack = []
i = 0
operator = ""
while True:
    if arr == stack:
        break
    while True:
            if len(stack) != 0: 
                if arr[0] == stack[-1]:
                    break
            stack.append(nums[0])
            nums.pop(0)
            operator += "+"
    