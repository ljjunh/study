import sys
import pprint
input = sys.stdin.readline
n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
#행 최댓값
max_row = 0
for i in range(n):
    row_sum = 0
    for j in range(n):
        row_sum += arr[i][j]
    if max_row < row_sum:
        max_row = row_sum

#열 최댓값
max_column = 0
for i in range(n):
    column_sum = 0
    for j in range(n):
        column_sum += arr[j][i]
    if max_column < column_sum:
        max_column = column_sum

# \대각선
max_diagonal = 0
for i in range(n):
    max_diagonal += arr[i][i]

# /대각선
max_diagonal2 = 0
j = n -1
for i in range(n):
    max_diagonal2 += arr[i][j]
    j -= 1
print(max(max_row, max_column, max_diagonal, max_diagonal2))