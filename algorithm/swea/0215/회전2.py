T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = (list(map(int, input().split())))
    front = 0
    rear = N - 1
    front += M
    rear += M
    front %= N
    rear %= N 
    print(f"#{tc} {arr[front]}")