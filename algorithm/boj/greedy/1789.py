n = int(input())
total = 0
cnt = 0
while True:
    cnt += 1
    total += cnt
    if total > n:
        break
print(cnt - 1)