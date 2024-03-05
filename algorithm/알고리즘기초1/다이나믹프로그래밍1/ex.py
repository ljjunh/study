import sys
imput = sys.stdin.readline
n = int(input())
D = [-1] * (n+1) # n+ 1의 개수만큼
D[0] = 0
D[1] = 1 # 바텀업 이니까 미리 초기화
for i in range(2, n+1):# 1까지는 이미 초기화했으니까 2부터
    D[i] = D[i-2] + D[i-1]
print(D[n])