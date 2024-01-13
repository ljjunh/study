N = int(input())
numbers = []
for _ in range(N):
    temp = int(input())
    if temp == 0:
        numbers.pop()
    else:
        numbers.append(temp)
print(sum(numbers))