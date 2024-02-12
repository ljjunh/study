temp = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
N, B = map(int, input().split())
res = ""
while N > 0:
    res = temp[N % B] + res
    N = N // B
print(res)