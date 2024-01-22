import sys
input = sys.stdin.readline
n = int(input())
a = [int(input()) for i in range(n)]
a.sort()
print(*a, sep = "\n")