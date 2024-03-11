import sys
input = sys.stdin.readline
N, H = map(int, input().split())
graph = [0 for _ in range(H)]
for i in range(N):
    height = int(input())
    if i % 2 == 0:
        graph[H-height] += 1
    if i % 2 == 1:
        graph[0] += 1
        graph[height] -= 1
prefix = [0 for _ in range(H+1)]
for i in range(H):
    prefix[i+1] = prefix[i] + graph[i]
prefix = prefix[1:]
print(min(prefix), prefix.count(min(prefix)))