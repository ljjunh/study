arr = ["A", "B", "C", "D", "E"]
n = len(arr)

def get_sub(tar):
    cnt = 0
    for i in range(n):
        # 1비트가 1인지 확인하는 코드
        if tar & 0x1:
            cnt += 1
        # right shift 비트 연산자 -> 오른쪽 끝 비트를 하나씩 제거
        tar >>= 1
    return cnt
        
result = 0
for tar in range(1 << n):
    if get_sub(tar) >= 2: # 비트가 2개이상 1이라면 ->2명 이상이라면
        result += 1
print(result)