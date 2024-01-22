from collections import deque
import sys

input = sys.stdin.readline
T = int(input())
for i in range(T):
    n, m = map(int, input().split())
    que = deque(list(map(int, input().split())))
    count = 0
    while que:
        best = max(que)
        front = que.popleft()
        m -= 1
        if best == front:
            count += 1
            if m < 0:
                print(count)
                break
        else:
            que.append(front)
            if m < 0:
                m = len(que) -1

                        
        # best = max(que) # 현재 큐 최대값
        # front = que.popleft() # 큐의 front 뽑음
        # m -= 1 # front 뽑았으니까 한칸당겨짐

        # if best == front: #최댓값 뽑았을때
        #     count += 1 # 하나가 출력되니까 순번 하나추가
        #     if m < 0: # m이 0이라는 것은 뽑은게 내가 원하는 숫자라는거
        #         print(count)
        #         break
        # else: # 뽑은 숫자가 제일 큰 숫자가 아니면
        #     que.append(front) # 제일 뒤로 밀려남
        #     if m < 0: # 제일 앞에서 뽑히면
        #         m = len(que) -1 # 제일 뒤로 이동
