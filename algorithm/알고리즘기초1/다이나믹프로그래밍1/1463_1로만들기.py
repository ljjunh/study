n = int(input())
d = [0] * (n + 1)
d[1] = 0 # 초기값 설정
for i in range(2, n + 1): # 1은 초기화해줬으니까 2부터 시작
    d[i] = d[i-1] + 1
    if i % 3 == 0:
        d[i] = min(d[i//3] + 1, d[i])
    if i % 2 == 0:
        d[i] == min(d[i//2] + 1, d[i])
print(d[n])