T = 10
for tc in range(1, T + 1):
    # N = 덤프횟수(상자를 옮길 수 있는 횟수)
    N = int(input())
    
    box = list(map(int, input().split()))
    
    # 횟수가 1 이상이면 계속 덤프 반복
    while N > 0:
        # 제일 높은 상자가 어디?
        max_idx = 0
        # 제일 높은 상자의 높이 값
        max_height = 0
        # 제일 낮은 상자가 어디?
        min_idx = 0
        # 제일 낮은 상자의 높이 값
        min_height = 100
        for i in range(100):
            # i번째 상자의 높이 : box[i]
            # i번째 상자의 높이가 내가 지금까지 알고있던 최대 높이보다 크면 변경
            if box[i] > max_height:
                max_height = box[i] # 최댓값 변경
                max_idx = i # 최댓값 위치 변경


            # i번째 상자의 높이가 내가 지금까지 알고있던 최저 높이보다 낮으면 변경
            if box[i] < min_height:
                min_height = box[i]
                min_idx = i
        # 100개의 상자를 다 확인하고 나서
        # 최대 상자 높이 -1, 최저 상자높이 + 1
        box[max_idx] -= 1
        box[min_idx] += 1

        # 덤프 1번 했으니까 횟수 1 감소
        N -= 1
    # 평탄화 작업을 끝내고 최댓값과 최솟값을 한번 더 확인
    max_height = 0
    min_height = 100
    for i in range(100):
        if box[i] > max_height:
            max_height = box[i]
        if box[i] < min_height:
            min_height = box[i]
    print(f"#{tc} {max_height - min_height}")
