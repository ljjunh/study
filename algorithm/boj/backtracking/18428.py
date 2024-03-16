import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 * 6)

def recur(use):
    global ans
    if use == 3:
        if dfs():
            ans = True
            return
    else:
        for i in range(N):
            for j in range(N):
                if graph[i][j] == "X":
                    graph[i][j] = "O"
                    recur(use + 1)
                    graph[i][j] = "X"


def dfs():
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for t in teacher:
        for k in range(4):
            nx, ny = t
            while 0 <= nx < N and 0 <= ny < N:
                if graph[nx][ny] == "O":
                    break
                if graph[nx][ny] == "S":
                    return False
                nx += dx[k]
                ny += dy[k]
    return True


N = int(input())
graph = []
teacher = []
ans = False
for i in range(N):
    graph.append(list(map(str, input().split())))
    for j in range(N):
        if graph[i][j] == "T":
            teacher.append([i, j])
recur(0)
if ans:
    print("YES")
else:
    print("NO")


    