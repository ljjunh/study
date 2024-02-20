def preorder(T):
    global answer
    if T:
        answer.append(T)
        preorder(left[T])
        preorder(right[T])

T = int(input())
for tc in range(1, T + 1):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))
    left =[0] * (E + 2) 
    right = [0] * (E + 2)
    answer = []
    for i in range(E):
        p, c = arr[i * 2], arr[i * 2 + 1]
        if left[p] == 0:
            left[p] = c
        else:
            right[p] = c
    preorder(N)
    print(f"#{tc} {len(answer)}")