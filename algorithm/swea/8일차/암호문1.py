T = 10
for tc in range(1, T + 1):
    N = int(input()) # 원본 암호문 길이
    og = input().split() # 원본 암호문
    M = int(input()) # 명령어 개수
    order = [list(map(int, i.split())) for i in input().split("I")[1:]]
    for i in range(M):
        idx, a, *values = order[i] #a는 안쓰는거
        og[idx:idx] = values # 그냥og[idx] = values하면 값이바뀌니까 이렇게씀
    print(f"#{tc}", *og[:10])