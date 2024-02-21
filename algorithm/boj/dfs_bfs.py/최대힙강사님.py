# 최대 힙
heap = [0] * 11
# 마지막에 넣은 원소 위치
last = 0

# 삽입 연산
def enq(item):
    global last
    last += 1 # 마지막원소 한칸 뒤에 넣어야 함
    heap[last] = item

    # 원소를 추가하고 나서 (부모노드 > 자식노드) 조건을 만족하도록 해야함
    # 현재 위치를 자식 노드라고 생각
    # 비교할 부모노드의 위치를 계산 (2로 나누면 계산 가능)
    c = last
    p = c // 2

    # 부모노드가 존재하고, 부모노드가 자식노드보다 작으면 자리 교환
    while p and heap[p] < heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        # 그 위에 있는 부모와 비교를 계속 해야하기 때문에 위치 변경
        c = p
        p = c // 2

# 삭제 연산
def deq():
    global last
    # 루트노드를 삭제할껀데 이따가 자리 바꿔야 하니까 미리 기억
    root = heap[1]
    # 마지막 위치에 있던 노드를 루트 위치로 땡겨온다.
    heap[1] = heap[last]
    # 원소를 하나 삭제했으니까 마지막 원소 위치를 한칸 땡겨온다
    last -= 1

    # 루트로 마지막 원소를 땡겨 왔는데
    # 그 원소가 루트가 될 자격이 있나??(부모노드 > 자식노드)
    p = 1
    c = p * 2 # 왼쪽 자식p * 2, 오른쪽자식 p * 2 + 1

    # 자리 조정
    # 최대 힙은 부모가 자식보다 커야함
    # 부모가 자식보다 적으면 자리를 계속 교환
    
    # 자식이 존재하면 비교
    while c <= last:
        # 왼쪽 자식이 있으면 오른쪽 자식도 있나 확인
        # 둘 중에 큰거랑 부모랑 자리를 바꿀거임
        if c + 1 <= last and heap[c] < heap[c+1]:
            # 오른쪽 자식이 있고 오른쪽 자식이 왼쪽자식보다 더 크면
            c = c + 1
        # 자식이 부모보다 큰가 확인
        if heap[p] < heap[c]:
            # 자리교환
            heap[p], heap[c] = heap[c], heap[p]
            p = c # 자식을 새로운 부모로 생각하고
            c = c * 2 # 왼쪽 자식을 기준으로 다시 비교 시작
        else:
            # 나보다 큰 자식이 없으면 제자리를 찾았다는거
            # 반복 중단
            break
    # 원래 root 리턴
    return root



arr = [6, 4, 5, 1, 3, 2, 9, 7, 8, 10]
for i in arr:
    enq(i)

print(heap)


# 힙 정렬
# 삭제연산할때 나오는 순서대로 빈 리스트에 append 해주면 내림차순 정렬됨
sorted_arr = []

for i in range(10):
    sorted_arr.append(deq())
print(sorted_arr)