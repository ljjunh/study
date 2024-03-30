import sys
input = sys.stdin.readline

def recur(n, sm, add, sub, mul, div):
    global max_num, min_num
    if n == N:
        max_num = max(max_num, sm)
        min_num = min(min_num, sm)
        return
    if add > 0:
        recur(n+1, sm+arr[n], add-1, sub, mul, div)
    if sub > 0:
        recur(n+1, sm-arr[n], add, sub-1, mul, div)
    if mul > 0:
        recur(n+1, sm * arr[n], add, sub, mul-1, div)
    if div > 0:
        recur(n+1, int(sm/arr[n]), add, sub, mul, div-1)
    

N = int(input())
arr = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())
max_num = -2147000000
min_num = 2147000000
recur(1, arr[0], add, sub, mul, div)
print(max_num, min_num, sep="\n")