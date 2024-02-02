T = int(input())
for tc in range(1, T + 1):
    D, A, B, F = map(int, input().split())

    temp = D / (B + F) # 파리랑 B가 만나는데 걸리는 시간 7.14
    temp2 = D / (A + B) # A랑B가 만나는데 걸리는시간 10.0
    temp3 = (temp2 - temp) # 2.857...동안 파리가 왔다갔다함 
    print(f"#{tc} {(temp3 * F) + (temp * F)}")