import sys
input = sys.stdin.readline
n = int(input())
res = []
for _ in range(n):
    res.append(list(map(int, input().split())))
temp = 0
for i in res:
    for j in i:
        temp += j

sum = 0
for i in range(n):
    if i == len(res) // 2:
        pass
    elif i % 2 == 1:
        sum += res[i][0] + res[i][-1] 
    else:
        sum += (res[i][0] + res[i][-1] + res[i][1] + res[i][-2])
print(temp - sum)