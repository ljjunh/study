import sys
input = sys.stdin.readline
from collections import deque
n = int(input())
arr = deque([list(map(int, input().split())) for _ in range(n)])

m = int(input())
#command = [list(map(int, input().split())) for _ in range(m)]

for i in range(m):
    a, b, c = map(int, input().split())
    if b == 0:
       for j in range(c):
           pass