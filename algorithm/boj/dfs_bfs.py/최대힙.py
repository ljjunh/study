'''
2 5 3 6 4
'''
# 최대힙
def enq(n):
    global last
    # 마지막 노드 추가(완전 이진 트리 유지)
    last += 1
    # 마지막 노드에 데이터 삽입
    h[last] = n
    # 부모 > 자식 비교를 위해
    c = last
    p = c // 2 # 부모 번호 계산
    while p and h[p] < h[c]: # 부모가 존재하고, 부모가 자식보다 작으면
        h[p], h[c] = h[c], h[p] # 교환
        c = p
        p = c // 2

# 힙 - 삭제연산
def deq():
    global last
    tmp = h[1] # 루트를 잠시 보관
    h[1] = h[last]
    last -= 1
    p = 1 # 새로 옮긴 루트
    c = p * 2
    while c <= last: # 자식이 하나라도 있으면
        if c + 1 <= last and h[c] < h[c + 1]: # 오른쪽 자식이 있고 더 크면
            c += 1
        if h[p]  < h[c]:
            h[p], h[c] = h[c], h[p]
            p = c
            c = p * 2
        else:
            break
    return tmp



N = 10 # 필요한 노드 수
h = [0] * (N + 1) # 최대힙
last = 0 # 힙의 마지막 노드 번호
enq(2)
enq(5)
enq(3)
enq(6)
enq(4)
#print(h)
while last > 0:
    print(deq())