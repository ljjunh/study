N = input() # 목표채널
M = int(input()) # 고장난 버튼 수
if M == 0:
    if N == "100":
        print(0)
        exit()
    print(len(N))
    exit()
arr = list(map(int, input().split())) # 고장난 버튼
if N == "100":
    print(0)
    exit()
now = 100 # 현재 채널
possible = [1] * 10
for i in arr:
    possible[i] = 0
temp = ""
cnt = 0
for i in N:
    # in N으로 하면 안됨 목표채널 1일때; index로 해야함
    if possible[int(i)]:
        temp += i
        cnt += 1
    elif int(i) <= 4:
        j = 1
        while True:
            if 0 <= (int(i) - j):
                break
            if possible[int(i) - j]:
                temp += str(possible[int(i) - j])
                cnt += 1
                break
            else:
                j += 1
    elif i >= 5:
        k = 1
        while True:
            if (int(i) + k) > 9:
                break
            if possible[int(i) + k]:
                temp += str(possible[int(i) + k])
                cnt += 1
                break
            else:
                k += 1
start = int(temp)
while start != int(N):
    if start < int(N):
        start += 1
        cnt += 1
    elif start > int(N):
        start -= 1
        cnt += 1
print(cnt)
    