A = [7, 2, 5, 4, 3, 1, 6]
N = 7

# A안에서 원하는 값의 위치를 찾아 RETURN하는 함수
# 못찾은 경우는 -1을 리턴한다.
v = 1

for i in range(N):
    if A[i] == v:
        print(i)
        break
else:
    print(-1)


def search(idx, N, v):
    # 인덱스 범위를 벗어났는데 찾지 못했을 경우
    if idx == N:
        return -1
    # 인덱스 범위 안에서 v를 찾았다. 그 위치를 반환
    elif A[idx] == v:
        return idx
    
    # 다음 단계에서 결졍된 값을 리턴
    return search(idx + 1, N, v)
print(search(0, N, v))    
    