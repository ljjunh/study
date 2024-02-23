T = 10

for tc in range(1, T+1):

    N = int(input())

    lst = list(map(int, input().split()))

    # 조망권 수
    count = 0

    # 전체 건물에 대해 반복
    for i in range(2, N - 2): # 양쪽 2칸은 비어있으니까 볼 필요 없다.
        height = lst[i] # i번 건물의 높이
        # i번 건물의 꼭대기 부터 시작해서 아래로 내려가면서 조망권 확보 검사
        # 건물의 층수에 대해서 반복
        for floor in range(height, -1, -1):
            # 해당 층에서 왼쪽과 오른쪽 검사
            # i-2, i-1, i+1, i+2 번째 건물보다 현재 층수가 높은지 확인
            if floor > lst[i-2] and floor > lst[i-1] and floor > lst[i+1] and floor > lst[i+2]:
                count += 1
            else:
                # 이 층이 주변 건물보다 높이가 작아지면 이 밑층부터는 더 이상 확인 할 필요가 없다
                break
    print(f"#{tc} {count}")