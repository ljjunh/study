A = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
N = len(A)

cnt = 0
K = 0
# 1. 재귀
# 합이 K인 부분집합을 구하는 재귀함수

def subset(n, K, idx, selected):
    global cnt

    if idx == N:
        if sum(selected) == K:
            cnt += 1
            print(selected)
        return
    
    # idx 선택o
    subset(N, K, idx + 1, selected + [A[idx]])

    # idx 선택x 
    subset(N, K, idx + 1, selected)

subset(N, K, 0, [])
print(cnt)


# 바이너리카운팅
cnt = 0
for i in range(1 << N):
    ith_bin = i # i번째 부분집합을 이진수로 바꿔서 생각하자
    ith_set = [] # i번째 부분집합에 포함할 원소
    for j in range(N): # 2진수를 오른쪽으로 j번 밀어보기
        if ith_bin & 0x1:
            ith_set.append(A[j])
        ith_bin >>= 1
    if sum(ith_set) == 0:
        cnt += 1
        print(ith_set)
print(cnt)