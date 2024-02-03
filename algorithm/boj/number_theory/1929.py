import math
M, N = map(int, input().split())
# 1. 배열초기화 (인덱스 = 값)
arr = [0] * (N+1) #0은 사용안하니까 N+1개 만들어야 1부터N까지 배열 만들어짐
for i in range(2, N+1): # 1은 소수가 아니니까 2부터 시작
    arr[i] = i
# 2. 소수만 남기고 약수가 있는 숫자들 다 지우기
for i in range(2, int(math.sqrt(N))+1): # 2부터 N의 제곱근까지의 배수 모두 삭제
    if arr[i] == 0: # 소수가 아니면 다음반복으로 넘어감
        continue
    for j in range(i + i, N + 1, i): # i의 배수부터 끝까지 i스텝으로 넘어가야 4,6,8,10..., 6,9,12,15, 8,16.. 사라짐
        arr[j] = 0
for i in range(M, N + 1): #m부터 n범위의 소수만 출력
    if arr[i] != 0: # 0이 아니면 출력 즉 소수면 출력
        print(i)
        #print(arr[i]) #이렇게 뽑아도 상관없음 이미 인덱스=값 으로 넣어놔서
    
