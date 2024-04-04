from collections import deque

def bfs():
    global F, S, G, U, D
    visited = [0] * (F+1)
    visited[S] = 1
    q = deque()
    q.append(S)
    while q:
        v = q.popleft()
        if v == G: # 큐에서 뺀 값이 도착지점이면
            return visited[v]-1 # 시작층에서 1로 시작했으니까 -1

        for i in (v+U, v-D): # 올라가거나 내려간 층
            if 0 < i <= F and not visited[i]: # 범위 안넘고 방문한적 없으면
                q.append(i)
                visited[i] = visited[v] + 1
    return "use the stairs"
        

F, S, G, U, D = map(int, input().split())
print(bfs())