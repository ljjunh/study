N, K = map(int, input().split())
arr = list(map(int, input().split()))
prefix = [0] * (N + 1)
ans = []
for i in range(N):
    prefix[i+1] += prefix[i] + arr[i]
for i in range(K, N+1):
    ans.append(prefix[i] - prefix[i-K])
print(max(ans))