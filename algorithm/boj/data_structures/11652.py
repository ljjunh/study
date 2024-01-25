import sys
input = sys.stdin.readline
n = int(input())
dict = {}
for i in range(n):
    temp = int(input())
    if temp in dict:
        dict[temp] += 1
    else:
        dict[temp] = 1
res = sorted(dict.items(), key = lambda x: (-x[1], x[0]))
print(res[0][0])