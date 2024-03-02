x, y = map(int, input().split())
N = int(input())
arr = [[0] * x for _ in range(y)]
lst1 = [0, y]
lst2 = [0, x]
for _ in range(N):
    a, b = map(int, input().split())
    if a == 0:
        lst1.append(b)
    else:
        lst2.append(b)
lst1.sort()
lst2.sort()
max1 = 0
max2 = 0
for i in range(1, len(lst1)):
    max1 = max(max1, lst1[i] - lst1[i-1])
for i in range(1, len(lst2)):
    max2 = max(max2, lst2[i] - lst2[i-1])
print(max1 * max2)