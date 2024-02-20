T = int(input())

def inorder(t):
    global idx
    if t <= N:
        inorder(t * 2)
        tree[t] = idx 
        idx += 1
        inorder(t * 2 + 1)

for tc in range(1, T + 1):
    N = int(input())
    tree = [0] * (N + 1)
    idx = 1
    inorder(1)    
    print(f"#{tc} {tree[1]} {tree[N//2]}")
