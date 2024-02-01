T = int(input())
for tc in range(1, T + 1):
    P, A, B = map(int, input().split())

    # 누가 승자인가
    winner = ""

    # A와 B의 이진탐색 범위를 따로 선언
    A_start, A_end = 1, P
    B_start, B_end = 1, P

    #둘 중에 한 사람이라도 페이지를 찾을때까지 계속 반복
    while True:
        A_find = False # A가 페이지를 찾았는지 여부
        B_find = False # B가 페이지를 찾았는지 여부

        # A이진탐색 1번
            #A가 찾았다 -> A_find = True
        
        # B 이진탐색 1번
            # B가 찾았다 -> B_find = True
        

        # 승자를 결정
        # A만 찾았다 -> A승
        # B만 찾았다 -> B승
        # 둘다 찾았다 -> 무승부
        # 반복종료(승부가 결정된 경우만)