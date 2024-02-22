T = int(input())
for tc in range(1, T + 1):
    N, hex_num = input().split()
    N = int(N)
    # 전체 16진수를 2진수로 바꾼 결과
    answer = ""
    # i 번째 16진수를 2진수로 바꾸고, answer에 추가
    ith_num = int(hex_num, 16)
    while ith_num != 0:
        answer += str(ith_num % 2)
        ith_num //= 2
    res = ""
    if len(answer) % 4 != 0:
        res = "0"
    res += answer[::-1]
    print(f"#{tc}", res)