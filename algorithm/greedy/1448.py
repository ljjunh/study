import sys
input = sys.stdin.readline
N = int(input())
m = sorted([int(input()) for _ in range(N)], reverse=True)
result = -1 # 삼각형이 성립안되면 -1출력
for i in range(N - 2): # 값 3개를 뽑아야되서 뒤에 2개는 못씀
    if m[i] < m[i + 1] + m[i + 2]:
        result = m[i] + m[i + 1] + m[i + 2]
        break
print(result)
