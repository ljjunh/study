import sys
import heapq
input = sys.stdin.readline
N = int(input())
heap = []
for i in range(N):
    s = int(input())
    if s == 0:
        if not heap:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, (abs(s), s))
        
