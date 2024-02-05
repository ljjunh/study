import sys
from collections import deque
input = sys.stdin.readline
left = deque(list(input().rstrip())) 
right = deque()
n = int(input()) 
for i in range(n):
    order = list(input().rstrip().split()) 
    if order[0] == "L" and len(left) != 0:
        right.appendleft(left.pop())
    if order[0] == "D" and len(right) != 0:
        left.append(right.popleft())
    if order[0] == "B" and len(left) != 0:
        left.pop()
    if order[0] == "P":
        left.append(order[1])
print(*left,*right, sep = "")