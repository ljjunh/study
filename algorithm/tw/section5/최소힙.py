import heapq
heap = []
while True:
    t = int(input())
    if t == 0:
        print(heapq.heappop(heap))
    elif t == -1:
        exit()
    else:
        heapq.heappush(heap, t)
        