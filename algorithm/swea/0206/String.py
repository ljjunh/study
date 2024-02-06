T = 10
for tc in range(1, T + 1):
    N = int(input())
    P = list(input()) # pattern
    T = input() # text
    ti = 0 # text인덱스
    pi = 0 # pattern인덱스
    tl = len(T) # text길이
    pl = len(P) # pattern길이
    cnt = 0
    # 비교 시작
    # ti, pi가 텍스트의 길이를 벗어나 버리면 비교할게 없으니까 반복종료
    while pi < pl and ti < tl:
        # 패턴의 pi위치와 텍스트의 ti를 비교한다.
        # 비교해서 같으면 ti += 1, pi += 1
        # 다르면 ti = ti - pi 
        # 다음 비교 시작 위치 = 현재 비교 위치 - 내가 비교한 횟수
        if T[ti] != P[pi]:
            ti = ti - pi
            pi = -1 #바로 아래서 +1 해주기때문에 0이아닌 -1로 써줌
        # 다음 비교 위치는 뒤로 1칸 이동
        ti = ti + 1
        pi = pi + 1

        # 만약 패턴 비교 인덱스가 패턴의 길이만큼 되버렸다면
        # 중간에 pi = 0으로 돌아간적이 없다는 소리고
        # 그 말은 지금까지 다 같았다. 라는 말이니 패턴을 찾았다는 의미
        if pi == pl:
            cnt += 1
            # 다음 탐색을 위해서 pi = 0
            pi = 0
            # 텍스트도 한칸 뒤로 이동해서 비교 시작
            ti = ti - pi
    print(f"#{tc} {cnt}")