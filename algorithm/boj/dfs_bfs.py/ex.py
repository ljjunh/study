import math
order = 1
r = 5.73  # 공의 반지름
hole_distance = 999999999  # 가까운 홀을 찾기 위해 큰 값을 임의로 지정
whiteBall_x = balls[0][0] # 흰공의 x좌표
whiteBall_y = balls[0][1] # 흰공의 y좌표

player_one = [3, 1, 5]
player_two = [2, 4, 5]
if order == 1: # order가 1이면 선공
    for a in player_one:
        if balls[a][0] >= 1: # 공의 x좌표가 1 이상이면(테이블을 안벗어났으면) 
            targetBall_x = balls[a][0] # 타겟볼에 할당 
            targetBall_y = balls[a][1]
            break
elif order == 2: # order가 2면 후공
    for b in player_two:
        if balls[b][0] >= 1:
            targetBall_x = balls[b][0]
            targetBall_y = balls[b][1]
            break

    # 타격포인트와 비교
distance = math.sqrt((targetBall_x - whiteBall_x) ** 2 + (targetBall_y - whiteBall_y) ** 2) #피타고라스로 거리계산
target_x = targetBall_x # 선공 후공에 따라 타겟볼 좌표 할당
target_y = targetBall_y
    
    # HOLES = [[0, 0], [127, 0], [254, 0], [0, 127], [127, 127], [254, 127]]

for i in range(6): # 가장 가까운 홀 찾기
    x = HOLES[i][0]
    y = HOLES[i][1]

    hit_width = abs(x - targetBall_x) # 현재 반복중인 홀과 타겟볼 거리 계산
    hit_height = abs(y - targetBall_y) # 현재 반복중인 홀과 타겟볼 거리 계산

    hole_radian = math.atan(hit_width / hit_height) # 타겟볼과 홀의 가로, 세로 거리를 사용해서 홀과의 각도 계산

    hit_x = targetBall_x
    hit_y = targetBall_y

        # 1사분면 ++
    if targetBall_x > x and targetBall_y > y:
        hit_x += (r * math.sin(hole_radian))
        hit_y += (r * math.cos(hole_radian))
        # 4사분면 +-
    elif targetBall_x > x and targetBall_y < y:
        hit_x += (r * math.sin(hole_radian))
        hit_y -= (r * math.cos(hole_radian))
        # 3사분면 --
    elif targetBall_x < x and targetBall_y < y:
        hit_x -= (r * math.sin(hole_radian))
        hit_y -= (r * math.cos(hole_radian))
        # 2사분면 -+
    elif targetBall_x < x and targetBall_y > y:
        hit_x -= (r * math.sin(hole_radian))
        hit_y += (r * math.cos(hole_radian))

        # 타격포인트와 흰공까지의 거리
    target_distance = math.sqrt((hit_x - whiteBall_x) ** 2 + (hit_y - whiteBall_y) ** 2)
        # 타격포인트가 타격볼보다 가까운 경우에만
    if distance > target_distance:
            # 홀까지 거리를 계산하고
        target_hole = math.sqrt((targetBall_x - HOLES[i][0]) ** 2 + (targetBall_y - HOLES[i][1]) ** 2)
            # 가장 가까운 홀 찾기
        if hole_distance > target_hole:
            hole_distance = target_hole
            target_x = hit_x
            target_y = hit_y

width = abs(target_x - whiteBall_x)
height = abs(target_y - whiteBall_y)

radian = math.atan(width / height)
angle = 180 / math.pi * radian
    # 타겟구가 1사분면에 위치
if target_x > whiteBall_x and target_y > whiteBall_y:
    radian = math.atan(width / height)
    angle = 180 / math.pi * radian
    # 타겟구가 4사분면에 위치
elif target_x > whiteBall_x and target_y < whiteBall_y:
    radian = math.atan(height / width)
    angle = (180 / math.pi * radian) + 90
    # 타겟구가 3사분면에 위치
elif target_x < whiteBall_x and target_y < whiteBall_y:
    radian = math.atan(width / height)
    angle = (180 / math.pi * radian) + 180
    # 타겟구가 2사분면에 위치
elif target_x < whiteBall_x and target_y > whiteBall_y:
    radian = math.atan(height / width)
    angle = (180 / math.pi * radian) + 270

distance = math.sqrt(width ** 2 + height ** 2)
power = (distance * 1.2 + hole_distance * 0.8) / 3.75