temp = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
N, B = input().split()
N = N[::-1]
B = int(B)
answer = 0
for i in range(len(N)):
    answer += (B ** i) * (temp.index(N[i]))
print(answer)