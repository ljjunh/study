import heapq

def prim(s):
    heap = []
    # 연결되어있는지 확인
    MST = [0] * V
    ans = 0
    heapq.heappush(heap, (0, s))
    while heap:
        w, n = heapq.heappop(heap)
        if MST[n]:
            continue
        MST[n] = 1
        ans += w
        for i in range(V):
            if not graph[n][i] or MST[i]:
                continue
            heapq.heappush(heap, (graph[n][i], i))
    print(f"#{tc} {ans}")

T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    V = V + 1
    graph = [[0] * V for _ in range(V)]
    for i in range(E):
        s, e, w = map(int, input().split())
        graph[s][e] = w
        graph[e][s] = w
    prim(0)