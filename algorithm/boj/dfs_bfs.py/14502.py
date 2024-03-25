from collections import deque
import copy
import sys
input= sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# 백트래킹으로 빈칸0을 1로 3개씩 바꾸면서 3개 바꾸면 bfs로 안전영역 수 구하고 최대값 출력
def bfs():
    global ans
    q = deque()
    tmp = copy.deepcopy(graph) # 원본에 영향 안가게 복사
    for i in range(N):
        for j in range(M):
            if tmp[i][j] == 2:
                q.append((i, j)) # 바이러스 큐에 추가
    while q:
        cx, cy = q.popleft()
        for k in range(4):   
            nx, ny = cx+dx[k], cy+dy[k]
            if 0 <= nx < N and 0 <= ny < M and tmp[nx][ny] == 0:
                q.append((nx, ny)) 
                tmp[nx][ny] = 2 # 바이러스 퍼진곳은 2로 바꾸기
    cnt = 0
    for i in range(N): # 바이러스가 다 퍼지고 나서 안전영역 구하기
        cnt += tmp[i].count(0)
    ans = max(ans, cnt) # 최대 안전영역 구하기



def recur(n):
    if n == 3: # 벽으로 3개 바꾸면 bfs호출
        bfs()
        return
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0: # 0(빈칸)인 경우
                graph[i][j] = 1 # 1(벽)으로 바꾸고
                recur(n+1) # 재귀호출
                graph[i][j] = 0 # 다끝나면 다시 0으로

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
ans = 0
recur(0)
print(ans)