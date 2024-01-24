import sys
input = sys.stdin.readline
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)] #2차원배열 입력받기
largest = -2147000000
for i in range(n):
    sum1 = sum2 = 0 
    for j in range(n):
        sum1 += a[i][j] # 행의 합
        sum2 += a[j][i] # 열의 합
    if sum1 > largest:
        largest = sum1
    if sum2 > largest:
        largest = sum2

#대각선의 최대합
sum1 = sum2 = 0
for i in range(n):
    sum1 += a[i][i]
    sum2 += a[i][n-i-1]
if sum1 > largest:
    largest = sum1
if sum2> largest:
    largest = sum2
print(largest)