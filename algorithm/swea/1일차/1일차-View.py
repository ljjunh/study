T = 10
for i in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    for j in range(2, n - 2):
        temp = arr[j] - max(arr[j - 2 : j] + arr[j + 1 :  j + 3]) #j에서 양쪽2개의 최대값 빼줌
        if temp > 0: # temp가 음수가 아닌 양수인경우, 양쪽2개씩보다 큰거임
            cnt += temp
    print(f"#{i + 1} {cnt}")
