import sys
input = sys.stdin.readline
arr = [list(map(int, input().split())) for _ in range(7)]
cnt = 0
for i in range(7):
    start = 0
    end = 4
    for j in range(7):
        if len(arr) == end:
            continue
        if arr[i][start] == arr[i][end] and arr[i][start+1] == arr[i][end-1]:
            cnt += 1
            start += 1
            end += 1
        else:
            start += 1
            end += 1
for i in range(7):
    start = 0
    end = 4
    for j in range(7):
        if len(arr) == end:
            continue
        if arr[start][i] == arr[end][i] and arr[start+1][i] == arr[end-1][i]:
            cnt += 1
            start += 1
            end += 1
        else:
            start += 1
            end += 1
print(cnt)
