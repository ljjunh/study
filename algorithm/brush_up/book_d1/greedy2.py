n, m, k = map(int, input().split())
num = sorted(list(map(int, input().split())))
first = num[n - 1]
second = num[n - 2]
#n 전체횟수 m 총더할횟수 k최대반복
count = 0
count += int(m / (k + 1)) * k
count += m % (k + 1)
result = 0
result += count * first
result += (m - count) * second
print(result)
