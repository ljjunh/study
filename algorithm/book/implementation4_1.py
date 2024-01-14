n = int(input())
plans = input().split()
print(plans)
x, y = 1, 1
# L, R, U, D 이동방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)): # 이동방향 수 만큼 반복
        if plan == move_types[i]: 
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n: #공간을 넘어가면 무시
        continue
    x, y = nx, ny
print(x, y)