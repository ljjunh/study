A = [1, 2, 3, 4, 5]
N = len(A)
# 원소의 개수가 R개인 부분집합 구하기
def subset(N, R, level, idx, selected):
    if level == R:
        print(selected)
        return
    
    # idx : 내가 고르기 시작하는 원소의 위치
    for i in range(idx, N):
        subset(N, R, level + 1, i + 1, selected + [A[i]])

subset(N, 3, 0, 0, [])
    