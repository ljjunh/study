result = [0] * 26
for i in input():
    result[ord(i)-97] += 1
print(*result)
