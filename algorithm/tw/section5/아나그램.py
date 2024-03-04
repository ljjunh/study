A = input()
B = input()
dict = dict()
for i in A:
    dict[i] = dict.get(i, 0) + 1
for i in B:
    dict[i] = dict.get(i, 0) - 1
for i in A:
    if dict.get(i) != 0:
        print("NO")
        break
else:
    print("YES")
    