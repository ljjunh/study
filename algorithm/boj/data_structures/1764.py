import sys
input = sys.stdin.readline
n, m = map(int, input().split())
# 1. 딕셔너리 사용
# dict = {}
# for _ in range(n+m):
#     name = input().rstrip()
#     if name in dict:
#         dict[name] += 1
#     else:
#         dict[name] = 1
# res = sorted(dict.items())
# cnt = 0
# for i in res:
#     if i[1] > 1:
#         cnt += 1
# print(cnt)
# for i in res:
#     if i[1] > 1:
#         print(i[0])

# 2. 집합 사용
a = set()
b = set()
for _ in range(n):
    name = input().rstrip()
    a.add(name)
for _ in range(m):
    name = input().rstrip()
    b.add(name)
res = sorted(list(a & b))
print(len(res), *res, sep = "\n")