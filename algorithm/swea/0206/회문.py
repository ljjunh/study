def palindrome(T):
    i = 0
    N = len(T) - 1
    temp = 0
    if len(T) % 2:
        while i != N:
            if T[i] == T[N]:
                temp = 1
            else:
                temp = 0
                return temp
            i += 1
            N -= 1
            if i == N:
                return temp
    else:
        while i < N:
            if T[i] == T[N]:
                temp = 1
            else:
                temp = 0
                return temp
            i += 1
            N -= 1
            if i > N:
                return temp
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    res = 0
    row = []
    col = []
    for i in range(N):
        text = input()
        row.append(text)
    for i in range(N):
        text_col = ''
        for j in range(N):
            text_col += row[j][i]
        col.append(text_col)

    for x in row:
        for i in range(N-M+1):

            if palindrome(x[i:i+M]):
                res = x[i:i+M]
    if res == 0:
        for y in col:
            for i in range(N-M+1):

                if palindrome(y[i:i+M]):
                    res = y[i:i+M]

    print(f'#{tc} {res}')