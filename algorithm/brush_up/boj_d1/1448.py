import sys
input = sys.stdin.readline
n = int(input())
m = sorted([int(input()) for _ in range(n)], reverse=True) # 내림차순으로 해야 최댓값이 나옴
result = -1 # result에 아무것도 안들어가면 -1출력할꺼라 -1 넣었음. 값이 들어가면 알아서 초기화
for i in range(n - 2): # 3개씩 뽑는거라 뒤에 2개는 반복을 돌면 안됨
    if m[i] < m[i + 1] + m[i + 2]:
        result = m[i] + m[i + 1] + m[i + 2]
        break
print(result) 