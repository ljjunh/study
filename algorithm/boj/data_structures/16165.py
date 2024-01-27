import sys
input = sys.stdin.readline
n, m = map(int, input().split())
dict = {}
for i in range(n):
    temp1 = input().rstrip()
    temp2 = int(input())
    temp3 = []
    for j in range(temp2):
        temp3.append(input().rstrip())
    dict[temp1] = temp3
for j in range(m):
    temp4 = input().rstrip()
    temp5 = int(input())
    if temp5 == 0:
        print(*sorted(dict[temp4]), sep = "\n")
    elif temp5 == 1:
        for k, v in dict.items():
            if temp4 in dict[k]:
                print(k)

