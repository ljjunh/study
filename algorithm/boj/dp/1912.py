n = int(input())
arr = list(map(int, input().split()))

prefix = [-1001] * (n+1)
for i in range(n):
    prefix[i+1] = max(arr[i], prefix[i] + arr[i])
print(max(prefix))