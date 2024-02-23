from collections import deque
# 암호 뽑고 10진수로 바꾸고 2진수로 바꾸고 뒤에 있는 0 다 지우고 길이 56개에 맞춰서 앞에 0 추가
password = [[0,0,0,1,1,0,1], [0,0,1,1,0,0,1], [0,0,1,0,0,1,1],[0,1,1,1,1,0,1],[0,1,0,0,0,1,1],[0,1,1,0,0,0,1],[0,1,0,1,1,1,1],[0,1,1,1,0,1,1],[0,1,1,0,1,1,1],[0,0,0,1,0,1,1]]

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    temp = []
    chk = 0
    state = False
    for i in range(N):
        for j in range(M):
            if arr[i][j] != "0":
                temp.append(arr[i][j:])
                chk = 1
                break
        if chk == 1:
            break
    pass16 = "" # 16진수 암호
    for i in temp[0]:
        pass16 += i
    pass10 = int(pass16, 16)
    pass2 = deque(str(bin(pass10))[2:])
    
    cnt = 0
    for i in range(len(pass2) - 1, 0, -1):
        if pass2[i] == "1":
           break
        elif pass2[i] == "0":
            cnt += 1
    print(cnt)

            