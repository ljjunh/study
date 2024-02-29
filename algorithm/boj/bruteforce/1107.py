import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
impossible = list(map(int, input().split()))
# +, -로만 이동하는 경우
ans = abs(100 - N)

for i in range(1000001):
    temp = str(i)
    for j in range(len(temp)):
        if int(temp[j]) in impossible:
            break
        elif j == len(temp) - 1: # 중간에 안멈추고 끝까지 오면
            ans = min(ans, abs(int(temp) - N) + len(temp))
            #ans는 temp와 N의 차이 절대값 + temp의 길이(버튼 입력)
print(ans)