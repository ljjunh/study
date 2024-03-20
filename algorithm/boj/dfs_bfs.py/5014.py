from collections import deque
def bfs():
    global F, S, G, U, D
    visited[S] = 1
    q = deque()
    q.append(S)
    while q:
        v = q.popleft()
        if v == G:
            print(visited[v]-1)
            return
        for i in (v+U, v-D):
            if 1 <= i <= F and not visited[i]:
                visited[i] = visited[v] + 1
                q.append(i)
    print("use the stairs")
    return
    
F, S, G, U, D = map(int, input().split())
visited = [0] * (F+1)
bfs()