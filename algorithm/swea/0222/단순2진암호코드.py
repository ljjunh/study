password = [[0,0,0,1,1,0,1], [0,0,1,1,0,0,1], [0,0,1,0,0,1,1],[0,1,1,1,1,0,1],[0,1,0,0,0,1,1],[0,1,1,0,0,0,1],[0,1,0,1,1,1,1],[0,1,1,1,0,1,1],[0,1,1,0,1,1,1],[0,0,0,1,0,1,1]]

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input())) for _ in range(N)]
    #뒤에서부터 세면서 첫번째 1이 나오면 그대로 56개 복사
    for i in range(N):
        for j in range(M-1, -1, -1):
            if arr[i][j] == 1:
                x, y = i, j
                break    
    temp = arr[x][y-55:y+1]
    res = []
    for i in range(7, 57, 7):
        temp2 = temp[i-7:i]
        for key, value in enumerate(password):
            if temp2 == value:
                res.append(key)
    odd_num = 0 # 홀수
    even_num = 0 # 짝수
    for i in range(len(res)): #인덱스0부터 시작하니까 홀수짝수 바꿈
        if i % 2 == 0:
            odd_num += res[i]
        elif i % 2 == 1:
            even_num += res[i]

    if (odd_num * 3 + even_num) % 10 == 0:
        print(f"#{tc} {sum(res)}")
    else:
        print(f"#{tc} 0")
        
        
