import sys
input = sys.stdin.readline
n = int(input())
for i in range(n):
    arr = input().rstrip()
    cnt = 0
    for j in arr:
        if j == "(":
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0: # 0보다 작을경우에는 (가 없을때 )가 들어오는경우
            break
    if cnt == 0: # 0이면 VPS니까 YES
        print("YES")
    else: # 0보다 크면 (가 덜 닫힌거니까 NO, 0보다 작으면 (가 없을때 )가 들어온거
        print("NO")