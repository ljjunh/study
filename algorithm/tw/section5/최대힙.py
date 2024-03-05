import heapq
heap = []
while True:
    s = int(input())
    if s == 0:
        print(-heapq.heappop(heap))
    elif s == -1:
        exit()
    else:
        heapq.heappush(heap, -s)
