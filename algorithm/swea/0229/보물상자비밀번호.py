T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    q = list(input())
    arr = []
    # 모든 수 중 K번째로 큰수를 10진수로 만든 수
    # 지금 그냥 3개씩 넣고있음 N//4개만큼 넣어야함
    for i in range(0, N, N // 4):
        arr.append(q[i:i+N//4])
    for i in range(N//4):
        q.append(q.pop(0))
        for j in range(0, N, N // 4):
            arr.append(q[j:j+N//4])
    res = set()
    for i in arr:
        temp = ""
        for j in i:
            temp += j
        res.add(temp)
    ans = []
    for i in res:
        ans.append(i)
    ans.sort(reverse=True)
    print(f"#{tc} {int(ans[K-1], 16)}")
    