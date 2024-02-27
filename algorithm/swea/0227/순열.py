path = []
def type1(x): # 중복순열
    if x == N:
        print(path)
        return
    for i in range(1, 7):
        path.append(i)
        type1(x+1)
        path.pop()

visited = [False] * 7

def type2(x): # 순열
    if x == N:
        print(path)
        return
    for i in range(1, 7):
        if not visited[i]:
            visited[i] = True
            path.append(i)
            type2(x+1)
            path.pop()
            visited[i] = False

N, type = map(int, input().split())
if type == 1:
    type1(0) # 중복순열
elif type == 2:
    type2(0) # 순열
