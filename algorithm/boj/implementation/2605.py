N = int(input())
arr = list(map(int, input().split()))
ans = []
for i in range(N):
    ans.insert(len(ans) - arr[i], i+1)
print(*ans)