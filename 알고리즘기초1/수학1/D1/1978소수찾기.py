def ss(a):
    if a < 2:
        return False
    for i in range(2, int(a**0.5)+1):
        if a % i == 0:
            return False
    return True
n = int(input())
arr = list(map(int, input().split()))
cnt = 0
for i in arr:
    if ss(i) == True:
        cnt += 1
print(cnt)