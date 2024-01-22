import sys
N = int(input())
deque = [] #deque로 만드는게 낫지만 리스트로 해봄
for _ in range(N):
    order = sys.stdin.readline().split()
    if order[0] == "push_front":
        deque.insert(0, order[1])
    elif order[0] == "push_back":
        deque.append(order[1])
    elif order[0] == "pop_front":
        if len(deque) == 0:
            print(-1)
        else:
            print(deque.pop(0))
    elif order[0] == "pop_back":
        if len(deque) == 0:
            print(-1)
        else:
            print(deque.pop())
    elif order[0] == "size":
        print(len(deque))
    elif order[0] == "empty":
        if len(deque) == 0:
            print(1)
        else:
            print(0)
    elif order[0] == "front":
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[0])
    elif order[0] == "back":
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[-1])

