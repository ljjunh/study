import pprint
N = 5

# 행번호 r
# 열번호 c
arr = [[N *r+c for c in range(N)] for r in range(N)]

# 대각선 좌표 힌트
# 행번호 == 열번호 : 오른쪽 아래 대각선
# 열번호 == 인덱스 최대값 - 행번호 : 왼쪽 아래 대각선

sum1 = 0 # 왼쪽 대각선
sum2 = 0 # 오른쪽 대각선
for i in range(N):
    sum1 += arr[i][i]
    if N // 2 == i:
        continue
    sum2 += arr[i][N-i-1]
dia_sum = sum1 + sum2
print(dia_sum)