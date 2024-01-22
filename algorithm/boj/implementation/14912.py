n, k = map(int,input().split())
cnt = 0
for i in range(1, n+1):
    for j in str(i):
        if int(j) == k:
            cnt += 1
print(cnt)


# for i in range(1, n+1):
#     if str(k) in str(i):
#         cnt += str(i).count(str(k))
# print(cnt) 