import sys
def recur(cnt, num):
    if cnt == N:
        recur(0, num+1)
        ans += 1
        return

    if num == 1000:
        return
    
    strike_count = 0
    ball_count = 0
    a = num // 100
    b = (num // 10) // 10
    c = num % 10
    if a == arr[cnt][0]//100 :
        strike_count += 1
    if a == (arr[cnt][0]//10)//10 or a == arr[cnt][0] % 10:
        ball_count += 1
    if b == arr[cnt][0] // 10:
        strike_count += 1
    if b == arr[cnt][0]//100 or b == arr[cnt][0] % 10:
        ball_count += 1
    if c == arr[cnt][0] % 10:
        strike_count += 1
    if c == arr[cnt][0] // 100 or (arr[cnt][0]//10) // 10:
        ball_count += 1
    

    # 만약 힌트를 통과했다면
    # if 스트라이크 카운트랑 볼 카운트가 입력값이랑 동일하다면 
    if strike_count == arr[cnt][1] and ball_count == arr[cnt][2]:
        recur(cnt+1, num)
    # 만약 힌트에 통과하지 못한다면
    else:
        recur(0, num+1)

input = sys.stdin.readline
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0
recur(0, 100)
print(ans)