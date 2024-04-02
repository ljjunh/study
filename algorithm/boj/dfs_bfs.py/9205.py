import sys
input = sys.stdin.readline
from collections import deque

def bfs(x, y):
    global N, ex, ey
    visited = [0] * N
    q = deque()
    q.append((x, y))
    while q:
        cx, cy = q.popleft()
        if abs(cx-ex) + abs(cy-ey) <= 1000: # 마지막 편의점에서 도착지까지 1000m내에 갈 수 있으면 happy
            return "happy"
        for i in range(N):
            if visited[i] == 0: # 미방문 편의점
                nx, ny = arr[i]
                if abs(cx-nx) + abs(cy-ny) <= 1000: #다음 편의점까지 갈 수 있으면
                    q.append((nx, ny))
                    visited[i] = 1
    return "sad" #도착지까지 1000m내에 갈 수 없으면 sad
    
T = int(input())
for _ in range(T):
    N = int(input())
    sx, sy = map(int, input().split()) # 집
    arr = [] # 편의점
    for i in range(N):
        a, b = map(int, input().split())
        arr.append((a, b))
    ex, ey = map(int, input().split()) # 도착지
    print(bfs(sx, sy))
