n = int(input())
m =  int(input())
button = list(map(int, input().split()))
rmc = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "+", "-"]
for i in button:
    rmc.remove(i)