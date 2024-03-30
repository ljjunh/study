from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def cal(x, y, d):
    global cnt
    while True:
        graph[x][y] = 2 #청소한거 2로 표시
        cnt += 1 
        state = True
        while state:
            for k in ((d+3)%4, (d+2)%4, (d+1)%4, d):
                # 해당 방향의 왼쪽부터 4방향 탐색
                nx, ny = x+dx[k], y + dy[k]
                if graph[nx][ny] == 0: # 청소안된곳이 있으면
                    x, y, d = nx, ny, k
                    state = False # 현재if문과 while문 탈출해서
                    break # 첫번째 while문으로 가서 청소표시, cnt+1
            else:
                # for문에서 while문 탈출 안되고 여기까지 온거면
                # 4방향 다 청소가 되어있거나 벽임
                nx, ny = x-dx[d], y-dy[d] # 바로보는 방향에서 후진
                if graph[nx][ny] == 1: # 뒤가 벽이면 종료
                    return
                else: # 벽이 아니면 그쪽부터 다시 청소
                    x, y = nx, ny
                    
                    


N, M = map(int, input().split())
x, y, d = map(int, input().split())
# d = 0:상 1:우 2:하 3:좌
graph = [list(map(int ,input().split())) for _ in range(N)]
cnt = 0
cal(x, y, d)
print(cnt)