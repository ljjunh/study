import collections
import sys
input = sys.stdin.readline
n = int(input())
arr = sorted([int(input()) for i in range(n)])
# 평균값
print(round(sum(arr) / len(arr)))
# 중앙값
print(arr[len(arr)//2])
# 최빈값
temp = dict(collections.Counter(arr))
temp2 = sorted(temp.items(), key=lambda x : -x[1])
if len(temp2) == 1:
    print(temp2[0][0])
elif temp2[0][1] == temp2[1][1]:
    print(temp2[1][0])
else:
    print(temp2[0][0])
# 범위
print(abs(max(arr)- min(arr)))